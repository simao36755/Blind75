# Topics: Array, Two Pointer, Greedy
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0, len(height) - 1
        maxArea = 0

        while l < r:
            area = (r-l) * min(height[l], height[r])
            maxArea = max(maxArea, area)
            
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1

        return maxArea


s = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(s.maxArea(height))

# Input: height nums (array) Output: max container (int)
# Methods: 用greedy方式，一開始選在左右兩邊柱子(寬度最寬)假設能裝最多水，每次把短的柱子換掉內縮
# [1,8,6,2,5,4,8,3,7]
#  L               R    => 8*1 = 8
#    L             R    => 7*7 = 49
#    L           R      => 6*3 = 18
#    L         R        => 5*8 = 40
#    L       R          => 4*4 = 16
#    L     R            => 3*5 = 15
#   ...