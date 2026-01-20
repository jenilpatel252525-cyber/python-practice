a=[1,2,3]

b=[]

curr=[]

def permutation():
    # print("0")
    if len(curr)==len(a):
            b.append(curr[:])
            # print("1")
            return
    for j in range(len(a)):
        if a[j] in curr:
            # print("2")
            continue
        curr.append(a[j])
        print(curr)
        # print("3")
        permutation()
        # print("4")
        curr.pop()
        # print("5")
    
permutation()

print(b)