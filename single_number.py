"""
Problem Statement:
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return [i for i in set(nums) if nums.count(i) < 2][0]
