import random
import bisect

class Solution:
    def __init__(self, rects):
        self.rects = rects
        self.prefix = []

        total_points = 0
        for x1, y1, x2, y2 in rects:
            # Calculate number of integer points in this rectangle
            area = (x2 - x1 + 1) * (y2 - y1 + 1)
            total_points += area
            self.prefix.append(total_points)  # cumulative point count

    def pick(self):
        # Pick a random integer from 1 to total number of points
        point_index = random.randint(1, self.prefix[-1])

        # Find the rectangle using binary search
        rect_index = bisect.bisect_left(self.prefix, point_index)
        x1, y1, x2, y2 = self.rects[rect_index]

        # Now use your idea: pick random x and y in the chosen rectangle
        rand_x = random.randint(x1, x2)
        rand_y = random.randint(y1, y2)

        return [rand_x, rand_y]
