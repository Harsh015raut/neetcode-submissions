class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower()
        # S = ""
        # for i in s:
        #     if i.isalnum():
        #         S+=i
        #     else:
        #         pass 
        # return S==S[::-1]
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left].isalnum():
                if s[right].isalnum():
                    if s[left]==s[right]:
                        left+=1
                        right-=1
                    else:
                        return False
                else:
                    right-=1
            else:
                left+=1        

        return True
        # while left < right:
        
        #     while left < right and not s[left].isalnum():
        #         left += 1
   
        #     while left < right and not s[right].isalnum():
        #         right -= 1
    
        #     if s[left] != s[right]:
        #         return False
        #     left += 1
        #     right -= 1
        # return True