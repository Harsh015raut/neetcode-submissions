class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        left = 0
        lst = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            left=i+1
            right = len(nums) - 1 
            # while left<right:
            #     if nums[left]+nums[right] == -nums[i] and [nums[i],nums[left],nums[right]] not in lst:
            #         lst.append([nums[i],nums[left],nums[right]])
            #         left+=1
            #         right-=1
            #     elif nums[left] + nums[right] < -nums[i]:
            #         left+=1
            #     else:
            #         right-=1
            
            while left < right:
                total = nums[left] + nums[right]
                if total == -nums[i]:
                    lst.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
        
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif total < -nums[i]:
                    left += 1
                else:
                    right -= 1
        return lst  