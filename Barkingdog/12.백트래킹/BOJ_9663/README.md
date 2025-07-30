## 백준 9663번 - N-Queen

[문제 보러 가기](https://www.acmicpc.net/problem/9663)

## 요약

> 크기가 $N \times N$인 체스판 위에 퀸 $N$개를 서로 공격할 수 없게 놓는 문제이다.
> $N$이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

## 핵심 규칙

> 입력
>
> > 첫째줄에 N이 주어진다.(1 ≤ N < 15)
>
> 출력
>
> > 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

## 예제 입출력

입력 및 출력 예시는 [문제 링크](https://www.acmicpc.net/problem/9663) 참고.

### 문제풀이

`1. 관찰`
퀸은 가로, 세로, 대각선을 공격할 수 있는 기물이므로, 하나의 가로 줄, 하나의 세로줄에는 반드시 퀸 1개만이 올 수 있다.

$N \times N$의 체스판에 $N$개의 퀸을 위치시키려면 한 줄당 1개의 퀸이 위치해야 한다.

이중 for 문을 활용해서 퀸을 놓아보자, 만약 1쌍의 퀸이라도 서로 공격당하게 되는 위치에 존재하게 된다면, 백 트래킹을 수행

여왕에게 공격받을 수 있는 위치를 잘 지정해야 하는데, 현재 여왕의 위치를 queen_row, queen_col이라고 하면 내가 놓을 말의 위치가 row, col일때 row가 queen_row와 같거나, col이 queen_col과 같으면 안된다.

위의 방법으로 직선은 문제를 해결

`! 대각선`

대각선을 해결하는 방법은?

두 점이 대각선이라고 한다면, abs(row - queen_row) == abs(col - queen_col)인 경우
x축의 거리와 y축의 거리가 동일하므로, 대각선에 위치함을 알 수 있다.

```Python
# 문제코드

import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def safe(row, col) -> bool:
    for queen_row, queen_col in queens:
        if col == queen_col:
            return True
        if abs(row - queen_row) == abs(col - queen_col):
            return True
    return False

def N_Queen(row):
    global ans
    if row == n:
        ans += 1
        return

    for i in range(n):
        attack_by_queen = safe(row, i)
        if not attack_by_queen:
            queens.append([row, i])
            N_Queen(row + 1)
            queens.pop()


if __name__ == "__main__":
    n = int(input())
    ans = 0
    queens = []
    N_Queen(0)
    print(ans)
```

`2. 시간초과`

map을 미리 지정하고, 사용 불가능한 위치를 미리 지정하자.

가능한 위치인지 아닌지 확인하는 과정에서, row는 무조건 True로 설정해야 한다.

```Python
# 문제코드 2

import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def cal_attacked(row, col):
    for i in range(n):
        attacked[row][i] += 1     # 행
        attacked[i][col] += 1     # 열

    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)] # 대각선
    for dx, dy in directions:
        r, c = row + dx, col + dy
        while 0 <= r < n and 0 <= c < n:
            attacked[r][c] += 1
            r += dx
            c += dy
    return False

def calBack_attacked(row, col):
    for i in range(n):
        attacked[row][i] -= 1     # 행
        attacked[i][col] -= 1     # 열

    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)] # 대각선
    for dx, dy in directions:
        r, c = row + dx, col + dy
        while 0 <= r < n and 0 <= c < n:
            attacked[r][c] -= 1
            r += dx
            c += dy
    return False

def N_Queen(row):
    global ans
    if row == n:
        ans += 1
        return

    for col in range(n):
        if not attacked[row][col]:
            queens.append([row, col])
            cal_attacked(row, col)
            N_Queen(row+1)
            calBack_attacked(row, col)
            queens.pop()


if __name__ == "__main__":
    n = int(input())
    ans = 0
    queens = []
    attacked = [[0] * n for _ in range(n)]
    N_Queen(0)
    print(ans)
```

변경했지만, 값을 추가하는 과정에서 for문을 또 돌기 때문에 시간 초과가 발생..
오히려 더 느려졌다..

`3.대각선만 체킹`
col은 어차피 계산을 할 수 있으므로, if문을 하나 추가해서 해보자..

queens의 원소의 개수는 현재까지 이동한 row의 개수와 같다.

즉, for i in range(len(queens))를 사용하면, i는 row와 같고, queens[i]는 col과 같아지는 것이다.

이렇게 하면 pypy3로는 통과가 된다.. 하지만 python3는 여전히 시간초과가 발생한다.

`4.Python으로 풀기`

퀸은 첫번째 row부터 배치할 것이기 때문에, 배치 후 오른쪽 아래 대각선과 왼쪽 아래 대각선의 경우만 True로 설정하면 된다.

$N \times N$의 크기의 배열에서 왼쪽 아래 또는 오른쪽 아래로 가능한 대각선의 개수는 총 $2N - 1$개가 된다.

따라서 오른쪽 아래, 왼쪽 아래 대각선을 $2N - 1$개로 설정하고, 같은 대각선에 있는 경우 또는 같은 열에 있는 경우를 제외하고 백트래킹을 수행하면 된다.

**대각선 표현**을 어떻게 수행할지 결정하는게 가장 어렵다....
