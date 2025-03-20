def process_transaction(data):
    required_fields = ["payer", "payee", "amount"]
    
    for field in required_fields:
        if field not in data:
            return {"status": "error", "message": f"Missing {field}"}
    
    return {"status": "success", "transaction_id": "txn_12345"}

