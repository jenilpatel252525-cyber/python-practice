gas = [1,2,3,4,5]

cost = [3,4,5,1,2]

m=len(gas)-1

flag=False

for i in range(len(gas)):
    start=i
    visited=set()
    j=i
    fuel=0
    answer=None
    
    while True:
        if j in visited:
            answer=start
            flag=True
            break
        visited.add(j)
        fuel+=gas[j]
        if j<m:
            if cost[j]>fuel:
                break
            else:
                fuel-=cost[j]
                j+=1
        else:
            if cost[j]>fuel:
                break
            else:
                fuel-=cost[j]
                j=0
                
    if flag:
        break
    
if not flag:
    print(-1)
    
else:
    print(answer)
    
    
def canCompleteCircuit(gas, cost):
    total_tank = 0      # Total net gas
    curr_tank = 0       # Gas in tank from start point
    start_index = 0     # Candidate starting station

    for i in range(len(gas)):
        gain = gas[i] - cost[i]
        total_tank += gain
        curr_tank += gain

        # If we run out of gas at i, we cannot start from `start_index`
        if curr_tank < 0:
            start_index = i + 1
            curr_tank = 0

    return start_index if total_tank >= 0 else -1