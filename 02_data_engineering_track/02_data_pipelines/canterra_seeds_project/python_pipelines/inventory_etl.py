import pandas as pd
import os

def run_agribusiness_etl():
    print("🌾 Starting CANTERRA SEEDS Inventory ETL Pipeline...")
    
    # Define file paths dynamically
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    batches_path = os.path.join(base_dir, "data", "seed_batches.csv")
    valuations_path = os.path.join(base_dir, "data", "inventory_valuations.csv")
    
    # 1. EXTRACT: Ingest raw operational CSV files
    if not os.path.exists(batches_path) or not os.path.exists(valuations_path):
        print("❌ Error: Raw data files missing. Check your /data folder.")
        return
        
    df_batches = pd.read_csv(batches_path)
    df_valuations = pd.read_csv(valuations_path)
    
    # 2. TRANSFORM: Merge datasets and execute analytical calculations
    # Combine tables on unique Batch ID
    merged_df = pd.merge(df_batches, df_valuations, on="batch_id")
    
    # Calculate absolute financial value of stock on hand
    merged_df["total_value_cad"] = round(merged_df["quantity_metric_tons"] * merged_df["cost_per_metric_ton"], 2)
    
    # Multi-variable logic: Flag critical status if moisture > 14% AND stock is warehouse-bound
    def flag_risk_profile(row):
        if row["moisture_percentage"] > 14.0 and row["stock_status"] == "In-Warehouse":
            return "CRITICAL_SPOILAGE_RISK"
        elif row["quantity_metric_tons"] != row["physical_audit_quantity_mt"]:
            return "AUDIT_QUANTITY_VARIANCE"
        return "OPERATIONAL_NORMAL"
        
    merged_df["operational_alert_level"] = merged_df.apply(flag_risk_profile, axis=1)
    
    # 3. LOAD: Output a highly optimized repository for SQL/Power BI ingestion
    output_path = os.path.join(base_dir, "data", "cleaned_warehouse_analytics.csv")
    merged_df.to_csv(output_path, index=False)
    
    print(f"✅ ETL Execution Successful! Pipeline dataset saved to: {output_path}")
    print(merged_df[["batch_id", "crop_type", "operational_alert_level"]].head())

if __name__ == "__main__":
    run_agribusiness_etl()
