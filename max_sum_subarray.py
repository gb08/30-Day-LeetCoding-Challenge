"""
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = nums[0]
        final_sum = nums[0]
        for i in nums[1:]:
            maxsum = max(i, maxsum + i)
            final_sum = max(final_sum, maxsum)
        return final_sum
