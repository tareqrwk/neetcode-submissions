class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"(": ")", "[": "]", "{": "}"}

        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            if not stack:
                return False
            if bracket not in pairs:
                top = stack.pop()   
                if pairs[top] != bracket:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

