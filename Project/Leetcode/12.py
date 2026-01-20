a=[1,2,3,4]
i=0
b=set()
while(i<len(a)):
    if a[i] in b:
        print("repeated")
        break

    else:
        b.add(a[i])
        i+=1