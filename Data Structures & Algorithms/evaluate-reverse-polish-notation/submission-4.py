
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ["+", "-", "*", "/"] and len(stack)>1:
                num2 = str(stack.pop())
                num1 = str(stack.pop())
                exp = eval(num1 + i + num2)
                stack.append(int(exp))
            else:
                stack.append(i)
        return int(stack.pop()) 
        