from core import parser, operator, processor
from core.processor import Processor

operator_map = operator.OperatorMap([
    operator.Operator(1, '*', Processor.multiply),
    operator.Operator(1, '/', Processor.divide),
    operator.Operator(2, '+', Processor.sum),
    operator.Operator(2, '-', Processor.subtract)
])

p = processor.Processor(parser.Parser(operator_map))

running = True
while running:
    print("Input expression [press enter to quit]: ")
    expression = input()
    if len(expression) == 0:
        running = False
        continue

    result = p.process(expression)
    if result is None:
        print("Syntax error. Unable to process expression")
        continue

    print(f"{expression} = {p.calculate(result)}")
