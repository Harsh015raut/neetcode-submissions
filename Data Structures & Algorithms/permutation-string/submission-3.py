class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # w = 0 
        # l = 0 
        # for r in range(len(s2)):
        #     if s2[r] in s1 and s2[r]!=s2[r-1]:
        #         w+=1
        #         if w==len(s1):
        #             return True            
        #     else:
        #         l+=1
        #         w=0
        # return False

        s = {}
        for i in s1:
            if i in s:
                s[i]+=1
            else:
                s[i] = 1
        
        t = {}
        w = len(s1)
        l=0
        
        for r in range(len(s2)):
            t[s2[r]] = t.get(s2[r],0) + 1

            if r-l+1==w:
                if t==s:
                    return True
                t[s2[l]] -= 1
                if t[s2[l]] == 0:
                    del t[s2[l]]

                l += 1

        return False




            # if w==len(s1):
            #     return True
            # elif s2[r] in s1:
            #     r+=1
            # elif w>len(s1):
            #     return False
            # else:
            #     l+=1
            #     w=0
            
        