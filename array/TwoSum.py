# Time complexity: O(n)
# Space complexity: O(n)
from typing import List

class TestSolution:
  def twoSum(self):
    solution= Solution()
    assert solution.twoSum([2,7,11,15], 9) == (0,1)
    assert solution.twoSum([3,2,4], 6) == (1,2)
    assert solution.twoSum([3,3], 6) == (0,1) 

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen_hash = {}
    for index, value in enumerate(nums):
      if target - value in seen_hash:
        return seen_hash[target - value], index
      seen_hash[value] = index


TestSolution().twoSum()
