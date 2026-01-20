a=[9,9,9]

l=len(a)

i=len(a)-1

while(i>=0):
    a[i]=a[i]+1
    if(a[i]>9):
        a[i]=0
        i=i-1

        if a[0]==0:
            print([1] + [0] * l)

    else:
        print(a)
        break

# def plusOne(digits):
#     n = len(digits)
    
#     for i in range(n - 1, -1, -1):
#         if digits[i] < 9:
#             digits[i] += 1
#             return digits  # No carry needed, done
#         digits[i] = 0  # Set current to 0, carry to next
    
#     # If we got through the whole list, all were 9s
#     return [1] + [0] * n
