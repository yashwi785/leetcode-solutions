# Problem: 1. Two Sum (Easy)
# Link: https://leetcode.com/problems/two-sum/
# Approach: single pass, hash map of value -> index
# Time: O(n)  Space: O(n)
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index
        for index, value in enumerate(nums):
            needed = target - value
            if needed in seen:
                return [seen[needed], index]
            seen[value] = index
        return []


if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))
