from typing import List

class Solution:
    def survivedRobots(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        robots = sorted([(positions[i], healths[i], directions[i], i) for i in range(n)])
        stack = []
        
        for pos, health, direction, index in robots:
            if direction == 'R':
                stack.append((pos, health, direction, index))
            else:  # direction == 'L'
                while stack and stack[-1][2] == 'R' and stack[-1][1] < health:
                    _, h, _, _ = stack.pop()
                    health -= 1
                if stack and stack[-1][2] == 'R':
                    if stack[-1][1] == health:
                        stack.pop()
                    else:
                        stack[-1] = (stack[-1][0], stack[-1][1] - 1, stack[-1][2], stack[-1][3])
                else:
                    stack.append((pos, health, direction, index))
        
        result = sorted(stack, key=lambda x: x[3])
        return [robots[i][3] for i in range(n) if robots[i] in result]

# Example usage
solution = Solution()
print(solution.survivedRobots([1, 3, 5, 6], [2, 3, 1, 1], "RLRL"))  # Output: [0, 3]
