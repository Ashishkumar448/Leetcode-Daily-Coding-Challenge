class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        # Directions: north, east, south, west
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0  # Starting position
        d = 0  # Facing north initially
        obstacles_set = {(ox, oy) for ox, oy in obstacles}  # Convert to set for O(1) lookup
        max_distance = 0

        for command in commands:
            if command == -1:  # Turn right
                d = (d + 1) % 4
            elif command == -2:  # Turn left
                d = (d + 3) % 4
            else:  # Move forward
                for _ in range(command):
                    next_x = x + dirs[d][0]
                    next_y = y + dirs[d][1]
                    if (next_x, next_y) in obstacles_set:  # Check if the next position is an obstacle
                        break
                    x, y = next_x, next_y  # Move to the next position
                    max_distance = max(max_distance, x * x + y * y)  # Update the max Euclidean distance

        return max_distance
