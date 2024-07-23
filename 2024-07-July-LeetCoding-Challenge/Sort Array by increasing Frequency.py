from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Count the frequencies of each number
        freqs = Counter(nums)
        
        # Sort based on frequency and value (in decreasing order)
        nums.sort(key=lambda x: (freqs[x], -x))
        
        return nums
