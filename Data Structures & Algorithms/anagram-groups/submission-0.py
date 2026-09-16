class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [""]
        else:
            d = {}
            for i in strs:
                if "".join(sorted(i)) not in d:
                    d["".join(sorted(i))] = [i]
                else:
                    d["".join(sorted(i))].append(i)
            return [value for value in d.values()]