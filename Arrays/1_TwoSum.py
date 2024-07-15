# Topics:  Array, HashMap

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMaps = dict()
        for idx, val in enumerate(nums):
            diff = target-val
            if diff in prevMaps:
                return [prevMaps[diff], idx]
            else:
                prevMaps[val] = idx


s = Solution()

nums = [2,7,11,15]
target = 9
print(s.twoSum(nums, target))


# Input: Arrays, Output: List
# Method: enum遍歷並且跟target比較 就能找到2個index