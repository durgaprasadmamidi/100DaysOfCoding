class Stack:
    def __init__(self):
        self.ls=[]
        
    def push(self,val):
        self.ls.append(val)
    
    def pop(self):
        return self.ls.pop()
    
    def peek(self):
        return self.ls[len(self.ls)-1]
    
    def isEmpty(self):
        return self.ls == []
    
    def pair(self,val):
        if val=='(':
            return ')'
        elif val=='{':
            return '}'
        elif val=='[':
            return ']'
            
class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        for i in s:
            if i in ['(','[','{']:
                stack.push(i)
            elif stack.isEmpty():
                return False
            elif i == stack.pair(stack.peek()):
                stack.pop()
            else:
                return False
        return stack.isEmpty()
