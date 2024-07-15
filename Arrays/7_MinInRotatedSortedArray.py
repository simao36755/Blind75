# Topics: Array, Binary Search
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        while nums[l] > nums[r]:
            m = (l+r) // 2

            if nums[m] >= nums[l]: #m is left
                l = m+1
            else:
                r = m
            
        return nums[l]

s = Solution()
nums = [5,1,2,3,4]
print(s.findMin(nums))

# Input: nums (array) Output: O(logn)時間內找到min數 (int)
# Method: 怎麼找到最小？：找到小群的最左邊。
#         不是同一群數字的話，要維護left, middle, right 三個變數，重點在middle是左群還是右群數字
#         nums = [5,1,2,3,4]
#                 l   m   r     => m<=r m是右群數字，m右邊都比m大，r=m

#         nums = [5,6,7,1,2]
#                 l   m   r     => m>r m是左群數字，l已經大於r了，l~m都不會是小的 l=m+1