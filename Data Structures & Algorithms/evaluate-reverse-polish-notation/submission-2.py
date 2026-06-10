class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                result = num1 + num2
                stack.append(result)
            elif token == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                result = num2 - num1
                stack.append(result)
            elif token == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                result = num2 * num1
                stack.append(result)
            elif token == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                result = num2 / num1
                stack.append(int(result))
            else:
                stack.append(int(token))
        return stack[0]