import random,bisect

w=[1,2,4]

def randompick(w):
    total=sum(w)
    s=[]
    temp=0
    for i in range(len(w)):
        temp+=w[i]
        s.append(temp)
    picked=random.randint(1,total)
    idx=bisect.bisect_left(s,picked)
    return idx

print(randompick(w))