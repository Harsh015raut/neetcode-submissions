class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            l = 0
            longstr = 0
            elem = set() 
            for r in range(len(s)):
                while s[r] in elem:
                    elem.remove(s[l])
                    l+=1
                elem.add(s[r])
                longstr = max(longstr,len(elem))
            return longstr

            # while l<len(s)-1:
            #     r+=1
            #     if s[r] in elem:
            #         elem.remove(s[l])

            #     if s[l]!=s[r] and s[l] and s[r] not in elem:
            #         elem.add(s[l])
            #         elem.add(s[r])
            #         l+=1
            #         st+=1
            #         longstr = max(longstr,st)   
            #     else:
            #         longstr = max(longstr,st)
            #         elem = set()
            #         st=1
            #         l+=1
            # return longstr
            
            

            



        
