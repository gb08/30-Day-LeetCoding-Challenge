"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
"""

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len, count = 0,0
        num_map = {}
        
        if nums.count(0) == nums.count(1):
            return len(nums)
        for i,n in enumerate(nums):
            count += 1 if n else -1
            if count == 0:
                max_len = i + 1
            elif count in num_map:
                max_len = max(max_len, i-num_map[count])
            else:
                num_map[count] = i
        return max_len 
                    
