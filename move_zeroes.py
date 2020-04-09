"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the 
relative order of the non-zero elements.
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p = 0
        q = 1
        
        while p < q and q < len(nums):
            if nums[p] == 0 and nums[q] != 0:
                nums[p] = nums[q]
                nums[q] = 0
            elif nums[p] == 0 and nums[q] == 0:
                q += 1
                continue
            
            p += 1
            q += 1
