def exclusiveTime(n, logs):
    res = [0] * n
    stack = []
    prev_time = 0

    for log in logs:
        fid, typ, t = log.split(":")
        fid, t = int(fid), int(t)

        if typ == "start":
            if stack:
                # Add time spent to current running function
                res[stack[-1]] += t - prev_time
            stack.append(fid)
            prev_time = t
        else:  # "end"
            # Pop the function and add its time
            res[stack.pop()] += t - prev_time + 1
            prev_time = t + 1  # move past this end

    return res

n=1
logs=["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]

print(exclusiveTime(n,logs))