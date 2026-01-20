people = [[9, 0], [7, 0], [7, 1], [6, 1], [5, 2], [4, 4], [6, 0], [5, 0], [5, 1], [4, 2]]

people.sort(key=lambda x: (x[1], x[0]))

ans=[]

for i in range(len(people)):
    if len(ans)==0:
        ans.append(people[0])
        people.remove(ans[-1])
        continue
    if any(p[1] <= len(ans) for p in people):
        matches = [p for p in people if p[1] <= len(ans)]
        matches.sort()
        for j in range(len(matches)):
            curr=matches[j]
            temp=[p for p in ans if p[0] >= curr[0]]
            if len(temp)==curr[1]:
                ans.append(curr)
                people.remove(ans[-1])
                break
    else:
        ans.append(people[0])
        people.remove(ans[-1])

print(ans)







def reconstructQueue(people):
    # Sort: descending by height, ascending by k
    people.sort(key=lambda x: (-x[0], x[1]))

    queue = []
    for person in people:
        queue.insert(person[1], person)
    return queue
