"""
Given an integer array arr, count element x such that x + 1 is also in arr.
If there're duplicates in arr, count them seperately.
"""

class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        return sum([arr.count(i) for i in set(arr) if i+1 in arr])
