from core.operator import Operator


class Operation:
    operands = []
    operator = None

    def __init__(self, operands, operator: Operator) -> None:
        self.operands = operands
        self.operator = operator

    def __str__(self) -> str:
        left, right = self.operands
        return f"{str(left)} {self.operator} {str(right)}"

