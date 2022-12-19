class Operator:
    def __init__(self, priority, definition, action):
        self.definition = definition
        self.priority = priority
        self.action = action

    def __str__(self):
        return self.definition


class OperatorMap:
    def __init__(self, operators: list):
        self.operators = operators

    def list_by_priority(self):
        return sorted(self.operators, key=lambda operator: operator.priority)

    def group_by_priority(self) -> dict:
        prioritized = {}
        for operator in self.operators:
            if operator.priority not in prioritized:
                prioritized[operator.priority] = []
            prioritized[operator.priority].append(operator)

        return prioritized

    def find_by_definition(self, definition):
        for operator in self.operators:
            if operator.definition == definition:
                return operator

        return None
