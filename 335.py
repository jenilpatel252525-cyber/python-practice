class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # Directions: North, East, South, West
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0   # 0 = North
        x = y = 0

        for ch in instructions:
            if ch == 'G':
                dx, dy = dirs[d]
                x += dx
                y += dy
            elif ch == 'L':
                d = (d - 1) % 4
            else:  # 'R'
                d = (d + 1) % 4

        # Bounded if back to origin OR direction changed
        return (x == 0 and y == 0) or d != 0
