# Problem: 9. Palindrome Number (Easy)
# Link: https://leetcode.com/problems/palindrome-number/
# Approach: convert to string, reverse with [::-1], compare
# Time: O(n)  Space: O(n)


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        text = str(x)
        return text == text[::-1]


if __name__ == "__main__":
    print(Solution().isPalindrome(121))
