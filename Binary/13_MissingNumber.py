# Topics: Arrays, Hashtable
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]
        return res


s = Solution()
nums = [0,1,3]
print(s.missingNumber(nums))

# Input: nums (int array) Output: num (int) [0,n]缺乏的那個數字
# Methods: [0,1,3]  缺2
# [0,1,2,3] 跟 [0,1,3]
#   sum     -    sum

# Methods: 也可以用hashset做，[0,1,3] 跟 set(0,1,2,3) 
#                            i      in set: set.remove(i)