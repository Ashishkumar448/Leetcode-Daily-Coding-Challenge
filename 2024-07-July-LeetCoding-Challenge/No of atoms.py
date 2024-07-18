from collections import defaultdict
import re

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        i, n = 0, len(formula)
        
        while i < n:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                i += 1
                i_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplicity = int(formula[i_start:i] or 1)
                top = stack.pop()
                for elem, count in top.items():
                    stack[-1][elem] += count * multiplicity
            else:
                i_start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                elem = formula[i_start:i]
                i_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplicity = int(formula[i_start:i] or 1)
                stack[-1][elem] += multiplicity
        
        result = ""
        for elem in sorted(stack[-1]):
            result += elem
            if stack[-1][elem] > 1:
                result += str(stack[-1][elem])
        
        return result

# Example usage
solution = Solution()
print(solution.countOfAtoms("K4(ON(SO3)2)2"))  # Output: "K4N2O14S4"
