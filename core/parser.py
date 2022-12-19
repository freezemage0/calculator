import re
import string

from core import operator, operation
from core.operator import OperatorMap


class Parser:
    identifier = 0
    variables = {}

    def __init__(self, operators: OperatorMap):
        self.result = None
        self.operators = operators

    def parse(self, expression) -> operation.Operation:
        result = re.search(r"\(([^\(]*?)\)", expression)
        while result is not None:
            parser = Parser(self.operators)

            parser.parse(result.group(1))
            pointer = Parser.get_var_name()

            Parser.variables[pointer] = parser.result
            expression = expression.replace(f"{result.group(0)}", pointer)
            result = result.re.search(expression)

        for item in self.operators.list_by_priority():
            pattern = fr'(?P<left>\w+)\s?(?P<operator>\{item.definition})\s?(?P<right>\w+)'
            result = re.finditer(pattern, expression)

            if result is None:
                continue

            for match in result:
                left_operand = match.group('left')
                right_operand = match.group('right')

                if left_operand in Parser.variables:
                    left_operand = Parser.variables[left_operand]
                else:
                    left_operand = int(left_operand)

                if right_operand in Parser.variables:
                    right_operand = Parser.variables[right_operand]
                else:
                    right_operand = int(right_operand)

                o = operation.Operation([left_operand, right_operand], item)
                name = Parser.generate_var_name()

                Parser.variables[name] = o
                self.result = o

                expression = re.sub(match.re, name, expression, 1)
                self.parse(expression)

        return self.result

    @staticmethod
    def get_var_name() -> string:
        return f"parsed{Parser.identifier}"

    @staticmethod
    def generate_var_name() -> string:
        Parser.identifier += 1
        return Parser.get_var_name()
