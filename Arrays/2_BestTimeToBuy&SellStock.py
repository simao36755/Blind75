# Topics: Array, Dynamic Programming, Two Pointer

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low, current = 0, 1
        maxP = 0
        while current < len(prices):
            if prices[current] < prices[low]:
                low = current
            else:
                maxP = max(maxP, prices[current]-prices[low])
            current += 1
        
        return maxP



s = Solution()
prices = [7,1,5,3,6,4]
print(s.maxProfit(prices))

# Input: Stock Prices (Arrays) Output: Porfit (int)
# Method: 兩個指針，一個指著最低點、一個指著目前價錢 他會一直往後指到底。判斷正獲利、負獲利做不同事