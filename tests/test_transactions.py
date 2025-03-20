import pytest
from app.transactions import process_transaction

def test_valid_transaction():
    data = {"payer": "user1", "payee": "user2", "amount": 100}
    response = process_transaction(data)
    assert response["status"] == "success"

def test_missing_field():
    data = {"payer": "user1", "amount": 100}
    response = process_transaction(data)
    assert response["status"] == "error"

