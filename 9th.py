item=["apple","banana","apple","grapes"]

for i in item:
    if item.count(i) > 1:
        print("duplicate",i)
        break