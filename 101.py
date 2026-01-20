a=[0,0,1,1,1,1,2,3,3]
curr=0
i=0
start=0
end=0

while i<len(a)-1:
    start=i
    end=i
    while i < len(a) - 1 and a[i]==a[i+1]:
        end=i+1
        i+=1
    while end-start+1 > 2:
        del a[start]
        end-=1
        i-=1
    i+=1
    
print(a)





a = [0, 0, 1, 1, 1, 1, 2, 3, 3]
write = 0

for read in range(len(a)):
    if write < 2 or a[read] != a[write - 2]:
        a[write] = a[read]
        write += 1

print(a[:write])
