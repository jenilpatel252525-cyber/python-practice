s = "aabcbc"

def isValid(s):
    stack=[]
    for i in s:
        if i=="c":
            if len(stack)>=2:
                if stack[-1]=="b" and stack[-2]=="a":
                    stack.pop()
                    stack.pop()
                else:
                    stack.append(i)
            else:
                return False
        else:
            stack.append(i)
            
    return len(stack)==0

print(isValid(s))





def isValid(s):
    stack = []
    for ch in s:
        if ch == "c":
            if len(stack) >= 2 and stack[-1] == "b" and stack[-2] == "a":
                stack.pop()
                stack.pop()
            else:
                return False
        else:
            stack.append(ch)
    return not stack



def isValid(s):
    stack = []
    for ch in s:
        stack.append(ch)
        if stack[-3:] == ['a','b','c']:
            stack.pop()
            stack.pop()
            stack.pop()

    return not stack
