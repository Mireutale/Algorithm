"""
Problem/LeetCode/Q3898_FindTheDegreeOfEachVertex/Python/Q3898_v1.py

간선은 정점에 연결된 간선의 개수이고, 1인 경우 간선이 있다고 나타냄
"""
from typing import List

class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        degree = []
        for i in range(len(matrix)):
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
