# Time complexity: O(n)
# Space complexity: O(n)
from typing import List

class TestSolution:
  def containsDuplicate(self):
    solution = Solution()
    assert solution.containsDuplicate([1,2,3,1]) == True
    assert solution.containsDuplicate([1,2,3,4]) == False
    assert solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True


class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    tracker = set()
    for num in nums:
      if num in tracker:
        return True
      tracker.add(num)
    return False

TestSolution().containsDuplicate()
