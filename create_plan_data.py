import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from plans_df import plans_df


# Assuming previous plans_df is already created

# Step 1: Extract the prefix letter from provider
plans_df['prefix'] = plans_df['provider'].str[0].str.upper()

# Step 2: Create a group counter per prefix
plans_df['count'] = plans_df.groupby('prefix').cumcount() + 1

# Step 3: Concatenate prefix and count for unique plan ID
plans_df['plan_id'] = plans_df['prefix'] + plans_df['count'].astype(str)

# Optionally drop helper columns if no longer needed
plans_df = plans_df.drop(columns=['prefix', 'count'])

# Pop plan_id column out
plan_id_col = plans_df.pop('plan_id')

# Insert plan_id as the first column (position 0)
plans_df.insert(0, 'plan_id', plan_id_col)

# 2. Prepare base usage dictionaries and customer profiles
customer_profiles = {
    "Young_Professional": {"age_range": (22, 35), "usage_pattern": "high", "seasonal_variance": 0.15, "growth_rate": 0.025, "network_preference": "5G", "plan_preference": "Medium", "probability": 0.30},
    "Family_User": {"age_range": (30, 50), "usage_pattern": "medium", "seasonal_variance": 0.20, "growth_rate": 0.015, "network_preference": "5G", "plan_preference": "High", "probability": 0.25},
    "Senior": {"age_range": (55, 75), "usage_pattern": "low", "seasonal_variance": 0.10, "growth_rate": 0.005, "network_preference": "4G", "plan_preference": "Low", "probability": 0.20},
    "Student": {"age_range": (18, 25), "usage_pattern": "medium", "seasonal_variance": 0.25, "growth_rate": 0.020, "network_preference": "5G", "plan_preference": "Medium", "probability": 0.15},
    "Business_User": {"age_range": (25, 55), "usage_pattern": "high", "seasonal_variance": 0.12, "growth_rate": 0.018, "network_preference": "5G+", "plan_preference": "High", "probability": 0.10}
}
base_usage = {
    "low": {"mean": 4.5, "std": 1.5},
    "medium": {"mean": 8.2, "std": 2.8},
    "high": {"mean": 15.5, "std": 4.2}
}
sask_cities = ["Saskatoon", "Regina", "Prince Albert", "Moose Jaw", "Swift Current", "Yorkton", "North Battleford", "Estevan", "Weyburn", "Lloydminster"]

# Helper functions
def generate_customer_profile():
    customer_type = np.random.choice(list(customer_profiles.keys()), p=[p["probability"] for p in customer_profiles.values()])
    profile = customer_profiles[customer_type]
    return {
        "customer_type": customer_type,
        "age": random.randint(*profile["age_range"]),
        "city": random.choice(sask_cities),
        "usage_pattern": profile["usage_pattern"],
        "seasonal_variance": profile["seasonal_variance"],
        "growth_rate": profile["growth_rate"],
        "network_type": profile["network_preference"],
        "plan_category": profile["plan_preference"]
    }

def generate_monthly_usage(base_usage_gb, months, growth_rate, seasonal_variance):
    usage_data = []
    for month in range(months):
        trend_factor = (1 + growth_rate) ** month
        month_of_year = (month % 12) + 1
        if month_of_year in [12, 1, 2, 3]:
            seasonal_factor = 1 + (seasonal_variance * 0.8)
        elif month_of_year in [6, 7, 8]:
            seasonal_factor = 1 + (seasonal_variance * 0.6)
        else:
            seasonal_factor = 1 + (seasonal_variance * 0.2)
        noise_factor = np.random.normal(1, 0.1)
        monthly_usage = base_usage_gb * trend_factor * seasonal_factor * noise_factor
        monthly_usage = max(monthly_usage, 0.5)
        usage_data.append(round(monthly_usage, 2))
    return usage_data

# Generate customers and usage data
num_customers = 750
months_history = 18
customers_data = []
usage_data = []

for customer_id in range(1, num_customers + 1):
    profile = generate_customer_profile()
    # Select plan with matching category and network type
    available_plans = plans_df[(plans_df['category'] == profile['plan_category']) & (plans_df['network'].str.contains(profile['network_type'][0]))]
    selected_plan = available_plans.sample(1).iloc[0] if not available_plans.empty else plans_df.sample(1).iloc[0]
    plan_id = selected_plan['plan_id']

    usage_params = base_usage[profile["usage_pattern"]]
    base_monthly_usage = max(np.random.normal(usage_params["mean"], usage_params["std"]), 1.0)
    monthly_usage = generate_monthly_usage(base_monthly_usage, months_history, profile["growth_rate"], profile["seasonal_variance"])

    customer_record = {
        "customer_id": customer_id,
        "customer_type": profile["customer_type"],
        "age": profile["age"],
        "city": profile["city"],
        "provider": selected_plan["provider"],
        "plan_id": plan_id,
        "plan_name": selected_plan["plan_name"],
        "plan_type": selected_plan["plan_type"],
        "plan_category": selected_plan["category"],
        "data_allowance_gb": selected_plan["data_gb"],
        "monthly_price_cad": selected_plan["price_cad"],
        "network_type": selected_plan["network"],
        "contract_months": selected_plan["contract_months"]
    }
    customers_data.append(customer_record)

    start_date = datetime(2024,1,1)
    for month_idx, usage_gb in enumerate(monthly_usage):
        usage_date = start_date + timedelta(days=30 * month_idx)
        usage_record = {
            "customer_id": customer_id,
            "usage_date": usage_date.strftime("%Y-%m-%d"),
            "usage_gb": usage_gb,
            "plan_allowance_gb": selected_plan["data_gb"],
            "plan_id": plan_id,
            "overage_gb": max(0, usage_gb - selected_plan["data_gb"]),
            "month_year": usage_date.strftime("%Y-%m")
        }
        usage_data.append(usage_record)

customers_df = pd.DataFrame(customers_data)
usage_df = pd.DataFrame(usage_data)

# Save updated files
plans_df.to_csv('saskatchewan_telecom_plans_2025_with_id.csv', index=False)
customers_df.to_csv('saskatchewan_customers_2025_with_plan_id.csv', index=False)
usage_df.to_csv('saskatchewan_usage_data_2025_with_plan_id.csv', index=False)
