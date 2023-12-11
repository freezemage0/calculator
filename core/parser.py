import json
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
            expression = expression.replace(result.group(0), pointer)
            result = result.re.search(expression)

        groups = self.operators.group_by_priority()
        for group in groups.values():
            definitions = "\\".join(map(lambda op: op.definition, group))

            pattern = fr'(?P<left>-?\d*\.?\d+)\s?(?P<operator>[\{definitions}])\s?(?P<right>-?\d*\.?\d+)'
            regex = re.compile(pattern)
            result = regex.search(expression)

            while result:
                left_operand = result.group('left')
                right_operand = result.group('right')

                if left_operand in Parser.variables:
                    left_operand = Parser.variables[left_operand]
                else:
                    left_operand = float(left_operand)

                if right_operand in Parser.variables:
                    right_operand = Parser.variables[right_operand]
                else:
                    right_operand = float(right_operand)

                item = self.operators.find_by_definition(result.group('operator'))
                o = operation.Operation([left_operand, right_operand], item)
                name = Parser.generate_var_name()

                Parser.variables[name] = o
                self.result = o

                expression = re.sub(result.re, name, expression, 1)
                result = regex.search(expression)

        if expression not in Parser.variables:
            # In the end, expression will be shortened to one replacement. This one replacement is the whole operation.
            self.parse(expression)

        return self.result

    @staticmethod
    def get_var_name() -> string:
        return f"parsed{Parser.identifier}"

    @staticmethod
    def generate_var_name() -> string:
        Parser.identifier += 1
        return Parser.get_var_name()
