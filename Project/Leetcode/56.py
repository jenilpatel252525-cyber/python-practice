a=[-1, 10, -2, 3, 2, 1]

k=3

s1={}
s2={}

c1=0
c2=0

for i in range(k):
    c1+=a[i]
    c2+=a[-(i+1)]
    s1[i]=c1
    s2[i]=c2

sum=max(s1[k-1],s2[k-1])

for j in range(k-1):
    sum=max(sum,s1[j]+s2[k-2-j])

print(sum)