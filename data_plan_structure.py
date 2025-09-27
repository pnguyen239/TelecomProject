# Create a comprehensive plan data collection structure for Saskatchewan telecom providers
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import json

# Top 5 Saskatchewan Telecom Providers based on research
providers = {
    "SaskTel": {"market_share": 45, "network": ["4G", "5G"], "coverage": "Excellent"},
    "Telus": {"market_share": 20, "network": ["4G", "5G"], "coverage": "Good"},
    "Bell": {"market_share": 15, "network": ["4G", "5G"], "coverage": "Good"},
    "Rogers": {"market_share": 12, "network": ["4G", "5G"], "coverage": "Fair"},
    "Public Mobile": {"market_share": 8, "network": ["4G", "5G"], "coverage": "Good"}
}

# Plan structure for Low, Medium, High data categories
plan_structure = {
    "Low": {"data_range": "1-15GB", "price_range": "$25-45"},
    "Medium": {"data_range": "16-75GB", "price_range": "$46-85"},
    "High": {"data_range": "76GB+", "price_range": "$86-120"}
}

print("SASKATCHEWAN TELECOM PROJECT - DAY 1 PLAN")
print("="*50)
print("\n1. TOP 5 SASKATCHEWAN TELECOM PROVIDERS:")
for provider, data in providers.items():
    print(f"   • {provider}: {data['market_share']}% market share, {', '.join(data['network'])} network")

print("\n2. PLAN CATEGORIES IDENTIFIED:")
for category, details in plan_structure.items():
    print(f"   • {category} Data: {details['data_range']}, Price: {details['price_range']}")

# Key metrics for Business Analyst role
business_metrics = {
    "ARPU": {
        "definition": "Average Revenue Per User",
        "canada_benchmark": "$57-69 CAD/month (2024-2025)",
        "importance": "Primary profitability metric"
    },
    "Customer_Satisfaction": {
        "definition": "NPS, CSAT, CES scores",
        "canada_benchmark": "NPS: 30-50 (Telecom industry)",
        "importance": "Retention and loyalty indicator"
    },
    "Churn_Rate": {
        "definition": "Monthly customer turnover rate",
        "canada_benchmark": "1.5-2.5% monthly",
        "importance": "Customer retention metric"
    }
}

print("\n3. KEY BUSINESS METRICS TO TRACK:")
for metric, details in business_metrics.items():
    print(f"   • {metric}: {details['definition']}")
    print(f"     Benchmark: {details['canada_benchmark']}")
    print(f"     Purpose: {details['importance']}\n")

print("4. DATA COLLECTION REQUIREMENTS SUMMARY:")
print("   ✓ 5 Major providers identified")
print("   ✓ Postpaid & Prepaid plans for each provider")
print("   ✓ Low/Medium/High data categories")
print("   ✓ Network type (4G/5G) classification")
print("   ✓ Current 2025 pricing in CAD")
print("   ✓ Business metrics framework established")