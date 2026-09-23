class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        left = 0
        lst = []
        for i in range(len(nums)):
            left=i+1
            right = len(nums) - 1 
            while left<right:
                if nums[left]+nums[right] == -nums[i] and [nums[i],nums[left],nums[right]] not in lst:
                    lst.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                elif nums[left] + nums[right] < -nums[i]:
                    left+=1
                else:
                    right-=1
        return lst  