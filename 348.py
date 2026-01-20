s = "deeedbbcccbdaa"

k = 3

stack=[]

count=[]

i=0

while i<len(s):
    if stack:
        curr,c=stack[-1][0],stack[-1][1]
        if s[i]==curr:
            c+=1
            if c==k:
                stack.pop()
                i+=1
            else:
                stack[-1][1]=c
                i+=1
        else:
            stack.append([s[i],1])
            i+=1
    else:
        stack.append([s[i],1])
        i+=1
        
print(stack)








for ch in s:
    if stack and stack[-1][0] == ch:
        stack[-1][1] += 1
        if stack[-1][1] == k:
            stack.pop()
    else:
        stack.append([ch, 1])
