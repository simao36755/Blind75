# Topics: Array, Prefix, Postfix
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefixMult = 1
        for i in range(len(nums)):
            res[i] *= prefixMult
            prefixMult *= nums[i]
        postfixMult = 1
        for j in range(len(nums)-1,-1,-1):
            res[j] *= postfixMult
            postfixMult *= nums[j]

        return res

s = Solution()
nums = [1,2,3,4]
print(s.productExceptSelf(nums))

# Input: nums (array) Output: 除了自己之外所有的數字乘起來的數字array (array)
# Method: 把除了自己以外的prefix數字乘起來放入res, 再把除了自己以外的postfix數字乘起來再乘上res中的數字，就會是除了自己以外的所有數字相乘
#           nums = [1,2,3,4] , res=[]
#         res[0]=prefix (1)             res=[1]
#         res[1]=prefix * nums[0]       res=[1,1]
#         res[2]=prefix * nums[1]       res=[1,1,2]
#         res[3]=prefix * nums[2]       res=[1,1,2,6]
#         -------------------------------------------
#         res[3] *= postfix (1)         res=[1,1,2,6]
#         res[2] *= postfix (4)         res=[1,1,8,6]
#         res[1] *= postfix (12)        res=[1,12,8,6]
#         res[0] *= postfix (24)        res=[24,12,8,6]