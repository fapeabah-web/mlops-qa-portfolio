-- ==============================================================================
-- CASE STUDY: CANTERRA SEEDS CO-ORDINATOR INVENTORY CONTROL PIPELINE
-- Author: Franklin [Last Name], PhD
-- Purpose: Relational extraction layer to audit moisture thresholds, 
--          calculate crop portfolio valuation, and flag physical variances.
-- ==============================================================================

-- ------------------------------------------------------------------------------
-- SCENARIO A: THE HIGH-RISK MOISTURE ALERT MATRIX
-- Operational Goal: Isolate seed lots exceeding safe storage thresholds (>14%) 
--                   to trigger immediate aeration/blending and prevent spoilage.
-- ------------------------------------------------------------------------------
SELECT 
    batch_id,
    crop_type,
    seed_variety,
    processing_facility,
    moisture_percentage,
    quantity_metric_tons
FROM 
    seed_batches
WHERE 
    moisture_percentage > 14.0
ORDER BY 
    moisture_percentage DESC;


-- ------------------------------------------------------------------------------
-- SCENARIO B: TOTAL PORTFOLIO VALUATION BY CROP PORTFOLIO
-- Operational Goal: Compute total volume and absolute commercial dollar values (CAD) 
--                   to support management cost decisions and financial tracking.
-- ------------------------------------------------------------------------------
SELECT 
    b.crop_type,
    SUM(b.quantity_metric_tons) AS total_volume_mt,
    ROUND(SUM(b.quantity_metric_tons * v.cost_per_metric_ton), 2) AS total_inventory_value_cad
FROM 
    seed_batches b
JOIN 
    inventory_valuations v ON b.batch_id = v.batch_id
WHERE 
    v.stock_status = 'In-Warehouse'
GROUP BY 
    b.crop_type
ORDER BY 
    total_inventory_value_cad DESC;


-- ------------------------------------------------------------------------------
-- SCENARIO C: WAREHOUSE AUDIT DISCREPANCY VERIFICATION
-- Operational Goal: Contrast system balances against physical yard audit weights 
--                   to isolate transaction or entry errors across sites.
-- ------------------------------------------------------------------------------
SELECT 
    b.processing_facility,
    b.batch_id,
    b.quantity_metric_tons AS system_quantity_mt,
    v.physical_audit_quantity_mt,
    ROUND((b.quantity_metric_tons - v.physical_audit_quantity_mt), 2) AS variance_mt
FROM 
    seed_batches b
JOIN 
    inventory_valuations v ON b.batch_id = v.batch_id
WHERE 
    (b.quantity_metric_tons - v.physical_audit_quantity_mt) != 0;
