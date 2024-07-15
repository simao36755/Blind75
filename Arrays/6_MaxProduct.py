# Topics: Array, Dynamic Programming
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = nums[0]
        curMax, curMin = 1, 1

        for i in nums:
            if i == 0:
                curMax = 1
                curMin = 1
                global_max = max(i, global_max)
                continue
            val1 = curMax*i #The operation can only be performed once.
            val2 = curMin*i
            curMax = max(val1, val2, i)
            curMin = min(val1, val2, i)
            global_max = max(global_max, curMax)
        
        return global_max

s = Solution()
nums = [-4,-3,-2]
print(s.maxProduct(nums))


# Input: nums (array) Output: 連續乘積最大數 (int)
# Methods: 乘法可能有負負得正 正負得負的問題，維護curMax, curMin，遇到0就重設curMax, curMin成1
# [    -4    ,    -3    ,    -2    ]
#  curMax:-4 ,curMax:12 ,curMax:6
#  curMin:-4 ,curMin:-3 ,curMin:-24