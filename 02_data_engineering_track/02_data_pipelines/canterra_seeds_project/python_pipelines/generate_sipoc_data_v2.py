import pandas as pd
import numpy as np
import os
from datetime import datetime

np.random.seed(42)

# Directory configurations targeting your active VS Code architecture
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(base_dir, "data")
os.makedirs(data_dir, exist_ok=True)

# 1. ENHANCED AGRIBUSINESS RETAILER REGISTRY
major_coops = [
    'United Farmers of Alberta (UFA)', 'Nutrien Ag Solutions', 
    'Richardson Pioneer', 'Sollio Agriculture', 'Pioneer Co-op'
]

local_branches = [
    'Ag Grow Consulting', 'Agritech Team-Hafford, SK', 'AgroPlus Lethbridge', 'AgroPlus-Medicine Hat',
    'Benato Ag', 'Core Ag-Radville', 'Core Ag-Lethbridge', 'Cornerstone Seeds-Moosomin, SK',
    'Cornerstone Seeds-Welwyn, SK', 'Dawson Creek Coop-Rolla, BC', 'DSAG', 'Elevation Ag',
    'Fedoruk Seeds', 'GrowPlan Fertilizer', 'Hawk\'s Agro-Swift Current, SK', 'Hawkview Ag-Fairview, AB',
    'Hetland Seeds', 'Horizon Fertilizer-Humboldt, SK', 'ICI Taber', 'Kemper Seeds',
    'Kemper Seeds-Humboldt, SK', 'Lake Country Coop-Knistino, SK', 'Lake Country Coop-Prince Albert, SK',
    'Lake Country Coop-Shelbrook, SK', 'LD Seeds', 'Max Consulting', 'McEwen\'s Fuels & Fertilizers-Ft. Sask, AB',
    'Merlot Ag-Girouxville, AB', 'Neerlandia Coop Agro-Neerlandia, AB', 'Nielsen Seeds-Hargrave, MB',
    'P&H-Dugald, MB', 'P&H-Wairwright, MB', 'P&H-Hanover', 'Peace Grain Advantage', 'Penwest Seeds',
    'Penwest Seeds-Three Hill, AB', 'Pioneer Coop-Kyle, SK', 'Pitura Seeds-Domain, MB', 'Ponoka Fertilizer',
    'Prairie Giant Crop Supply', 'ProSoils-Carraganna, SK', 'Simplot Grower Solutions-Cardstone,AB',
    'Simplot Grower Solutions-Chin, AB', 'Simplot Grower Solutions-Kindersley, SK', 'Simplot Grower Solutions-Meadowlake, SK',
    'Simplot Grower Solutions-Medstead, SK', 'Simplot Grower Solutions-Meota, SK', 'Simplot Grower Solutions-Rosetown, SK',
    'Simplot Grower Solutions-Spiritwood, SK', 'South Country Coop-Cypress', 'St. Isidore Coop',
    'St. Isidore Coop-Fahler', 'Synergy Seeds-Souris, MB', 'SynergyAG-Balcarres, SK', 'SynergyAG-Govan, SK',
    'SynergyAG-Yorkton, SK', 'Top Notch Filmore', 'UFA-Athabasca', 'UFA-Camrose', 'UFA-Grande Prairie',
    'UFA-Provost', 'UFA-St. Paul', 'UFA Strathmore', 'UFA Two Hills', 'UFA-Vermillion', 'UFA-Vulcan',
    'Verkie\'s Agro-Cut Knife, SK', 'Westgreen Agronomy', 'Wetaskiwin Coop Agro-Wetaskiwin, AB',
    'Whispering Pine Farms-Sedley, SK', 'Winny Seeds', 'Wyle Seeds'
]

independent_growers = [
    'Stamp Seeds (Enchant, Alberta)', 'Sissons Farms Ltd. (Portage La Prairie, Manitoba)',
    'Avondale Seed Farm (Reston, Manitoba)', 'Airth Farms Ltd. (Brooks, Alberta)',
    'True Seeds Ltd. (Redwater, Alberta)', 'Carl\'s Ag Ventures Ltd. (Hays, Alberta)',
    'Corns Seeds (Grassy Lake, Alberta)', 'Jonk Seeds (Westlock, Alberta)', 'Southline Ag Services (Climax, Saskatchewan)'
]

# Build Comprehensive Customer Segment Framework
retailer_pool = []
for r in major_coops:
    retailer_pool.append({'retailer_name': r, 'segment': 'Major Corporate Distributor'})
for r in local_branches:
    retailer_pool.append({'retailer_name': r, 'segment': 'Localized Cooperative Network'})
for r in independent_growers:
    retailer_pool.append({'retailer_name': r, 'segment': 'Authorized Independent Grower'})

df_retail_registry = pd.DataFrame(retailer_pool)
df_retail_registry['retailer_id'] = [f'RET-{i:03d}' for i in range(1, len(df_retail_registry) + 1)]

# 2. DEFINITIVE SEED VARIETY REGISTRY
crop_registry = {
    'Wheat': [
        'CS Baker', 'CS Breadwinner', 'CDC Evident', 'AAC Weyburn VB', 'CS Recoil', 'CS Garde', 
        'CS Palisade', 'CS Accelerate', 'CS Tracker', 'CS Jake', 'AAC Donlow', 'AAC Cameron VB', 
        'AAC Connery', 'AAC Congress', 'CDC Credence', 'CDC Envy', 'AAC Elie', 'AAC Leroy VB', 
        'AAC Redberry', 'AAC Vortex', 'CDC Precision', 'AAC Ahead VB', 'Fierce VB'
    ],
    'Oats': ['CS Camden', 'CDC Endure', 'Kalio', 'Kyron', 'CDC Morrison', 'Triactor', 'ORe Ruminator', 'AAC Fetch'],
    'Barley': [
        'AAC Connect', 'AB Wrangler', 'Canmore', 'CDC Goldstar', 'CDC Coalition', 'Celebration', 
        'AAC Prairie', 'AAC Lariat', 'AB Maximizer', 'AB Foothills', 'AB Cattleac', 'AS Lafleur'
    ],
    'Pulses': [
        'AAC Carver', 'AAC Beyond', 'CS ProStar', 'CDC 5791', 'CDC 6928 CL', 'CDC 6956 CL', 
        'ND Palomino', 'Windbreaker', 'AAC Aberdeen', 'CDC 5845', 'CDC 7358 CL', 'Rougeaux CL', 
        'CDC Engage', 'CDC 7208'
    ],
    'Specialty': ['CDC Lumio', 'CDC Cibo', 'CDC Calvi', 'CDC Neela', 'AC™ Prairie Thunder', 'AC™ Lightning', 'AB Snowcat', 'TriCal Surge']
}

# 3. GENERATE INTEGRATED TRANSACTIONAL TIMELINE LOGS
financial_profiles = {
    2021: {'rev': 51200000, 'cost': 42150000},
    2022: {'rev': 56443000, 'cost': 46120000},
    2023: {'rev': 49071000, 'cost': 39222000},
    2024: {'rev': 49071300, 'cost': 39222704},
    2025: {'rev': 58110450, 'cost': 45678318},
    2026: {'rev': 63137274, 'cost': 50412822}
}

quarterly_weights = {
    'Q1': {'sales': 0.005, 'cost': 0.05},
    'Q2': {'sales': 0.400, 'cost': 0.35},
    'Q3': {'sales': 0.520, 'cost': 0.45},
    'Q4': {'sales': 0.075, 'cost': 0.15}
}

batches_v2, quality_v2, processing_v2, finance_v2, bol_v2 = [], [], [], [], []
st_counter, bol_counter = 20001, 40001

for year, metrics in financial_profiles.items():
    for q, weights in quarterly_weights.items():
        q_rev = metrics['rev'] * weights['sales']
        q_cost = metrics['cost'] * weights['cost']
        q_profit = q_rev - q_cost
        
        # Capture Quarterly Financial Ledger Record
        finance_v2.append({
            'fiscal_year': year, 'quarter': q, 'allocated_revenue': round(q_rev, 2),
            'allocated_cost': round(q_cost, 2), 'net_profit': round(q_profit, 2)
        })
        
        # Mock transactional execution loops (Ensuring >100 entity records)
        loop_cycles = 8 if year <= 2023 else 18
        for _ in range(loop_cycles):
            crop = np.random.choice(list(crop_registry.keys()))
            variety = np.random.choice(crop_registry[crop])
            retailer = df_retail_registry.sample(1).iloc[0]
            st_id = f'ST-{st_counter}'
            
            net_w = np.random.uniform(18000, 38000)
            clerical_fault = np.random.choice([True, False], p=[0.05, 0.95])
            manual_w = net_w * (np.random.uniform(0.93, 1.07) if clerical_fault else 1.0)
            
            batches_v2.append({
                'scale_ticket_id': st_id, 'fiscal_year': year, 'quarter': q, 'crop_type': crop,
                'seed_variety': variety, 'net_weight_kg': round(net_w, 2), 'manual_entry_kg': round(manual_w, 2)
            })
            
            # Quality Trial Parameter Structuring
            germ = np.random.beta(17, 2) * 100
            moist = np.random.uniform(11.2, 17.8)
            quality_v2.append({
                'scale_ticket_id': st_id, 'germination_pct': round(germ, 1),
                'viability_pct': round(germ + np.random.uniform(0.5, 2.0), 1),
                'moisture_receival_pct': round(moist, 1),
                'moisture_post_pct': round(moist if moist <= 14.5 else moist - np.random.uniform(1.2, 2.8), 1),
                'foreign_material_receival_pct': round(np.random.uniform(1.5, 6.8), 2),
                'foreign_material_post_pct': round(np.random.uniform(0.1, 0.38), 2)
            })
            
            # Input Packaging & Logistics Data
            pkg = '1MT Bulk Tote' if net_w > 26000 else '25kg Paper Bag Valve'
            units = np.ceil(net_w / (1000.0 if '1MT' in pkg else 25.0))
            processing_v2.append({
                'scale_ticket_id': st_id, 'packaging_material_type': pkg, 'packaging_units_count': int(units),
                'treatment_chemical': 'Teraxxa F4' if crop in ['Wheat','Barley','Oats'] else 'Trilex AL + Inoculant'
            })
            
            # Bill of Lading Manifest Integration
            bol_v2.append({
                'bol_number': f'BOL-{bol_counter}', 'scale_ticket_id': st_id, 'retailer_id': retailer['retailer_id'],
                'carrier_name': np.random.choice(['Bison Transport', 'Trimac', 'CP Rail Transload']),
                'freight_terms': 'FOB Origin' if net_w > 26000 else 'FOB Destination', 'backorder_flag': np.random.choice([0, 1], p=[0.92, 0.08])
            })
            
            st_counter += 1
            bol_counter += 1

# Export Clean Relational Datasets
df_retail_registry.to_csv(os.path.join(data_dir, 'retail_partners_v2.csv'), index=False)
pd.DataFrame(finance_v2).to_csv(os.path.join(data_dir, 'financial_ledger_v2.csv'), index=False)
pd.DataFrame(batches_v2).to_csv(os.path.join(data_dir, 'seed_batches_v2.csv'), index=False)
pd.DataFrame(quality_v2).to_csv(os.path.join(data_dir, 'quality_inspections_v2.csv'), index=False)
pd.DataFrame(processing_v2).to_csv(os.path.join(data_dir, 'processing_logs_v2.csv'), index=False)
pd.DataFrame(bol_v2).to_csv(os.path.join(data_dir, 'erp_bills_of_lading_v2.csv'), index=False)

print("🎯 High-fidelity V2 Agribusiness datasets generated successfully.")
