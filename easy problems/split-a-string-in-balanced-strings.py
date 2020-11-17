class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = []
        count = 0
        for i in s:
            if len(stack) == 0:
                stack.append(i)
            elif i == "L":
                if stack[-1] == "R":
                    stack.pop()
                else:
                    stack.append(i)
            else:
                if stack[-1] == "L":
                    stack.pop()
                else:
                    stack.append(i)
            if len(stack) == 0:
                count += 1
        return count