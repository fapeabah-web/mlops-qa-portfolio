import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

np.random.seed(42)
# Dynamically points to your data folder matching your directory layout
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(base_dir, "data")
os.makedirs(data_dir, exist_ok=True)

print("🌾 Generating CANTERRA SEEDS Real-World SIPOC Infrastructure Datasets...")

# 1. SUPPLIERS STAGE: grower_suppliers
grower_ids = [f"GRW-{i:03d}" for i in range(1, 16)]
growers = ["Prairie Oats Farm", "Red River Seed Co", "Brandon Grain Growers", "Interlake Pedigreed Farms", "Pembina Valley Seeds"] * 3
regions = ["Manitoba-South", "Manitoba-West", "Saskatchewan-East", "Alberta-South", "Manitoba-Interlake"] * 3
df_growers = pd.DataFrame({
    'grower_id': grower_ids,
    'grower_name': growers,
    'region': regions,
    'contract_year': 2026
})

# 2. INPUTS STAGE: seed_batches
batch_ids = [f"LOT-2026-{i:03d}" for i in range(1, 51)]
crops = ['Pedigreed Wheat', 'Canola', 'Pulses/Peas', 'Barley', 'Oats']
crop_choices = np.random.choice(crops, size=50, p=[0.3, 0.3, 0.15, 0.15, 0.1])
df_batches = pd.DataFrame({
    'batch_id': batch_ids,
    'grower_id': np.random.choice(grower_ids, size=50),
    'crop_type': crop_choices,
    'received_date': [datetime(2026, 7, 1) + timedelta(days=int(np.random.randint(0, 60))) for _ in range(50)],
    'moisture_percentage': np.round(np.random.uniform(11.5, 16.5, size=50), 1)
})

# 3. PROCESS STAGE: processing_logs (Configured with Real-World Prairie Assets)
real_world_facilities = [
    'Winnipeg Corporate HQ', 
    'Manitoba Contract Growers', 
    'Saskatchewan Retail Networks', 
    'Alberta Co-op Distribution'
]
df_process = pd.DataFrame({
    'batch_id': batch_ids,
    'processing_facility': np.random.choice(real_world_facilities, size=50, p=[0.1, 0.4, 0.3, 0.2]),
    'quantity_metric_tons': np.random.randint(40, 300, size=50),
    'physical_audit_quantity_mt': np.random.randint(40, 300, size=50),
    'stock_status': np.random.choice(['In-Warehouse', 'In-Transit', 'Allocated'], size=50, p=[0.7, 0.2, 0.1])
})
# Introduce audit variances to test your metrics validation logic
df_process.loc[0:4, 'physical_audit_quantity_mt'] = df_process.loc[0:4, 'quantity_metric_tons'] - 2

# 4. OUTPUTS STAGE: inventory_valuations
df_valuations = pd.DataFrame({
    'batch_id': batch_ids,
    'cost_per_metric_ton': np.round(np.random.uniform(400, 1200, size=50), 2),
    'certified_seed_tag_id': [f"TAG-CA-70D-{i:03d}" for i in range(1, 51)],
    'auditor_verified': np.random.choice(['Yes', 'No'], size=50, p=[0.95, 0.05])
})

# 5. CUSTOMERS STAGE: retail_orders & partners
retail_ids = [f"RTL-{i:03d}" for i in range(1, 11)]
retails = ["Nutrien Ag Solutions", "Richardson Pioneer", "Federated Co-operatives Ltd", "Cargill Canada"] * 2 + ["Independent Dealer A", "Independent Dealer B"]
df_retailers = pd.DataFrame({
    'retail_id': retail_ids,
    'retail_partner_name': retails,
    'destination_province': np.random.choice(['MB', 'SK', 'AB'], size=10)
})

df_orders = pd.DataFrame({
    'order_id': [f"ORD-2026-{i:03d}" for i in range(1, 41)],
    'retail_id': np.random.choice(retail_ids, size=40),
    'batch_id': np.random.choice(batch_ids, size=40, replace=False),
    'ordered_quantity_mt': np.random.randint(10, 50, size=40),
    'order_status': np.random.choice(['Shipped', 'Pending Fulfillment', 'Delayed'], size=40, p=[0.8, 0.15, 0.05])
})

# Output all 6 tables as standard CSV seeds in your data folder
df_growers.to_csv(os.path.join(data_dir, "grower_suppliers.csv"), index=False)
df_batches.to_csv(os.path.join(data_dir, "seed_batches.csv"), index=False)
df_process.to_csv(os.path.join(data_dir, "processing_logs.csv"), index=False)
df_valuations.to_csv(os.path.join(data_dir, "inventory_valuations.csv"), index=False)
df_retailers.to_csv(os.path.join(data_dir, "retail_partners.csv"), index=False)
df_orders.to_csv(os.path.join(data_dir, "retail_orders.csv"), index=False)

print("🎯 Success! 6 local relational CSV files are built and ready in your data directory.")
