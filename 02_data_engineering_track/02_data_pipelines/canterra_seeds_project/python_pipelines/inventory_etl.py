import pandas as pd
import os
from sqlalchemy import create_engine

def run_agribusiness_etl():
    print("🌾 Initiating CANTERRA SEEDS Master SIPOC + ERP Cloud Data Pipeline...")
    
    # Define paths dynamically matching your architecture
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")
    
    # 1. EXTRACT: Gather all 8 relational datasets (including new ERP documents)
    files = {
        'grower_suppliers': 'grower_suppliers.csv',
        'seed_batches': 'seed_batches.csv',
        'processing_logs': 'processing_logs.csv',
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
            print(f"❌ Error: Required core file missing: {file_path}")
            return
        dfs[table_name] = pd.read_csv(file_path)

    # 2. TRANSFORM LAYER: Compile advanced analytical view locally
    print("📊 Compiling warehouse analytics view...")
    try:
        merged_df = pd.merge(dfs['seed_batches'], dfs['processing_logs'], on="batch_id")
        merged_df = pd.merge(merged_df, dfs['inventory_valuations'], on="batch_id")
        
        merged_df["total_value_cad"] = round(merged_df["quantity_metric_tons"] * merged_df["cost_per_metric_ton"], 2)
        
        def flag_risk_profile(row):
            if row["moisture_percentage"] > 14.5 and row["stock_status"] == "In-Warehouse":
                return "CRITICAL_AERATION_REQUIRED"
            elif row["quantity_metric_tons"] != row["physical_audit_quantity_mt"]:
                return "AUDIT_QUANTITY_VARIANCE"
            return "OPERATIONAL_NORMAL"
            
        merged_df["operational_alert_level"] = merged_df.apply(flag_risk_profile, axis=1)
        
        analytics_path = os.path.join(data_dir, "cleaned_warehouse_analytics.csv")
        merged_df.to_csv(analytics_path, index=False)
        
        # Append calculated view to cloud streaming pool
        dfs['warehouse_analytics'] = merged_df
        print("   ✅ Local analytics view appended successfully.")
    except Exception as trans_error:
        print(f"⚠️ Calculation transformation note: {trans_error}")

    # 3. LOAD INFRASTRUCTURE: Stream all 9 distinct tables directly to Render
    db_user = "canterra_admin"
    db_pass = "fDOH0m1yRmvtYCvzUKxt4vGUGjRZrV9e"
    db_host = "dpg-dbaacmlg1s2s73bcimh0-a.oregon-postgres.render.com"
    db_name = "canterra_seeds_db"
    
    try:
        RENDER_CLOUD_URL = f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}/{db_name}"
        engine = create_engine(RENDER_CLOUD_URL)
        
        print("🌐 Streaming datasets over web sockets to Render Cloud...")
        for table_name, dataframe in dfs.items():
            dataframe.to_sql(table_name, engine, if_exists='replace', index=False)
            print(f"   🚀 Loaded [public.{table_name}] table into cloud database.")
            
        print("🏁 Master ETL Execution Complete! Complete ecosystem is live.")
    except Exception as e:
        print(f"❌ Cloud connection pipeline failure: {e}")

if __name__ == "__main__":
    run_agribusiness_etl()
