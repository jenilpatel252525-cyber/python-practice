# a=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21]

import math
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
j=len(a)

sum=0
i=1

while sum<j:
    sum=sum+i
    i=i*2

p=int((sum-1)/2 - 1)

k=sum-(i/4)

b=[]
c=[]
low=0

high=len(a)-1

mid=int((low+high)/2)

while True:
    if high-low==2:
        mid1=int((low+high)/2) 
        # print(mid1)
        b.append(a[mid1])
        if len(b)==sum:
            break
        b.append(a[mid1-1])
        if j < k:
            b.append(None)
            b.append(None)
        if len(b)==sum:
            break
        b.append(a[mid1+1])
        if j < k:
            b.append(None)
            b.append(None)
        if len(b)==sum:
            break
        if len(c)<=1:
            if len(c)<=0:
                low=high+2
                high=len(a)-1
            else:
                low=c.pop()+1
                if b.count(a[mid-1])<1:
                    high=a[mid-1]
                else:
                    high=len(a)-1
        else:
            low=c.pop()+1
            high=c.pop()-1

    elif high-low<=1:
        mid1=int((low+high)/2)
        # print(mid1)
        b.append(a[mid1])
        if len(b)==sum:
            break
        if mid1-1 < low:
            b.append(None)
            if len(b)==sum:
                break
        if b.count(a[mid1+1]) > 0:
            b.append(None)
            if len(b)==sum:
                break
        else:
            b.append(a[mid1+1])
            if len(b)==sum:
                break
        if len(c)<=1:
            if len(c)<=0:
                low=high+2
                high=len(a)-1
            else:
                low=c.pop()+1
                if b.count(a[mid-1])<1:
                    high=a[mid-1]
                else:
                    high=len(a)-1
        else:
            low=c.pop()+1
            high=c.pop()-1
    else:
        mid1=int((low+high)/2)
        # print(mid1)
        b.append(a[mid1])
        if len(b)==sum:
            break
        c.append(mid1)
        high=mid1-1

d=[]
r=1
q=1
d.append(b[0])
ctr=2
ctr1=2
ctr2=2
while True:
    if ctr<=0:
        p=int((p/2)-1)
        r=q+1
        # print(r)
        q=q+1
        ctr=ctr1*2
        ctr1=ctr1*2
        ctr2=ctr1
    d.append(b[r])
    ctr=ctr-1
    if len(d)>=len(b):
        break
    # if ctr % 2 == 0:
    #     if ctr % 4 == 0:
    #         if ctr % 8 == 0:
    #             r=r+p+4
    #         else:
    #             r=r+p+3
    #     else:
    #         r=r+p+2
    # else:
    #     r=r+p+1

    # if ctr % 8 == 0:
    #     r=r+p+4
    # elif ctr % 4 == 0:
    #     r=r+p+3
    # elif ctr % 2 == 0:
    #     r=r+p+2
    # else:
    #     r=r+p+1

    add = 1
    temp = ctr

    while temp % 2 == 0 and temp != 0:
        add += 1
        temp //= 2

    r = r + p + add

    print(r)

# print(b)
print(d)




5,   2,   1,None,None,   3,None,4,    8,   6,None,7,    9,None,10 

5,2,8,1,3,6,9,None,None,None,4,None,7,None,10



from collections import deque

def sorted_array_to_balanced_level_order(arr):
    if not arr:
        return []

    # Step 1: Build height-balanced BST (using recursion)
    class TreeNode:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    def build_tree(low, high):
        if low > high:
            return None
        mid = (low + high) // 2
        node = TreeNode(arr[mid])
        node.left = build_tree(low, mid - 1)
        node.right = build_tree(mid + 1, high)
        return node

    root = build_tree(0, len(arr) - 1)

    # Step 2: Level-order traversal with None placeholders
    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Optional: Trim trailing None values
    while result and result[-1] is None:
        result.pop()

    return result
