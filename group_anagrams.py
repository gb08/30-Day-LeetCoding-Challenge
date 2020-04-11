"""
Given an array of strings, group anagrams together.
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = {}
        for i,new_a in enumerate(strs):
            new_a = str(sorted(new_a))
            if new_a not in result:
                result.update({new_a: [strs[i]]})
            else:
                result[new_a].append(strs[i])
 
        return list(result.values())
