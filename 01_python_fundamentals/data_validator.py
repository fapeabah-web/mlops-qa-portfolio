# A simple Object-Oriented QA system to validate data records
class DataRecordValidator:
    def __init__(self, record_id, product_name, quality_score):
        self.record_id = record_id
        self.product_name = product_name
        self.quality_score = quality_score

    def run_compliance_check(self):
        print(f"🔬 Auditing Record #{self.record_id} for product: {self.product_name}...")
        
        # QA Logic Gate: If quality score drops below 75, flag as defect
        if self.quality_score < 75:
            return "❌ REJECTED: Product fails structural quality thresholds."
        else:
            return "✅ PASSED: Product meets compliance standard metrics."

# --- Testing our QA Architecture with Data ---
# Test Case 1: High Quality Batch
batch_01 = DataRecordValidator(record_id=101, product_name="Premium Grain Batch A", quality_score=92)
print(batch_01.run_compliance_check())

print("-" * 50)

# Test Case 2: Low Quality Batch
batch_02 = DataRecordValidator(record_id=102, product_name="Substandard Batch B", quality_score=64)
print(batch_02.run_compliance_check())