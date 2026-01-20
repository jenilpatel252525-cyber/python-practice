s=")(()("

stack=[]

count=0

for i in range(len(s)):
    if s[i]=="(":
        stack.append(i)
    else:
        if len(stack)>0: 
            stack.pop()
        else:
            count+=1
            
count+=len(stack)

print(count)