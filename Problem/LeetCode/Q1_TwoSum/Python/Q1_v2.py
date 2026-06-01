"""
Problem/LeetCode/1_TwoSum/1_TwoSum_v2.py

시간적 이익을 위한 딕셔너리 생성, 해당 딕셔너리에서 값을 O(n)으로 찾음
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map: dict[int, int] = {}
        
        for idx in range(len(nums)):
            num = nums[idx]
            diff = target - num

            if diff in diff_map:
                return [diff_map[diff], idx]
            
            diff_map[num] = idx
        
        return []

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
