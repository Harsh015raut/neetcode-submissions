class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower()
        S = ""
        for i in s:
            if i.isalnum():
                S+=i
            else:
                pass 
        return S==S[::-1]
