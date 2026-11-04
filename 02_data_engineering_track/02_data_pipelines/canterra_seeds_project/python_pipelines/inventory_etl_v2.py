import os
import pandas as pd
from sqlalchemy import create_engine

def run_production_render_pipeline():
    print("🚀 Initializing Live Render.com PostgreSQL Cloud Ingestion Pipeline...")
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")
    
    # Establish direct path references
    targets = {
        'retail_partners_v2': 'retail_partners_v2.csv',
        'financial_ledger_v2': 'financial_ledger_v2.csv',
        'seed_batches_v2': 'seed_batches_v2.csv',
        'quality_inspections_v2': 'quality_inspections_v2.csv',
        'processing_logs_v2': 'processing_logs_v2.csv',
        'erp_bills_of_lading_v2': 'erp_bills_of_lading_v2.csv'
    }
    
    # Securely point engine to your active cloud cluster URL string on Render
    db_user = "canterra_admin"
    db_pass = "fDOH0m1yRmvtYCvzUKxt4vGUGjRZrV9e"
    db_host = "dpg-dbaacmlg1s2s73bcimh0-a.oregon-postgres.render.com"
    db_name = "canterra_seeds_db"
    
    try:
        RENDER_CLOUD_URL = f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}/{db_name}"
        engine = create_engine(RENDER_CLOUD_URL)
    
        for table, file_name in targets.items():
            path = os.path.join(data_dir, file_name)
            if os.path.exists(path):
                df = pd.read_csv(path)
                # Push to the database layer, replacing existing structures smoothly
                df.to_sql(table, engine, if_exists='replace', index=False)
                print(f" -> Live Stream Verified: {table}")
            else:
                print(f" ❌ Missing Source Reference: {file_name}")
    except Exception as e:
        print(f"❌ Pipeline failed: {e}")

if __name__ == '__main__':
    run_production_render_pipeline()
