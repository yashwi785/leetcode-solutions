# Problem: 344. Reverse String (Easy)
# Link: https://leetcode.com/problems/reverse-string/
# Approach: two pointers, swap first and last, move inward
# Time: O(n)  Space: O(1)
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1         # index of the last item
        while left < right:
            s[left], s[right] = s[right], s[left]   # swap the two items
            left = left +1     # move inward
            right = right -1     # move inward
        