"""
Problem/LeetCode/Q9_PalindromeNumber/Python/Q9_v1.py
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        if x == 0:
            return True
        
        ary = list()
        while x > 0:
            ary.append(x % 10)
            x //= 10

        if ary == list(reversed(ary)):
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
