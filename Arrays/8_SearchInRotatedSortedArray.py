# Topics: Array, Binary search
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        
        while l <= r:
            m = (l+r) // 2
            # use mid determine whether it is target
            if nums[m] == target:
                return m
            # mid is left portion
            if nums[m] >= nums[l]:
                if target >= nums[l] and target <= nums[m]:
                    r = m-1
                else:
                    l = m+1
            # mid is right portion
            else:
                if target >= nums[m] and target <= nums[r]:
                    l = m+1
                else:
                    r = m-1

        return -1


s = Solution()
# nums = [3,1]
nums = [4,5,6,7,0,1,2]
target = 5
print(s.search(nums, target))


# Input: nums (array), target (int) Output: 回傳target的index (int)
# Methods: 用binary search切分，看切到的mid數字是不是target，不是的話有兩個情況，target在左群、target在右群
#          判斷左右群改動lmr，最後找出m==target or -1