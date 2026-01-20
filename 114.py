a=[2,3,-2,-4,-1,3,-5,2]

product=-float("inf")

cp=1

pos=False

neg=False

for i in range(len(a)):
    if a[i]>0:
        if not pos:
            cp=1
        pos=True
        neg=False
    elif a[i]==0:
        pos=False
        neg=False
    else:
        if not neg:
            cp=1
        neg=True
        pos=False
    if pos:
        cp=cp*a[i]
    elif neg:
        cp=cp*a[i]
    else:
        cp=cp*a[i]
    product=max(product,cp)
    
print(product)







a = [-2, 0, -1]

max_product = a[0]
curr_max = a[0]
curr_min = a[0]

for i in range(1, len(a)):
    num = a[i]
    if num < 0:
        curr_max, curr_min = curr_min, curr_max  # Swap when negative

    curr_max = max(num, curr_max * num)
    curr_min = min(num, curr_min * num)

    max_product = max(max_product, curr_max)

print(max_product)
