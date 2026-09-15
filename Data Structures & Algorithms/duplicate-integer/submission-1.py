class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # d = {}
        # for i in range(len(nums)):
        #     if nums[i] in d:
        #         return True 
        #     d[nums[i]] = i
        # return False
        seen = set()
        for num in nums:
            if num in seen:
                return True 
            seen.add(num)
        return False
