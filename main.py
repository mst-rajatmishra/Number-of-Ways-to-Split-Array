from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        prefix_sum = 0
        valid_splits = 0
        
        # Iterate through the array, checking splits from index 0 to n-2
        for i in range(n - 1):
            prefix_sum += nums[i]
            if prefix_sum >= total_sum - prefix_sum:
                valid_splits += 1
        
        return valid_splits
