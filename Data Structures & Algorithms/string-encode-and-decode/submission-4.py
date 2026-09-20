class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s+=f"{len(i)}+{i}"
        return s

    def decode(self, s: str) -> List[str]:
        decoded=[]
        gap = 0
        i=0
        while i<len(s): #"5+Hello5+World"
            if s[i]=="+":
                l = int(s[i-gap:i])
                decoded.append(s[i+1:i+l+1])
                i = i+l+1
                gap = 0
            else:
                gap+=1
                i+=1
        return decoded

        























