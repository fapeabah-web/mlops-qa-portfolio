import pandas as pd
import numpy as np
import os
from datetime import datetime

# Set up paths matching your directory structure
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(base_dir, "data")

print("📦 Simulating Generations ERP Transactional Document Outputs...")

# Read your existing live pipeline data
analytics_path = os.path.join(data_dir, "cleaned_warehouse_analytics.csv")
if not os.path.exists(analytics_path):
    print("❌ Error: Cleaned warehouse data missing. Run inventory_etl.py first.")
    exit()

df = pd.read_csv(analytics_path)

# 1. Generate Automated Inbound Scale Tickets (Suppliers -> Inputs)
scale_tickets = pd.DataFrame({
    'scale_ticket_id': [f"ST-2026-{i:03d}" for i in range(1, len(df)+1)],
    'batch_id': df['batch_id'],
    'grower_id': df['grower_id'],
    'gross_weight_mt': df['quantity_metric_tons'] + 15.2, # Simulating truck weight
    'tare_weight_mt': 15.2,
    'net_weight_mt': df['quantity_metric_tons'],
    'moisture_pct': df['moisture_percentage'],
    'intake_status': df['operational_alert_level']
})

# 2. Generate Outbound Bills of Lading (Outputs -> Customers)
bol_documents = pd.DataFrame({
    'bill_of_lading_id': [f"BOL-CAN-{i:03d}" for i in range(1, len(df)+1)],
    'batch_id': df['batch_id'],
    'certified_tag_id': df['certified_seed_tag_id'],
    'carrier_name': np.random.choice(['Bison Transport', 'Mullen Group', 'CP Rail', 'Gardewine'], len(df)),
    'shipping_facility': df['processing_facility'],
    'delivery_status': df['stock_status']
})

# Save documents cleanly to your local data folder for Excel / Power BI ingestion
scale_tickets.to_csv(os.path.join(data_dir, "erp_scale_tickets.csv"), index=False)
bol_documents.to_csv(os.path.join(data_dir, "erp_bills_of_lading.csv"), index=False)

print("🎯 ERP Simulation Complete! 'erp_scale_tickets.csv' and 'erp_bills_of_lading.csv' are live.")
