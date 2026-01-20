points = [[0,0],[1,0],[2,0]]

x=set()

for i in points:
    x.add(tuple(i))

count=0

def find_other_endpoint(a, b, c, d):
    x = 2 * a - c
    y = 2 * b - d
    return x, y

for i in points:
    a,b=i[0],i[1]
    for j in points:
        c,d=j[0],j[1]
        if c==a and d==b:
            continue
        else:
            e,f=find_other_endpoint(a, b, c, d)
            if (e,f) in x:
                count+=1
                
print(count)







def numberOfBoomerangs(points):
    count = 0

    for i in points:
        dist_map = {}
        for j in points:
            if i == j:
                continue
            dx = i[0] - j[0]
            dy = i[1] - j[1]
            dist = dx * dx + dy * dy  # no sqrt needed
            dist_map[dist] = dist_map.get(dist, 0) + 1

        for d in dist_map.values():
            count += d * (d - 1)  # permutations (j, k)

    return count