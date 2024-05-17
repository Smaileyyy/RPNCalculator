from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI()

stacks = {}

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur RPN Calculator API, Consultez /docs pour la documentation."}


@app.get("/rpn/op")
def list_operands():
    return ["+", "-", "*", "/"]

@app.post("/rpn/op/{op}/stack/{stack_id}")
def apply_operand(op: str, stack_id: str):
    if stack_id not in stacks:
        raise HTTPException(status_code=404, detail="Stack pas trouvé")
    stack = stacks[stack_id]
    if len(stack) < 2:
        raise HTTPException(status_code=400, detail="Pas assez d'élements dans la pile")
    b = stack.pop()
    a = stack.pop()
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        if b == 0:
            raise HTTPException(status_code=400, detail="La division par zéro n'est pas autorisé")
        result = a / b
    else:
        raise HTTPException(status_code=400, detail="Opération invalide")
    stack.append(result)
    return {"stack": stack}

@app.post("/rpn/stack")
def create_stack():
    stack_id = str(len(stacks) + 1)
    stacks[stack_id] = []
    return {"stack_id": stack_id}

@app.get("/rpn/stack")
def list_stacks():
    return {"stacks": list(stacks.keys())}

@app.delete("/rpn/stack/{stack_id}")
def delete_stack(stack_id: str):
    if stack_id in stacks:
        del stacks[stack_id]
        return {"detail": "Stack supprimé"}
    else:
        raise HTTPException(status_code=404, detail="Stack pas trouvé")

@app.post("/rpn/stack/{stack_id}")
def push_value(stack_id: str, value: float):
    if stack_id not in stacks:
        raise HTTPException(status_code=404, detail="Stack pas trouvé")
    stacks[stack_id].append(value)
    return {"stack": stacks[stack_id]}

@app.get("/rpn/stack/{stack_id}")
def get_stack(stack_id: str):
    if stack_id not in stacks:
        raise HTTPException(status_code=404, detail="Stack pas trouvé")
    return {"stack": stacks[stack_id]}
