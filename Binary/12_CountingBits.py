# Topics: Dynamic programming
from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]
        offset = 1

        for i in range(1, n+1, 1):
            if i == offset * 2:
                offset = i
            dp.append(1 + dp[i - offset])

        return dp


s = Solution()
n = 8
print(s.countBits(n))

# Input: num (int) Output: List int (array) n的這個數字從0~n 每個數字的binary總共有幾個1
# Method: 用DP的方式記住已經算過的資訊，列出每個數字的binay找規律，1 + dp[ i - offset]
# n = 8
#     i          offset (如果offset*2 == i 代表偏移量要改)
#     0 - 0000      1                            dp[0]
#     1 - 0001      1                            1 + dp[i - offset]
#     2 - 001 0     2                            1 + dp[i - offset]
#     3 - 001 1     2                            類推...
#     4 - 01 00     4
#     5 - 01 01     4
#     6 - 01 10     4
#     7 - 01 11     4
#     8 - 1 000     8
