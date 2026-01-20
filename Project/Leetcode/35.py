a=[1,2,3,10,5,6,7]
b=[2,4,6,8,10]

c={}
d={}

for i in a:
    c[i]=a.index(i)
# c = {value: index for index, value in enumerate(a)}


for i in b:
    d[i]=b.index(i)

min=100

for key in c:
    if key in d:
        i=c[key]+d[key]
        if i<min:
            min=i

print(min)