def calculate(s: str) -> int:
    # Step 1: Tokenize (convert string into numbers/operators list)
    tokens = []
    i = 0
    while i < len(s):
        if s[i] == ' ':
            i += 1
            continue
        if s[i].isdigit():
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            tokens.append(num)
            continue
        else:
            tokens.append(s[i])
        i += 1

    # Step 2: Process * and /
    i = 0
    while i < len(tokens):
        if tokens[i] == "*" or tokens[i] == "/":
            left = tokens[i-1]
            right = tokens[i+1]
            if tokens[i] == "*":
                result = left * right
            else:  # Division truncates toward 0
                result = int(left / right)
            tokens[i-1:i+2] = [result]  # Replace (left,op,right) with result
            i -= 1
        else:
            i += 1

    # Step 3: Process + and -
    i = 0
    while i < len(tokens):
        if tokens[i] == "+" or tokens[i] == "-":
            left = tokens[i-1]
            right = tokens[i+1]
            if tokens[i] == "+":
                result = left + right
            else:
                result = left - right
            tokens[i-1:i+2] = [result]
            i -= 1
        else:
            i += 1

    return tokens[0]






def calculate_stack(s: str) -> int:
    stack = []
    num = 0
    sign = '+'
    i = 0

    while i < len(s):
        ch = s[i]

        if ch.isdigit():
            num = num * 10 + int(ch)

        if ch in "+-*/" or i == len(s) - 1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            elif sign == '/':
                prev = stack.pop()
                stack.append(int(prev / num))  # truncate toward zero

            sign = ch
            num = 0

        i += 1

    return sum(stack)