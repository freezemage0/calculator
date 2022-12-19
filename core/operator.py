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
