secret = "1807"

guess = "7810"

A=0

a={}

B=0

for i in range(len(secret)):
    if secret[i]==guess[i]:
        A+=1
    else:
        if secret[i] in a:
            a[secret[i]]+=1
        else:
            a[secret[i]]=1

for i in range(len(guess)):
    if guess[i] in a:
        if a[guess[i]]>0:
            B+=1
            a[guess[i]]-=1
            
print(f"{A}A{B}B")










from collections import Counter

secret = "1807"
guess  = "7810"

# Step 1: Count bulls directly
A = sum(s == g for s, g in zip(secret, guess))

# Step 2: Count frequencies of digits (only for mismatches)
secret_counter = Counter(s for s, g in zip(secret, guess) if s != g)
guess_counter  = Counter(g for s, g in zip(secret, guess) if s != g)

# Step 3: Count cows as the overlap in counts
B = sum((secret_counter & guess_counter).values())

print(f"{A}A{B}B")