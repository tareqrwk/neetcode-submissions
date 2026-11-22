class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_formated = ""
        for l in s:
            if l.isalnum():
                s_formated += l
        s_formated = s_formated.lower()
        left = 0
        right = len(s_formated) - 1
        while left < right:
            if s_formated[left] != s_formated[right]:
                return False
            left += 1
            right -= 1 
        return True