from collections import deque

senate="RRDDD"

def predictPartyVictory(senate: str) -> str:
    n = len(senate)
    qr = deque()   # indices of 'R'
    qd = deque()   # indices of 'D'

    # 1) Fill the queues
    for i, c in enumerate(senate):
        if c == 'R':
            qr.append(i)
        else:
            qd.append(i)

    # 2) Simulate rounds
    while qr and qd:
        r = qr.popleft()
        d = qd.popleft()

        if r < d:
            # R acts first, bans this D, and comes back next round
            qr.append(r + n)
        else:
            # D acts first, bans this R, and comes back next round
            qd.append(d + n)

    return "Radiant" if qr else "Dire"






dp=[True]*len(senate)

r=senate.count("R")
d=senate.count("D")
a=0
b=0

while r>0 and d>0:
    for i in range(len(senate)):
        if dp[i]==True:
            if senate[i]=="R":
                if b==0:
                    a+=1
                else:
                    dp[i]=False
                    r-=1
                    b-=1
            else:
                if a==0:
                    b+=1
                else:
                    dp[i]=False
                    d-=1
                    a-=1
                    
print(r,d)