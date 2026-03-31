class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            top = len(stack)-1
            if len(stack) > 0 and (i == ")" and stack[top] == "(" or i == "]" and stack[top] == "[" or i == "}" and stack[top] == "{"):
                stack.pop(top)
            else:
                stack.append(i)
        
        return len(stack) == 0