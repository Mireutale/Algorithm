#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    """
    [설계]
    첫째 줄 : 수의 개수 N
    둘째 줄부터 N개의 줄에는 수가 주어짐.
    오름차순으로 정렬 프로그램
    시간제한 5초 메모리 제한 8MB

    메모리 제한 이슈가 제일 큼
    계수 정렬을 사용할 필요 있음 -> 수가 입력될 때, 리스트의 번호에 맞는 값에
    1씩 추가해서 수를 체크하고 순서대로 출력 -> 오름차순 해결
    """
    count_of_number = int(input())
    nums = [0] * 10001
    for _ in range(count_of_number):
        nums[int(input())] += 1
    
    for i in range(len(nums)):
        if nums[i] != 0:
            for _ in range(nums[i]):
                print(i)