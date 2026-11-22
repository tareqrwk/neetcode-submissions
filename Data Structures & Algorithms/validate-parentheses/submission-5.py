class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paranthesis = {"(": ")", "{": "}", "[": "]"}

        for char in s:
            if char in paranthesis:
                stack.append(char)
            if not stack:
                return False
            if char not in paranthesis:
                top = stack.pop()
                if paranthesis[top] != char:
                    return False
        return len(stack) == 0