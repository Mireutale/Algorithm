"""
Problem/LeetCode/Q9_PalindromeNumber/Python/Q9_v2.py

while문을 활용하면, 정수 x를 분해하는데 시간이 오래 걸림 문자열로 바꿔서 처리하는게 빠르다.
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_string = str(x)
        if x_string == x_string[::-1]:
            return True
        else:
            return False

def main() -> None:
    solution = Solution()

    example1 = solution.isPalindrome(121)
    example2 = solution.isPalindrome(-121)
    example3 = solution.isPalindrome(10)

    print(f"Example 1: {example1}")
    print(f"Example 2: {example2}")
    print(f"Example 3: {example3}")

if __name__ == "__main__":
    main()
