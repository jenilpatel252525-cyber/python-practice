# a=set("qwertyuiopQWERTYUIOP")
# b=set("asdfghjklASDFGHJKL")
# c=set("zxcvbnmZXCVBNM")

# f=["Hello","Alaska","Dad","Peace"]
# j=0
# i=0

# x=[]

# a1=True
# b1=True
# c1=True

# e=""

# while i<len(f):
#     word=f[i]
#     if word[j] in a and a1:
#         b1=False
#         c1=False
#         e+=word[j]
#         j+=1
#         if j>=len(word):
#             x.append(e)
#             e=""
#             i+=1
#             j=0
#             a1=True
#             b1=True
#             c1=True
            
#     elif not b1 and not c1:
#         e=""
#         i+=1
#         j=0
#         a1=True
#         b1=True
#         c1=True
#     elif word[j] in b and b1:
#         a1=False
#         c1=False
#         e+=word[j]
#         j+=1
#         if j>=len(word):
#             x.append(e)
#             e=""
#             i+=1
#             j=0
#             a1=True
#             b1=True
#             c1=True
#     elif not a1 and not c1:
#         e=""
#         i+=1
#         j=0
#         a1=True
#         b1=True
#         c1=True
#     elif word[j] in c and c1:
#         a1=False
#         c1=False
#         e+=word[j]
#         j+=1
#         if j>=len(word):
#             x.append(e)
#             e=""
#             i+=1
#             j=0
#             a1=True
#             b1=True
#             c1=True
#     elif not b1 and not a1:
#         e=""
#         i+=1
#         j=0
#         a1=True
#         b1=True
#         c1=True

words = ["Hello", "Alaska", "Dad", "Peace"]

row1 = set("qwertyuiop")
row2 = set("asdfghjkl")
row3 = set("zxcvbnm")

rows = [row1, row2, row3]

output = []

for word in words:
    lower_word = set(word.lower())
    for row in rows:
        if lower_word.issubset(row):
            output.append(word)
            break  # no need to check other rows

print(output)



    
