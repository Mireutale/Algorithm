"""
Problem/LeetCode/Q1_TwoSum/Python/Q1_v1.py

이중 for문을 활용한 완전 탐색
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

def main() -> None:
    solution = Solution()

    example1 = solution.twoSum([2, 7, 11, 15], 9)
    example2 = solution.twoSum([3, 2, 4], 6)
    example3 = solution.twoSum([3, 3], 6)

    print(f"Example 1: {example1}")
    print(f"Example 2: {example2}")
    print(f"Example 3: {example3}")


if __name__ == "__main__":
    main()
