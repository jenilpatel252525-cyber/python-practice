dominoes = "RRL"

ans=""

prefix=[0]*len(dominoes)

for i in range(len(dominoes)):
    if dominoes[i]=="L":
        prefix[i]=-1
    elif dominoes[i]=="R":
        prefix[i]=1
    else:
        prefix[i]=0
        
for i in range(len(dominoes)-1):
    if dominoes[i+1]=="L":
        prefix[i]-=1
        
for i in range(1,len(dominoes)):
    if dominoes[i-1]=="R":
        prefix[i]+=1
        
for i in range(len(dominoes)):
    if prefix[i]==0:
        ans+="."
    elif prefix[i]==-1:
        ans+="L"
    else:
        ans+="R"
        
print(ans)