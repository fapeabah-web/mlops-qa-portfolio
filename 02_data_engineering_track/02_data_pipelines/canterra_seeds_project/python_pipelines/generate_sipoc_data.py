import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

np.random.seed(42)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(base_dir, "data")
os.makedirs(data_dir, exist_ok=True)

print("🌾 Building 5-Year Master CANTERRA SEEDS SIPOC Ecosystem (2021-2026)...")

total_records = 520  # Over 100 records per lot scenario
years = [2021, 2022, 2023, 2024, 2025, 2026]
crops = ['Canola', 'Pulses/Peas', 'Pedigreed Wheat', 'Barley', 'Oats']

# --- 1. SUPPLIERS STAGE ---
grower_ids = [f"GRW-{i:03d}" for i in range(1, 16)]
growers = ["Prairie Oats Farm", "Red River Seed Co", "Brandon Grain Growers", "Interlake Pedigreed Farms", "Pembina Valley Seeds"] * 3
regions = ["Manitoba-South", "Manitoba-West", "Saskatchewan-East", "Alberta-South", "Manitoba-Interlake"] * 3
df_growers = pd.DataFrame({
    'grower_id': grower_ids,
    'grower_name': growers,
    'region': regions,
    'contract_year': 2026
})

# --- 2. INPUTS STAGE ---
batch_ids = [f"LOT-{np.random.choice(years)}-{i:03d}" for i in range(1, total_records + 1)]
batch_ids.sort()

crop_choices = np.random.choice(crops, size=total_records, p=[0.3, 0.25, 0.25, 0.1, 0.1])
assigned_growers = np.random.choice(grower_ids, size=total_records)

received_dates = []
for bid in batch_ids:
    year = int(bid.split("-")[1])
    if np.random.rand() < 0.70:  # Harvest rush seasonality (August - October)
        month = np.random.randint(8, 11)
    else:
        month = np.random.choice([1, 2, 3, 4, 5, 6, 7, 11, 12])
    day = np.random.randint(1, 28)
    received_dates.append(datetime(year, month, day))

# Volume explosion logic: 120MT per crop in 2024 -> 360MT in 2025
quantities_mt = []
for bid in batch_ids:
    year = int(bid.split("-")[1])
    if year <= 2024:
        quantities_mt.append(np.round(np.random.uniform(20, 30), 2))
    elif year == 2025:
        quantities_mt.append(np.round(np.random.uniform(65, 85), 2))
    else:
        quantities_mt.append(np.round(np.random.uniform(55, 75), 2))

df_batches = pd.DataFrame({
    'batch_id': batch_ids,
    'grower_id': assigned_growers,
    'crop_type': crop_choices,
    'received_date': received_dates,
    'moisture_percentage': np.round(np.random.uniform(11.0, 16.5, size=total_records), 1)
})

# --- 3. PROCESS STAGE (Warehouse, Conditioning & Chemical Treatments) ---
facilities = ['Winnipeg Corporate HQ', 'Manitoba Contract Growers', 'Saskatchewan Retail Networks', 'Alberta Co-op Distribution']
contaminants = ['Chaff', 'Weeds', 'Undersized Seeds', 'Stones', 'Brittles and Plastics', 'Metal Parts', 'None']
stock_statuses = ['In-Warehouse', 'In-Transit', 'Allocated']

df_process = pd.DataFrame({
    'batch_id': batch_ids,
    'processing_facility': np.random.choice(facilities, size=total_records),
    'air_screen_separation_status': np.random.choice(['Pass', 'Re-clean Required'], size=total_records, p=[0.92, 0.08]),
    'gravity_table_efficiency_pct': np.round(np.random.uniform(94.5, 99.9, size=total_records), 2),
    'optical_color_sorter_passed': np.random.choice(['Yes', 'No'], size=total_records, p=[0.95, 0.05]),
    'detected_foreign_material': np.random.choice(contaminants, size=total_records, p=[0.12, 0.05, 0.05, 0.03, 0.02, 0.01, 0.72]),
    'quantity_metric_tons': quantities_mt,
    'physical_audit_quantity_mt': quantities_mt,
    'stock_status': np.random.choice(stock_statuses, size=total_records, p=[0.70, 0.20, 0.10])
})
# Introduce deliberate variances for audit analysis
df_process.loc[0:15, 'physical_audit_quantity_mt'] = df_process.loc[0:15, 'quantity_metric_tons'] - 1.5

applied_treatments = []
treatment_used = []
treatment_purchased = []

for idx, row in df_batches.iterrows():
    crop = row['crop_type']
    qty = df_process.loc[idx, 'quantity_metric_tons']
    if crop == 'Canola':
        agent, ratio = "Neonicotinoid + Broad-Spectrum Fungicide", 2.5
    elif crop == 'Pulses/Peas':
        agent, ratio = "Trilex AL + Liquid Rhizobium Inoculant", 3.0
    else:
        agent, ratio = "Teraxxa F4 Cereal Treatment", 2.0
    
    applied_treatments.append(agent)
    used = np.round(qty * ratio, 2)
    purchased = np.round(used * 1.10, 2) if np.random.rand() < 0.10 else used
    treatment_used.append(used)
    treatment_purchased.append(purchased)

df_chemical = pd.DataFrame({
    'batch_id': batch_ids,
    'applied_treatment_regimen': applied_treatments,
    'agent_unit_price_cad': np.random.choice([25.00, 48.00, 72.00, 95.00], size=total_records),
    'treatment_quantity_purchased_liters': treatment_purchased,
    'treatment_quantity_used_liters': treatment_used
})
df_chemical['warehouse_remaining_storage_liters'] = np.round(df_chemical['treatment_quantity_purchased_liters'] - df_chemical['treatment_quantity_used_liters'], 2)

# --- 4. OUTPUTS STAGE (Valuations & Inventory Carry-Forward) ---
costs_per_mt = np.round(np.random.uniform(450, 1350, size=total_records), 2)
carry_forward = []
next_year_valuation = []

for i in range(total_records):
    status = df_process.loc[i, 'stock_status']
    qty = df_process.loc[i, 'quantity_metric_tons']
    cost = costs_per_mt[i]
    
    # Inventory Balance Carry-Forward Logic
    if status == 'In-Warehouse':
        carry_forward.append('Yes - Carry Forward to Next Fiscal Year')
        next_year_valuation.append(np.round(qty * cost, 2))
    else:
        carry_forward.append('No - Shipped/In-Transit')
        next_year_valuation.append(0.00)

df_valuations = pd.DataFrame({
    'batch_id': batch_ids,
    'cost_per_metric_ton': costs_per_mt,
    'certified_seed_tag_id': [f"TAG-CA-{i:03d}" for i in range(1, total_records + 1)],
    'inventory_carry_forward_flag': carry_forward,
    'warehouse_carry_forward_valuation_cad': next_year_valuation
})

# --- 5. CUSTOMERS STAGE (Retail Partners & Orders) ---
retail_ids = [f"RTL-{i:03d}" for i in range(1, 11)]
retails = ["Nutrien Ag Solutions", "Richardson Pioneer", "Federated Co-operatives Ltd", "Cargill Canada"] * 2 + ["Independent Dealer A", "Independent Dealer B"]
df_partners = pd.DataFrame({
    'retail_id': retail_ids,
    'retail_partner_name': retails,
    'destination_province': np.random.choice(['MB', 'SK', 'AB'], size=10)
})

# Filter out batches that are In-Warehouse to create realistic customer orders
shipped_batches = [batch_ids[i] for i in range(total_records) if carry_forward[i] == 'No - Shipped/In-Transit']
num_orders = min(400, len(shipped_batches))

df_orders = pd.DataFrame({
    'order_id': [f"ORD-2026-{i:03d}" for i in range(1, num_orders + 1)],
    'retail_id': np.random.choice(retail_ids, size=num_orders),
    'batch_id': shipped_batches[:num_orders],
    'ordered_quantity_mt': np.random.randint(10, 45, size=num_orders),
    'order_status': np.random.choice(['Shipped', 'Pending Fulfillment', 'Delayed'], size=num_orders, p=[0.85, 0.10, 0.05])
})

# --- 6. ERP DOCUMENTS ---
df_scale_tickets = pd.DataFrame({
    'scale_ticket_id': [f"ST-5YR-{i:03d}" for i in range(1, total_records + 1)],
    'batch_id': batch_ids,
    'gross_weight_mt': np.round(df_process['quantity_metric_tons'] + 15.10, 2),
    'tare_weight_mt': 15.10,
    'net_intake_weight_mt': df_process['quantity_metric_tons']
})

df_bol = pd.DataFrame({
    'bill_of_lading_id': [f"BOL-5YR-{i:03d}" for i in range(1, num_orders + 1)],
    'batch_id': shipped_batches[:num_orders],
    'carrier_name': np.random.choice(['Bison Transport', 'Mullen Group', 'CP Rail', 'Gardewine Freight'], size=num_orders),
    'freight_cost_cad': np.round(np.random.uniform(1100, 4500, size=num_orders), 2)
})

# Save EVERY table to files
df_growers.to_csv(os.path.join(data_dir, "grower_suppliers.csv"), index=False)
df_batches.to_csv(os.path.join(data_dir, "seed_batches.csv"), index=False)
df_process.to_csv(os.path.join(data_dir, "processing_logs.csv"), index=False)
df_chemical.to_csv(os.path.join(data_dir, "chemical_treatments.csv"), index=False)
df_valuations.to_csv(os.path.join(data_dir, "inventory_valuations.csv"), index=False)
df_partners.to_csv(os.path.join(data_dir, "retail_partners.csv"), index=False)
df_orders.to_csv(os.path.join(data_dir, "retail_orders.csv"), index=False)
df_scale_tickets.to_csv(os.path.join(data_dir, "erp_scale_tickets.csv"), index=False)
df_bol.to_csv(os.path.join(data_dir, "erp_bills_of_lading.csv"), index=False)

print("🏁 Master SIPOC + ERP Dataset generated completely with warehouse carry-over details!")
