"""
Given two strings S and T, return if they are equal when both are typed into empty text editors.
# means a backspace character.
"""

class Solution(object):
    def check(self, S):
        S_1 = []
        for i in S:
            if i != "#":
                S_1.append(i)
            elif len(S_1)>0:
                S_1.pop()
        return S_1

    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return (self.check(S) == self.check(T))
