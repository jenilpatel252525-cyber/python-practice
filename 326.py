s = "101000"

curr=[0,s.count("0",1,len(s))]

minflip=sum(curr)

for i in range(1,len(s)):
    if s[i]=="0":
        curr[1]-=1
        if s[i-1]=="1":
            curr[0]+=1
    else:
        if s[i-1]=="1":
            curr[0]+=1
    if sum(curr)<minflip:
        minflip=sum(curr)
        
print(minflip)





s = "1100101100010110"

# CHANGED: left flips = number of '1's on left
# CHANGED: right flips = number of '0's on right
curr = [0, s.count("0")]

min_flips = curr[0] + curr[1]

for i in range(len(s)):
    if s[i] == "0":
        curr[1] -= 1   # CHANGED: remove one 0 from right side
    else:
        curr[0] += 1   # CHANGED: add one 1 to left side

    min_flips = min(min_flips,curr[0]+curr[1])

print(min_flips)
