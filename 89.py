a= [2, 3, 6, 7]

target = 7

b=[]

i=0

curr = []

def csum(a, curr, i):
    if i >= len(a):                      # LINE 1
        return
    curr.append(a[i])                    # LINE 2
    if sum(curr) == target:             # LINE 3
        b.append(curr[:])                # LINE 4
        return
    if sum(curr) > target:              # LINE 5
        return
    csum(a, curr, i)                     # LINE 6
    curr.pop()                           # LINE 7
    csum(a, curr, i + 1)                 # LINE 8

    
csum(a,curr,i)




a = [2, 3, 6, 7]
target = 7
b = []

def csum(i, curr, total):
    if total == target:
        b.append(curr[:])
        return
    if total > target or i >= len(a):
        return

    # Include a[i]
    curr.append(a[i])
    csum(i, curr, total + a[i])  # Reuse same element
    curr.pop()

    # Exclude a[i] and move to next
    csum(i + 1, curr, total)

csum(0, [], 0)
print(b)
