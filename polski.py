def to_rpn(expression: str) -> list:
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    result = []
    stack = []

    tokens = tokenize(expression)

    for token in tokens:
        if token.isdigit():
            result.append(int(token))
        elif token in precedence:
            while (stack and stack[-1] != '('
                   and precedence.get(stack[-1], 0) >= precedence[token]):
                result.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()

    while stack:
        result.append(stack.pop())

    return result


def tokenize(expression: str) -> list:
    return expression.replace('(', ' ( ').replace(')', ' ) ').split()


def evaluate_rpn(rpn: list) -> int:
    stack = []
    for token in rpn:
        if isinstance(token, int):
            stack.append(token)
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a-b)
                #stack.append(a // b)
    return stack[0]


def calculate(expression: str) -> int:
    rpn = to_rpn(expression)
    return evaluate_rpn(rpn)


if __name__ == "__main__":
    try:
        inp = input()
        rpnn = to_rpn(inp)
        pupa = ' '.join([str(i) for i in rpnn])
        print(f'RPN: {pupa}')
        print(f'Result: {evaluate_rpn(rpnn)}')
    except Exception as e:
        print(f"Error {e}")
