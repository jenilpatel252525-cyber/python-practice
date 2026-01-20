s1 = "aabcc"

s2 = "dbbca"

s3 = "aadbbcbcac"

curr1=0

curr2=0

curr=0

def interleave(curr,curr1,curr2):
    if curr>=len(s3):
        return curr1 == len(s1) and curr2 == len(s2)
    res=False
    if curr1<len(s1) and s3[curr]==s1[curr1]:
        res=res or interleave(curr+1,curr1+1,curr2)
    if curr2<len(s2) and s3[curr]==s2[curr2]:
        res=res or interleave(curr+1,curr1,curr2+1)
    return res

print(interleave(curr,curr1,curr2))