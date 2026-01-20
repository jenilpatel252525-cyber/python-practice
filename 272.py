s = "2[ab]3[c]"

num={"1","2","3","4","5","6","7","8","9","0"}

def decode(i,curr):
    if i>=len(s):
        return ""
    if s[i] in num:
        n=""
        while i<len(s) and s[i] in num:
            n+=s[i]
            i+=1
        return curr + int(n) * decode(i,"")
    elif s[i]=="[":
        return curr + decode(i+1,"")
    elif s[i]=="]":
        return curr + decode(i+1,"")
    else:
        return curr + decode(i+1,s[i])
    
print(decode(0,""))







s = "10[a2[c]]"

num = {"0","1","2","3","4","5","6","7","8","9"}

def decode(i):
    curr = ""
    while i < len(s):
        if s[i] in num:
            n = ""
            while i < len(s) and s[i] in num:
                n += s[i]
                i += 1
            # recursively decode inside brackets
            decoded, i = decode(i+1)   # skip '['
            curr += int(n) * decoded
        elif s[i] == "[":
            decoded, i = decode(i+1)
            curr += decoded
        elif s[i] == "]":
            return curr, i
        else:
            curr += s[i]
        i += 1
    return curr, i

print(decode(0)[0])   # Output: "accaccaccaccaccaccaccaccaccacc"
