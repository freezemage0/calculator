from core.operation import Operation


class Processor:
    parser = None

    def __init__(self, parser):
        self.parser = parser

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

        res = operation.operator.action(left, right)
        return res

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

    @staticmethod
    def power(left, right):
        return left ** right
