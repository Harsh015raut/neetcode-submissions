class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in range(len(strs)):
            s+=f"{len(strs[i])}+{strs[i]}"
        return s

    def decode(self, s: str) -> List[str]:
        lst=[]
        i = 0
        gap = 0
        while i<len(s):
            if s[i]=="+":
                l = int(s[i-gap:i])
                lst.append(s[i+1:i+l+1])
                i = i+l+1 
                gap = 0
            else:
                i+=1
                gap+=1
        return lst