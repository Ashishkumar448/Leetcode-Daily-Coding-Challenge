from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        count = 0
        
        # Iterate over each soldier rating as the middle soldier in the team
        for j in range(1, n-1):
            left_smaller = left_larger = right_smaller = right_larger = 0
            
            # Count how many soldiers on the left are smaller and larger than rating[j]
            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                elif rating[i] > rating[j]:
                    left_larger += 1
            
            # Count how many soldiers on the right are smaller and larger than rating[j]
            for k in range(j+1, n):
                if rating[k] < rating[j]:
                    right_smaller += 1
                elif rating[k] > rating[j]:
                    right_larger += 1
            
            # The number of teams with rating[j] as the middle soldier
            count += left_smaller * right_larger + left_larger * right_smaller
        
        return count

# Example usage
rating = [2, 5, 3, 4, 1]
solution = Solution()
print(solution.numTeams(rating))  # Output: 3
