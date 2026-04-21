# 문제설명

시간제한 0.25초, 메모리 512MB

수빈이와 동생 위치, N, K (0 ~ N, K ~ 500,000)

X위치에서
걷는다면 1초후 +1, -1  
순간이동 1초후 2*X
동생은 항상 걷는다, 이동은 가속이 붙으며  
이전 이동한 거리보다 1을 더한 만큼 이동한다.

동생을 찾는 가장 빠른 시간을 출력한다.

17 5에서 4초후에 방문이 가능해야 한다.

4초후 동생의 위치는 5 + 1 + 2 + 3 + 4 = 15이다.
17에서 15로 4초후에 이동하려면?  
-1 3번, +1 1번이 수행되어야 한다.  
즉, 이전에 도착한 자리를 다시 위치해야한다.  
그러면? 모든 자리를 중복 탐색을 수행할 것인가? -> 시간초과가 날게 분명하다.(0.25s)

## 문제풀이 1
    2초후에 15로 이동이 가능하다
    0초 1초 3초에서는 불가능
    4초에서는 다시 15에 위치할 수 있다.
    이게 무슨 뜻이냐면, 현재 위치한 자리는 +2초후에 다시 위치할 수 있다는 뜻.
    그래서 visited에 처음 자리에 도착한 시간을 정하자.
    1초마다 visitied를 변경하고, detination의 visited값이 맞는지 확인해보자
    만약 destination의 visited값이 변화해 있고, 차가 2의 배수인 경우 도달 가능한지 보자
## 문제풀이 1의 코드
```
"""
* Codes/0x09 BFS/BOJ_2206/2206_벽부수고이동하기.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def bfs(k, queue):
    next_queue = deque()
    time = 0
    destination = k
    while True:
        destination += time
        if destination > 500000:
            return print(-1)
        while queue:
            x = queue.popleft()
            if visited[destination] != -1:
                # * visited[destination]이 0이 아닌 경우
                if (time - visited[destination]) % 2 == 0:
                    return print(time)
            else:
                for nx in (x*2, x+1, x-1):
                    if 0 <= nx <= 500000 and visited[nx] == -1:
                        next_queue.append(nx)
                        visited[nx] = time + 1
        time += 1
        next_queue, queue = queue, next_queue

if __name__ == "__main__":
    n, k = map(int, input().split())
    # * 방문한 시간을 저장
    visited = [-1] * 500001
    queue = deque()
    queue.append(n)
    visited[n] = 0
    bfs(k, queue)
```

## 문제풀이 2
    반례가 많다..
    7 37 5 -> 7 -> 14(1초) -> 28(2초) -> 27(3초) -> 26(4초) -> 52(5초)

    10 57 5 -> 10 -> 20 -> 19 -> 18 -> 36 -> 72

    21 70 4 -> 21(0초) -> 42(1초) -> 41(2초) -> 40(3초) -> 80(4초)

    18 58 4 -> 18 -> 36 -> 35 -> 34 -> 68

    18 66 4 -> 18 -> 36 -> 37 -> 38 -> 76

    16 50 4 -> 16 -> 32 -> 31 -> 30 -> 60
        
    34 0 8 ->
    경로 1: 34 -> 35 -> 36 -> 37 -> 36
    경로 2: 34 -> 35 -> 36 -> 35 -> 36
    경로 3: 34 -> 35 -> 34 -> 35 -> 36
    경로 4: 34 -> 33 -> 34 -> 35 -> 36
    그러나 모든 경로가 -1로 처리된다... 어째서?
    
    내 코드 수행 결과 N, K = 21 70, ans : 4

    정답 루트 21(0초) -> 42(1초) -> 41(2초) -> 40(3초) -> 80(4초)
    21 - 70
    42, 22, 20 - 70 + 1
    84, 43, 41, 44, 23, 40, 19 - 70 + 1 + 2
    168, 85, 83, 86, 82, 88, 45, 46, 24, 80, 39, 38, 18 - 70 + 1 + 2 + 3
    [여기서 문제점 발생]
    3초에서 40으로 이동을 해야 다음 상황에 80에 도달이 가능하다.
    그러나, 이미 40을 2초에 위치하고, 80을 3초에 위치하기 때문에
    4초인 상황에서 visited[80]의 값은 3으로 되어 있지만 time - 3의 값은 1이 되어 버리고, 정답을 구할 수 없게 되어 버린다.

    해결방법 -> 짝수와 홀수의 visited를 나누자
    그러면 2초에 40에 위치한 경우와 3초에 40에 위치한 경우 두개를 나누고
    4초에 80에 위치가 가능한 경우는 2초에서 80에 위치한 경우 또는
    3초에서 40, 81, 79에 위치한 경우를 찾으면 된다

"""

## 문제풀이 2의 코드
```
"""
* Codes/0x09 BFS/BOJ_2206/2206_벽부수고이동하기.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def find_destination(time, destination, even_or_odd):
    # * -1, +1의 형태로 순환해서 현재 값이 얻어지는지 확인
    if visited[destination][even_or_odd] != -1:
        # * visited[destination]이 0이 아닌 경우
        if (time - visited[destination][even_or_odd]) % 2 == 0:
            print(time)
            exit()
    
    for delta in (destination // 2, destination - 1, destination + 1):
        if 0 <= delta <= 500000 and visited[delta][even_or_odd-1] != -1:
            print(time)
            exit()

def bfs(k, queue):
    next_queue = deque()
    time = 0
    destination = k
    while True:
        if time % 2 == 0:
            even_or_odd = 0
        else:
            even_or_odd = 1
        while queue:
            x = queue.popleft()
            for nx in (x*2, x+1, x-1):
                if 0 <= nx <= 500000 and visited[nx][even_or_odd] == -1:
                    next_queue.append(nx)
                    visited[nx][even_or_odd] = time + 1
        time += 1
        destination = k + time * (time + 1) // 2
        if destination > 500000:
            return print(-1)
        next_queue, queue = queue, next_queue
        find_destination(time, destination, even_or_odd)

if __name__ == "__main__":
    n, k = map(int, input().split())
    # * 방문한 시간을 저장
    visited = [[-1, -1] for _ in range(500001)]
    queue = deque()
    queue.append(n)
    # * 처음 위치한 경우의 시간 [짝수 시간대, 홀수 시간대]
    visited[n] = [0, -1]
    bfs(k, queue)

# commit msg
# --- 문제풀이_mireutale[25/ / ]
```

## 문제풀이 3
438 129118를 입력시  
95가 출력되어야 하지만 93이 출력됨 -> 로직이 잘못되었다.
결국에 다시 로직을 만들기로 함.

먼저 기본틀은 visited를 짝수와 홀수로 설정해서 계산하는 것.  
여기서, destination을 k + time * (time + 1) // 2의 형태로  
등차수열을 사용할 것.

queue를 사용해서, 1초 후에 도달 가능한 위치를 모두 파악하고 그 상황에  
destination에 도달 가능한지 판단을 할 것

even_or_odd 말고, time을 사용해서 수행하자
even인 경우는 time % 2를 사용하면 0, odd인 경우는 time % 2가 1이 되기 때문이다.