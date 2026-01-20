citations = [5,0,6,1,5,7,5,4,5]

curr=0
num=0
minn=float("inf")

for i in range(len(citations)):
    if citations[i]>=curr:
        minn=min(minn,citations[i])
        if num<minn:
            curr=citations[i]
            num+=1
            curr=min(curr,num)
        
print(curr)





def hIndex(citations):
    citations.sort(reverse=True)
    h = 0
    for i, c in enumerate(citations):
        if c >= i + 1:
            h = i + 1
        else:
            break
    return h

# citations = [5, 0, 6, 1, 5, 7, 5, 4]
# print(hIndex(citations))  # Output: 5







def hIndex(citations):
    n = len(citations)
    count = [0] * (n + 1)  # count[i] = number of papers with i citations

    for c in citations:
        if c >= n:
            count[n] += 1  # All counts >= n go into bucket n
        else:
            count[c] += 1

    total = 0
    for i in range(n, -1, -1):  # Go from high to low
        total += count[i]  # total papers with at least i citations
        if total >= i:
            return i
    return 0