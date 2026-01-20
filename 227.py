def getImportance(employees, id):
    # Build hashmap: id -> (importance, subordinates)
    emp_map = {emp[0]: (emp[1], emp[2]) for emp in employees}

    def dfs(emp_id):
        importance, subs = emp_map[emp_id]
        total = importance
        for sub in subs:
            total += dfs(sub)
        return total

    return dfs(id)

employees = [[1,2,[5]],[5,-3,[]]]
id = 1

print(getImportance(employees,id))









from collections import deque

def getImportance(employees, id):
    # Build hashmap
    emp_map = {emp[0]: (emp[1], emp[2]) for emp in employees}

    total = 0
    queue = deque([id])

    while queue:
        curr_id = queue.popleft()
        importance, subs = emp_map[curr_id]
        total += importance
        queue.extend(subs)  # add all subordinates to queue

    return total