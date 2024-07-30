# Topics: Dynamic Programming
class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1
        ways = 0
        for i in range(n-1):
            ways = a+b
            a = b
            b = ways
        return ways



s = Solution()
n = 5
print(s.climbStairs(n))

# Input: num (int) Output: ways (int) 從平地每次走 1 or 2 階梯，有幾種方式可以走到第n階梯
# Methods: 用DP方式，記住有幾種走法
# 1.DP方式：把大問題變小問題，儲存小問題的解，再解大問題     2.DFS方式：會有重複計算的問題

# Example: n = 5階，用DP解                                                                        Bottom-Up
#                                0階                                0走到5階，有幾種方法        ^     8
#            (+1)        /                 \        (+2)            1走到5階，有幾種方法        |     5
#                       1                   2                =>     2走到5階，有幾種方法        |     3
#                   /       \           /       \                   3走到5階，有幾種方法        |     2
#                  2         3         3         4                  4走到5階，有幾種方法        |     1
#                /   \     /   \     /   \     /                    base case 1種方法         |     1
#               3     4   4     5   4     5   5
#              / \   /   /         /
#             4   5 5   5         5
#            /
#           5