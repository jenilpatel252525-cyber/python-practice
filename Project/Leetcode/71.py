def findsum(a,target):
    res = []
    def backtrack(start,path,total):
        if total == target:
            res.append(path[:])
            return
        if total>target:
            return
        for i in range(start,len(a)):
            path.append(a[i])
            backtrack(i+1, path, total + a[i])
            path.pop()
    backtrack(0,[],0)
    return res

b=findsum([10,1,2,7,6,1,5],8)

unique = set(tuple(sorted(sublist)) for sublist in b)

result = [list(t) for t in unique]

print(result)