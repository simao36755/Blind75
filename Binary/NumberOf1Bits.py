class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n % 2
            n = n // 2
        return count


s = Solution()
num = 11
print(s.hammingWeight(num))

# Input: num (int) Output: 這個num的二進制有幾個1 (int)
# Method: 1. n%2 取餘數0或1加入count
#         2. n = n floor division 2  (n/2取ceil商數)