"""
Problem/LeetCode/Q9_PalindromeNumber/Python/Q9_v3.py

return을 바로 s[::-1] == s의 형태로 처리, 결과가 bool 값이므로 가능
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s[::-1] == s

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
