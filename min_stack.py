"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.items == []:
            self.items.append([x,x])
            return
        self.items.append([x,min(x, self.items[-1][1])])
        

    def pop(self):
        """
        :rtype: None
        """
        if self.items != []:
            self.items.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if self.items != []:
            return self.items[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        #print(self.items)
        if self.items != []:
            return self.items[-1][1]
