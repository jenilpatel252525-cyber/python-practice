a=[1,2,1,2,1]

k=2

b=set()
i=0
while i<len(a):
    if a[i] in b and i - a.index(a[i],0,i-1) <= k:
        print("yes")
        break
    else:
        b.add(a[i]) #not working for a
        i+=1

a = [1, 2, 3, 1, 4, 5]
k = 2

last_seen = {}

for i, val in enumerate(a):
    if val in last_seen and i - last_seen[val] <= k:
        print("yes")
        break
    last_seen[val] = i
else:
    print("no")


a = [1, 2, 1, 2, 1]
k = 2

c = {}  # key: element, value: last seen index
i = 0

while i < len(a):
    if a[i] in c:
        if i - c[a[i]] <= k:
            print("yes")
            break
    # update index of the current element
    c[a[i]] = i
    i += 1
else:
    print("no")
