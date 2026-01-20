words = ["a","ab","abc","d","cd","bcd","abcd"]

words.sort()

length=0

def have_common_char(s1, s2):
    return bool(set(s1) & set(s2))

for i in range(len(words)):
    j=len(words)-1
    while not have_common_char(words[i],words[j]) and j>i:
        length=max(length,len(words[i])*len(words[j]))
        j-=1
        
print(length)



def maxProduct(words):
    n = len(words)
    masks = [0] * n
    lengths = [len(word) for word in words]

    # Step 1: Compute bitmask for each word
    for i in range(n):
        mask = 0
        for ch in words[i]:
            mask |= 1 << (ord(ch) - ord('a'))  # set bit for each character
        masks[i] = mask

    # Step 2: Compare all pairs and check for no common letters
    max_product = 0
    for i in range(n):
        for j in range(i + 1, n):
            if masks[i] & masks[j] == 0:
                product = lengths[i] * lengths[j]
                max_product = max(max_product, product)

    return max_product