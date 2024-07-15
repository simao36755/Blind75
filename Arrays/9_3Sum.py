# Topics: Array, Sorting, Two Pointer
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for idx, val in enumerate(nums):
            # avoid first num duplicate
            if idx>0 and val == nums[idx-1]:
                continue
            l = idx + 1
            r = len(nums) - 1
            while l < r:
                sum = val + nums[l] + nums[r]
                if sum == 0:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    # avoid second num duplicate
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                elif sum > 0:
                    r -= 1
                else:
                    l += 1
        
        return res


s = Solution()
nums = nums = [-1,0,1,2,-1,-4]
print(s.threeSum(nums))

# Input: nums (array) Output: List[List[int]] (每個list內是三個加起來是零的數字)
# Method: [ -1, -1, -1, 0, 1, 2]
#          cur   L            R

# Sorting好的list，固定cur，剩下的數字用Two Pointer做Two Sum