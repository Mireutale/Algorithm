#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
input = lambda: sys.stdin.readline().rstrip()
 
"""
[설계]

stack은 자료를 넣는 입구와 출구가 같은 LIFO

1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓아서 하나의 수열을
만들 수 있다.
스택에 push하는 순서는 반드시 오름차순을 지킨다.

임의의 수열이 주어진 경우, 스택을 이용해 그 수열을 만들 수 있는지
없는지 판단하고, 있다면 어떤 순서로 push와 pop을 수행해야하는지 계산

n (1  ~ 100,000), 둘째 줄 부터 n개의 줄에는 수열을 이루는 정수가 주어짐

불가능한 수열 조건
i번째 수열의 값보다 i+1번째 수열의 값이 2이상 차이가 나는 경우
1 ~ i-1의 값 중에 i와 i+1번째 값이 없으면 불가능
"""

if __name__ == "__main__":
    n = int(input())
    stack, ans = [], []
    input_nums = 1
    sequence = True
    for i in range(n):
        data = int(input())
        while data >= input_nums:
            stack.append(input_nums)
            ans.append("+")
            input_nums += 1
        if stack[-1] == data:
            stack.pop()
            ans.append("-")
        else:
            sequence = False

    if sequence:
        for i in ans:
            print(i)
    else:
        print("NO") 
