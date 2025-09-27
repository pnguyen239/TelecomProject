import pandas as pd

# Define the list of plans (based on the previous data)
plans_data = [
    {"provider": "SaskTel", "plan_name": "Basic Nationwide 15", "plan_type": "Postpaid", "data_gb": 15, "price_cad": 85, "network": "5G", "category": "Low", "contract_months": 24},
    {"provider": "SaskTel", "plan_name": "VIP 70", "plan_type": "Postpaid", "data_gb": 70, "price_cad": 70, "network": "5G", "category": "Medium", "contract_months": 24},
    {"provider": "SaskTel", "plan_name": "VIP 125", "plan_type": "Postpaid", "data_gb": 125, "price_cad": 80, "network": "5G", "category": "High", "contract_months": 24},
    {"provider": "SaskTel", "plan_name": "totalSHARE Nationwide 50", "plan_type": "Postpaid", "data_gb": 50, "price_cad": 95, "network": "5G", "category": "Medium", "contract_months": 24},
    {"provider": "SaskTel", "plan_name": "noSTRINGS 10GB", "plan_type": "Prepaid", "data_gb": 10, "price_cad": 45, "network": "4G", "category": "Low", "contract_months": 0},
    {"provider": "SaskTel", "plan_name": "noSTRINGS 25GB", "plan_type": "Prepaid", "data_gb": 25, "price_cad": 65, "network": "5G", "category": "Medium", "contract_months": 0},

    {"provider": "Telus", "plan_name": "5G Standard 60GB", "plan_type": "Postpaid", "data_gb": 60, "price_cad": 60, "network": "5G", "category": "Medium", "contract_months": 24},
    {"provider": "Telus", "plan_name": "5G+ Complete 100GB", "plan_type": "Postpaid", "data_gb": 100, "price_cad": 80, "network": "5G", "category": "High", "contract_months": 24},
    {"provider": "Telus", "plan_name": "5G+ Complete Explore", "plan_type": "Postpaid", "data_gb": 150, "price_cad": 110, "network": "5G", "category": "High", "contract_months": 24},
    {"provider": "Telus", "plan_name": "Essential Plan", "plan_type": "Postpaid", "data_gb": 10, "price_cad": 35, "network": "4G", "category": "Low", "contract_months": 24},
    {"provider": "Telus", "plan_name": "Prepaid 15GB", "plan_type": "Prepaid", "data_gb": 15, "price_cad": 40, "network": "4G", "category": "Low", "contract_months": 0},
    {"provider": "Telus", "plan_name": "Prepaid 25GB", "plan_type": "Prepaid", "data_gb": 25, "price_cad": 55, "network": "5G", "category": "Medium", "contract_months": 0},

    {"provider": "Bell", "plan_name": "Select 100GB", "plan_type": "Postpaid", "data_gb": 100, "price_cad": 85, "network": "5G+", "category": "High", "contract_months": 24},
    {"provider": "Bell", "plan_name": "Max CAN-US 175GB", "plan_type": "Postpaid", "data_gb": 175, "price_cad": 120, "network": "5G+", "category": "High", "contract_months": 24},
    {"provider": "Bell", "plan_name": "Essential 25GB", "plan_type": "Postpaid", "data_gb": 25, "price_cad": 50, "network": "5G", "category": "Medium", "contract_months": 24},
    {"provider": "Bell", "plan_name": "Basic Talk & Text", "plan_type": "Postpaid", "data_gb": 5, "price_cad": 30, "network": "4G", "category": "Low", "contract_months": 24},
    {"provider": "Bell", "plan_name": "Prepaid 20GB", "plan_type": "Prepaid", "data_gb": 20, "price_cad": 45, "network": "4G", "category": "Medium", "contract_months": 0},
    {"provider": "Bell", "plan_name": "Prepaid 40GB", "plan_type": "Prepaid", "data_gb": 40, "price_cad": 65, "network": "5G", "category": "Medium", "contract_months": 0},

    {"provider": "Rogers", "plan_name": "Essentials 75GB", "plan_type": "Postpaid", "data_gb": 75, "price_cad": 70, "network": "5G+", "category": "Medium", "contract_months": 24},
    {"provider": "Rogers", "plan_name": "Popular 125GB", "plan_type": "Postpaid", "data_gb": 125, "price_cad": 80, "network": "5G+", "category": "High", "contract_months": 24},
    {"provider": "Rogers", "plan_name": "Ultimate 250GB", "plan_type": "Postpaid", "data_gb": 250, "price_cad": 100, "network": "5G+", "category": "High", "contract_months": 24},
    {"provider": "Rogers", "plan_name": "Basic 15GB", "plan_type": "Postpaid", "data_gb": 15, "price_cad": 45, "network": "5G", "category": "Low", "contract_months": 24},
    {"provider": "Rogers", "plan_name": "chatr 12GB", "plan_type": "Prepaid", "data_gb": 12, "price_cad": 40, "network": "4G", "category": "Low", "contract_months": 0},
    {"provider": "Rogers", "plan_name": "chatr 30GB", "plan_type": "Prepaid", "data_gb": 30, "price_cad": 60, "network": "4G", "category": "Medium", "contract_months": 0},

    {"provider": "Public Mobile", "plan_name": "Basic 3GB", "plan_type": "Prepaid", "data_gb": 3, "price_cad": 25, "network": "4G", "category": "Low", "contract_months": 0},
    {"provider": "Public Mobile", "plan_name": "Standard 20GB", "plan_type": "Prepaid", "data_gb": 20, "price_cad": 40, "network": "5G", "category": "Medium", "contract_months": 0},
    {"provider": "Public Mobile", "plan_name": "Plus 60GB", "plan_type": "Prepaid", "data_gb": 60, "price_cad": 45, "network": "5G", "category": "Medium", "contract_months": 0},
    {"provider": "Public Mobile", "plan_name": "Premium 80GB", "plan_type": "Prepaid", "data_gb": 80, "price_cad": 50, "network": "5G", "category": "High", "contract_months": 0},
    {"provider": "Public Mobile", "plan_name": "Value 10GB", "plan_type": "Prepaid", "data_gb": 10, "price_cad": 35, "network": "4G", "category": "Low", "contract_months": 0}
]

# Create DataFrame
plans_df = pd.DataFrame(plans_data)

# Display the first few rows to check
print(plans_df.head())

