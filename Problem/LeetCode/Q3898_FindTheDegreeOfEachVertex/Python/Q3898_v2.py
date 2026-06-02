"""
Problem/LeetCode/Q3898_FindTheDegreeOfEachVertex/Python/Q3898_v2.py

n을 따로 설정함, 하지만 실제로 시간의 차이는 없음
"""
from typing import List

class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        degree = []
        for i in range(n):
            degree.append(sum(matrix[i]))

        return degree

def main() -> None:
    solution = Solution()

    example1 = solution.findDegrees([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    example2 = solution.findDegrees([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
    example3 = solution.findDegrees([[0]])

    print(f"Example 1: {example1}")
    print(f"Example 2: {example2}")
    print(f"Example 3: {example3}")


if __name__ == "__main__":
    main()
