import time

wait_time=1

max_try=5

attempts=0

while attempts < max_try:
    print("attempt",attempts + 1,"wait time",wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1