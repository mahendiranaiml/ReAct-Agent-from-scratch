import json

def calculator(input_text: str) -> str:
    data = json.loads(input_text)

    a = float(data["a"])
    b = float(data["b"])
    op = data.get("operation")

    def addition(a, b):
        return str(a + b)

    def subtraction(a, b):
        return str(a - b)

    def multiplication(a, b):
        return str(a * b)

    def division(a, b):
        return str(a / b) if b != 0 else "Error: division by zero"

    if op == "add":
        return addition(a, b)
    elif op == "subtract":
        return subtraction(a, b)
    elif op == "multiply":
        return multiplication(a, b)
    elif op == "divide":
        return division(a, b)

    return "Invalid operation"