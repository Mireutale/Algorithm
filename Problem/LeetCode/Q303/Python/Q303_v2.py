# v1에 비해서, prefix는 미리 첫번째 원소부터 합을 정리해놓고 사용하기 때문에, 반복되는 계산이 필요가 없음.
class NumArray:
    def __init__(self, nums: list[int]):
        self.prefix = [0]

        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]
