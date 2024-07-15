# Topics: Array, HashTable, Sorting
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            else:
                hashset.add(i)
        return False

s = Solution()
nums = [1,2,3,1]
print(s.containsDuplicate(nums))



# Input: nums (array) Output: (bool)
# Method: 遍歷nums，把沒出現過在set中的數字加入set，有出現過直接回傳