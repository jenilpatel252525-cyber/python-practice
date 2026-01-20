from collections import defaultdict

a = [4, 2, 2, 6, 4]
k = 6
L = 2
R = 3
x=0
count=0
s={}

for i in range(len(a)):
    if a[i]==k:
        if 1 in range(L,R+1):
            count+=1
    x=x^a[i]
    if x==k and i>0:
        if i in range(L,R+1):
            count+=1
    s[i]=x

j=0
x2=0
flag=False

while j<len(s):
    if s[j]==k:
        flag=True
    if flag:
        x2=x2^a[i]
        if x2==0 and i-j+1 in range(L,R+1):
            count+=1
            flag=False
    else:
        j+=1

print(count)