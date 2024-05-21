from fastapi.testclient import TestClient
from .main import app, stacks
from fastapi import HTTPException

client = TestClient(app)

def test_list_operands():
    response = client.get("/rpn/op")
    assert response.status_code == 200
    assert response.json() == ["+", "-", "*", "/"]

def test_apply_operand_add():
    stack_id = "test_stack"
    stacks[stack_id] = [10, 5]

    response = client.post(f"/rpn/op/+/stack/{stack_id}")
    assert response.status_code == 200
    assert response.json() == {"stack": [15]}

def test_another_operand():
    stack_id = "test_stack"
    stacks[stack_id] = [10, 5]

    response = client.post(f"/rpn/op/%/stack/{stack_id}")
    assert response.status_code == 400
    assert response.json() == {"detail": "Opération invalide"}


def test_create_stack():
    response = client.post("/rpn/stack")
    assert response.status_code == 200
    assert "stack_id" in response.json()
    
def test_invalid_stack():
    response = client.get("/rpn/stack/invalid_stack_id")
    assert response.status_code == 404
    assert response.json() == {"detail": "Stack pas trouvé"}