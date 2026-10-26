import pandas as pd
import os
from sqlalchemy import create_engine

def run_agribusiness_etl():
    print("🌾 Running CANTERRA SEEDS Complete SIPOC + ERP Ingestion Engine...")
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")
    
    files = {
        'grower_suppliers': 'grower_suppliers.csv',
        'seed_batches': 'seed_batches.csv',
        'processing_logs': 'processing_logs.csv',
        'chemical_treatments': 'chemical_treatments.csv',
        'inventory_valuations': 'inventory_valuations.csv',
        'retail_partners': 'retail_partners.csv',
        'retail_orders': 'retail_orders.csv',
        'erp_scale_tickets': 'erp_scale_tickets.csv',
        'erp_bills_of_lading': 'erp_bills_of_lading.csv'
    }
    
    dfs = {}
    for table_name, file_name in files.items():
        file_path = os.path.join(data_dir, file_name)
        if not os.path.exists(file_path):
            print(f"❌ Error: Missing table: {file_path}")
            return
        dfs[table_name] = pd.read_csv(file_path)

    # Database Credentials
    db_user = "canterra_admin"
    db_pass = "fDOH0m1yRmvtYCvzUKxt4vGUGjRZrV9e"
    db_host = "dpg-dbaacmlg1s2s73bcimh0-a.oregon-postgres.render.com"
    db_name = "canterra_seeds_db"
    
    try:
        RENDER_CLOUD_URL = f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}/{db_name}"
        engine = create_engine(RENDER_CLOUD_URL)
        
        print("🌐 Streaming full relational grid schemas to Render Cloud...")
        for table_name, dataframe in dfs.items():
            dataframe.to_sql(table_name, engine, if_exists='replace', index=False)
            print(f"   🚀 Successfully loaded table: [public.{table_name}]")
            
        print("🏁 System Overhaul Complete! All data details are securely live.")
    except Exception as e:
        print(f"❌ Connection pipeline failure: {e}")

if __name__ == "__main__":
    run_agribusiness_etl()
