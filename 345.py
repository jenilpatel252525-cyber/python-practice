s = "(ed(et(oc))el)ba"

def reverseString(i):
    if i == len(s):
        return [], i

    if s[i] == "(":
        stack = []
        i += 1

        while i < len(s) and s[i].isalpha():
            stack.append(s[i])
            i += 1
        
        while i < len(s) and s[i] != ")":
            sub, i = reverseString(i)
            stack.extend(sub)
            
        stack.reverse()
        return stack, i + 1


    else:
        stack = []
        stack.append(s[i])
        i += 1

        while i < len(s) and s[i].isalpha():
            stack.append(s[i])
            i += 1

        return stack, i
    
st=[]

i=0
    
def solution(i):
    while i<len(s):
        res,i=reverseString(i)
        st.extend(res)
        
solution(0)

print("".join(st))










s = "(ed(et(oc))el)"

def reverseString(i):
    res = []

    while i < len(s):
        if s[i] == "(":
            sub, i = reverseString(i + 1)
            res.extend(sub[::-1])
        elif s[i] == ")":
            return res, i + 1
        else:
            res.append(s[i])
            i += 1

    return res, i


ans, _ = reverseString(0)
print("".join(ans))
