asteroids = [5, 10, -5, -8, 12, -15, 20, -3, -20]

i=1

ans=[asteroids[0]]

def ispositive(num):
    return True if num>0 else False

while i < len(asteroids):
    if ispositive(asteroids[i]):
        if ispositive(ans[-1]):  # both right moving
            ans.append(asteroids[i])
            i += 1
        else:  # ans[-1] is negative, current is positive → no collision (they move apart)
            ans.append(asteroids[i])
            i += 1
    else:  # current asteroid is negative
        if not ispositive(ans[-1]):  # both left
            ans.append(asteroids[i])
            i += 1
        else:  # collision case: ans[-1] >0, asteroid[i] <0
            if abs(asteroids[i]) > abs(ans[-1]):
                ans.pop()  # destroy last positive
                # don't increment i yet, recheck this asteroid with new ans[-1]
                if not ans:  
                    ans.append(asteroids[i])
                    i += 1
            elif abs(asteroids[i]) == abs(ans[-1]):
                ans.pop()
                i += 1
            else:  # abs(asteroids[i]) < abs(ans[-1]) → current destroyed
                i += 1

print("Final state:", ans)






def asteroidCollision(asteroids):
    stack = []
    for a in asteroids:
        alive = True
        while alive and a < 0 and stack and stack[-1] > 0:
            if stack[-1] < -a:
                stack.pop()      # stack asteroid destroyed, continue loop
                continue
            elif stack[-1] == -a:
                stack.pop()      # both destroyed
            alive = False        # current asteroid destroyed
        if alive:
            stack.append(a)
    return stack

# Test
print(asteroidCollision([5, 10, -5, -8, 12, -15, 20, -3, -20]))