tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

s=set()

s.add("+")
s.add("-")
s.add("*")
s.add("/")

stack = []

for i in range(len(tokens)):
    if tokens[i] in s:
        b=stack.pop()
        a=stack.pop()
        c=tokens[i]
        if c == "+":
            result = a + b
        elif c == "-":
            result = a - b
        elif c == "*":
            result = a * b
        elif c == "/":
            result = int(a / b)
        stack.append(result)
    else:
        stack.append(int(tokens[i]))

print(stack.pop())