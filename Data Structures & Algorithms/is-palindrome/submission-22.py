class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for letter in s:
            if letter.isalnum():
                cleaned += letter
        cleaned = cleaned.lower()
        t = ""
        for i in range(len(cleaned) - 1, -1, -1):
            if cleaned[i].isalnum():
                t += cleaned[i]
        return cleaned == t