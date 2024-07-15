#Topics: Array, Dynamic Programming, Sliding Window
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        slidewinSum = 0
        maxn = float('-inf')
        for i in nums:
            if slidewinSum < 0:
                slidewinSum = 0
            slidewinSum += i
            maxn = max(maxn, slidewinSum)
        
        return maxn

s = Solution()
nums = [-2,1,-3,4]
print(s.maxSubArray(nums))


# Input: nums (array) Output: 連續最大和 (int)
# Method: 用sliding window的方式，如果前綴是負數，拋棄前綴的總和。window後移，window如果有大於max max=window，
#                                                                     window如果沒大於max也不是負數，會一直往後加 找更大數字