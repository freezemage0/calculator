from core.operation import Operation


class Processor:
    operator_map = None
    parser = None

    def __init__(self, parser, operator_map):
        self.parser = parser
        self.operator_map = operator_map

    def process(self, expressions):
        self.parser.result = None
        self.parser.parse(expressions)
        result = self.parser.result
        return result

    def calculate(self, operation):
        left, right = operation.operands

        if isinstance(left, Operation):
            left = self.calculate(left)
        if isinstance(right, Operation):
            right = self.calculate(right)

        return operation.operator.action(left, right)

    @staticmethod
    def sum(left, right):
        return left + right

    @staticmethod
    def subtract(left, right):
        return left - right

    @staticmethod
    def multiply(left, right):
        return left * right

    @staticmethod
    def divide(left, right):
        if right == 0:
            raise ZeroDivisionError

        return left / right
