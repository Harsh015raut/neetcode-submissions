class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return 

        d = {} # {0:3,1:4,2:5,3:6}
        for i in range(len(nums)):
            partner = target - nums[i]
            if partner in d:
                return [d[partner],i]
            d[nums[i]] = i         