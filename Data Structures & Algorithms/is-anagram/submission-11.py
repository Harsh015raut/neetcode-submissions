class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        t1 = {}
        for char in s:
            if char in s1:
                s1[char] +=1
            else:
                s1[char] = 1        
        for char in t:
            if char in t1:
                t1[char] +=1
            else:
                t1[char] = 1    
        if t1.keys() == s1.keys():
            for i in s1:
                if s1[i] != t1[i]:
                    return False 
            return True 
        else:
            return False 
        # return s1==t1  
        
            
        