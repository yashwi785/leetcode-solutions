# Problem: 412. Fizz Buzz (Easy)
# Link: https://leetcode.com/problems/fizz-buzz/
# Approach: loop 1 to n; check "divisible by both" first, then 3, then 5
# Time: O(n)  Space: O(n)


class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        answer = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer


if __name__ == "__main__":
    print(Solution().fizzBuzz(15))
