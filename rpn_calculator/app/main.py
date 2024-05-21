from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI()

stacks = {}


def infix_to_postfix(expression: str) -> List[str]:
    priorities = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    operators = []

    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()

    for token in tokens:
        if token.isnumeric() or '.' in token:
            output.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()
        else:
            while (operators and operators[-1] in priorities and
                   priorities[operators[-1]] >= priorities[token]):
                output.append(operators.pop())
            operators.append(token)

    while operators:
        output.append(operators.pop())

    return output

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

@app.post("/rpn/calculate/{stack_id}")
def calculate_complex_expression(stack_id: str, expression: str):
    if stack_id not in stacks:
        raise HTTPException(status_code=404, detail="Stack pas trouvé")
    
    stack = stacks[stack_id]
    #tokens = expression.split()
    postfix_expression = infix_to_postfix(expression)

    #for token in tokens:
    for token in postfix_expression:
        if token in "+-*/":
            if len(stack) < 2:
                raise HTTPException(status_code=400, detail="Pas assez d'élements dans la pile")
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                if b == 0:
                    raise HTTPException(status_code=400, detail="La division par zéro n'est pas autorisé")
                result = a / b
            stack.append(result)
        else:
            try:
                stack.append(float(token))
            except ValueError:
                raise HTTPException(status_code=400, detail=f"Invalid token: {token}")

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

