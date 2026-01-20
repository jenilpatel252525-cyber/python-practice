houses = [1, 4, 8, 10, 15, 20]
heaters = [3, 9, 18]

heated = {}
radius = 0

while len(heated) < len(houses):
    radius += 1
    for heater in heaters:
        for house in houses:
            if house in heated:
                continue
            if heater - radius <= house <= heater + radius:
                heated[house] = True

print(radius)





houses = [1, 4, 8, 10, 15, 20]
heaters = [3, 9, 18]

unheated = set(houses)
radius = 0

while unheated:
    radius += 1
    heated_now = set()
    for heater in heaters:
        for house in unheated:
            if heater - radius <= house <= heater + radius:
                heated_now.add(house)
    unheated -= heated_now  # remove heated houses

print(radius)





houses = [1, 4, 8, 10, 15, 20]
heaters = [3, 9, 18]

unheated = set(houses)
unheated-=set(heaters)

radius = 0

while unheated:
    radius += 1
    heated_now = set()
    for heater in heaters:
        heated_now.add(heater-radius)
        heated_now.add(heater+radius)
    unheated -= heated_now

print(radius)


houses = [1, 4, 8, 10, 15, 20]
heaters = [3, 9, 18]

unheated = set(houses)
radius = 0

# Remove already heated houses (radius 0)
for h in heaters:
    unheated.discard(h)

while unheated:
    radius += 1
    for h in heaters:
        unheated.discard(h - radius)
        unheated.discard(h + radius)

print(radius)



def findRadius(houses, heaters):
    houses.sort()
    heaters.sort()
    i = 0
    radius = 0

    for house in houses:
        # Move to the closest heater
        while i < len(heaters) - 1 and abs(heaters[i + 1] - house) <= abs(heaters[i] - house):
            i += 1
        distance = abs(heaters[i] - house)
        radius = max(radius, distance)

    return radius

# Example
houses = [1, 4, 8, 10, 15, 20]
heaters = [3, 9, 18]
print(findRadius(houses, heaters))  # Output: 2
