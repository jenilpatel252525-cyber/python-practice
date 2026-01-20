s = "catsanddog"

wordDict = ["cats","dog","sand","and","cat"]

temp=""

answer=""

def pop_last_char(s):
    return s[:-1] if s else s

def find(j,answer):
    # if j == len(s):
    #     return True
    for i in range(j,len(s)):
        temp = s[j:i+1]
        if temp in wordDict:
            answer+=temp
            if answer==s:
                return True
            temp=""
            if find(i+1,answer):
                return True
            # temp=pop_last_char(temp)
    return False

print(find(0,answer))