OPERATORS = ['+', '-', '*', '/', '(', ')']


def validate_expression_type(inp):
    inp = inp.strip()
    print(inp)
    if inp != '1' and inp != '2':
        print("Please enter a valid code... ")
        return 0
    else:
        return int(inp)


def evaluate_expression(expression, expression_type):
    processing_stack = []
    if expression_type == 1:
        expression = convert_to_postfix(expression)

    expression = expression.strip()
    for char in expression:
        if char in OPERATORS:  # operators should only be {+, -, *, /} at this point
            x = processing_stack.pop()
            y = processing_stack.pop()
            if char == '+':
                processing_stack.append(y+x)
            if char == '-':
                processing_stack.append(y-x)
            if char == '*':
                processing_stack.append(y*x)
            if char == '/':
                processing_stack.append(y/x)
        else:
            processing_stack.append(int(char))
    print(processing_stack.pop())
    return True


def convert_to_postfix(expression):
    operator_stack = []
    out = ""
    for char in expression:
        if char in OPERATORS:
            if char == ')':
                while operator_stack[-1] != '(':
                    out += operator_stack.pop()
                operator_stack.pop()  # remove the open parenthesis
            else:
                operator_stack.append(char)
        else:
            out += char

    while operator_stack:  # empty sequences are false
        popped = operator_stack.pop()
        if popped != '(' and popped != ')':
            out += popped

    return out

if __name__ == '__main__':

    expressionType = 0
    message1 = """
    \n\n\tcode | type
    -----|---------------------------------------------
       1 | infix  (must be fully parenthesized)
       2 | postfix
    """
    print(message1)
    while expressionType == 0:
        inputExpressionType = input("Enter expression type: ")
        expressionType = validate_expression_type(inputExpressionType)

    success = False
    while not success:
        expression = input("Please enter expression: ")
        success = evaluate_expression(expression, expressionType)

