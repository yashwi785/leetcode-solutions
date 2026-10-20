# Problem: 9. Palindrome Number (Easy)
# Link: https://leetcode.com/problems/palindrome-number/
# Approach: convert to string, reverse with [::-1], compare
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            reverseofx =str(x)[::-1]
            if reverseofx==str(x):
                return True
            else:
                return False   
        