# 백준 1182번 - 부분 수열의 합

[문제 보러 가기](https://www.acmicpc.net/problem/1182)

## 요약

> N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서  
> 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

## 핵심 규칙

> 입력
>
> > 첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 20, |S| ≤ 1,000,000)
> > 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다.
> > 주어지는 정수의 절댓값은 100,000을 넘지 않는다.

> 출력
>
> > 첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.

## 예제 입출력

입력 및 출력 예시는 [문제 링크](https://www.acmicpc.net/problem/1182) 참고.

### 문제풀이

```Text
5 0
-7 -3 -2 5 8
```

위 입력의 결과로 나오는 출력은 1 이다.

백 트래킹을 수행하면서 모든 부분 수열에 대해 s와 동일한지 확인
-> 만약 동일 한 값이 있으면 ans에 추가

`1.첫번째 풀이`

이전에 푼 N과 M(12)번 처럼, used 값과 set을 활용해서 풀 생각이였다..

사실 푸는데는 문제가 없음 그러나 너무 코드가 길어지는 것 같아 다른 방식을 생각

`2. 문제점`

첫번째로는 다음에 사용할 수 있는 리스트를 전달하는 방식이였는데, 리스트를 슬라이싱 하려고 하니
계속해서 복사하고 전달하는 과정에서 시간 소모가 너무 많았다.

```Python
"""다음에 들어갈 수 있는 리스트를 추가 : 시간초과"""
    def back_tracking(num):
    global ans
    if len(sub_num) > 0 and sum(sub_num) == s:
        ans += 1
        return
    else:
        for i in num:
            if i not in sub_num:
                sub_num.append(i)
                back_tracking(num[i:])
                sub_num.pop()

if __name__ == "__main__":
    n, s = map(int, input().split())
    num = list(map(int, input().split()))
    sub_num = []
    back_tracking(num)
    print(ans)
```

다음번 풀이에서는 start 원소의 위치를 지정해서 전달하면, 만약 0번째 원소를 이미 사용한 경우 더 이상 부분 집합에 들어가지 않으므로
다음 start를 현재 + 1의 형태로 전달해주면 되었는데, return값의 문제가 있었다..

부분 수열의 합이 -2 -3 5로 0이 만들어지는 예시를 보면, 추후에 1 -2 1이 들어와서 만들어지는 부분수열 -2 -3 5 1 -2 1이전 -2 -3 5에서 return이 되어버리는 문제가 있었다..

추가적으로 잘못된 점!!

부분 수열의 길이가 0보다 크고, 합이 s와 같은 경우 ans에 값을 추가하지만, else문을 넣어서 아래 반복문이 진행되지 않도록 했다...

즉, 중간 부분 수열을 찾으면 그 다음 부분 수열들은 else에 걸려서 전부 죽어버리는 것..

```Python
"""
* CodingTest/Barkingdog/12.백트래킹/BOJ_1182/1182_부분수열의 합.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

ans = 0

if __name__ == "__main__":
    n, s = map(int, input().split())
    num = list(map(int, input().split()))
    sub_num = []

    def back_tracking(start):
        global ans
        if sum(sub_num) == s and len(sub_num) > 0:
            ans += 1
        """아래 두개 사용 금지!!!!"""
            # ! return
        # !else:
        for i in range(start, n):
            sub_num.append(num[i])
            back_tracking(i+1)
            sub_num.pop()

    back_tracking(0)
    print(ans)
```
