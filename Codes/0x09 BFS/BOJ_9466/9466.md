
# [설계]

### 문제  
이번 가을학기에 '문제 해결' 강의를 신청한 학생들은 텀 프로젝트를 수행해야 한다. 프로젝트 팀원 수에는 제한이 없다. 심지어 모든 학생들이 동일한 팀의 팀원인 경우와 같이 한 팀만 있을 수도 있다. 프로젝트 팀을 구성하기 위해, 모든 학생들은 프로젝트를 함께하고 싶은 학생을 선택해야 한다. (단, 단 한 명만 선택할 수 있다.) 혼자 하고 싶어하는 학생은 자기 자신을 선택하는 것도 가능하다.

학생들이(s1, s2, ..., sr)이라 할 때, r=1이고 s1이 s1을 선택하는 경우나, s1이 s2를 선택하고, s2가 s3를 선택하고,..., sr-1이 sr을 선택하고, sr이 s1을 선택하는 경우에만 한 팀이 될 수 있다.

예를 들어, 한 반에 7명의 학생이 있다고 하자. 학생들을 1번부터 7번으로 표현할 때, 선택의 결과는 다음과 같다.

1	2	3	4	5	6	7
3	1	3	7	3	4	6
위의 결과를 통해 (3)과 (4, 7, 6)이 팀을 이룰 수 있다. 1, 2, 5는 어느 팀에도 속하지 않는다.

주어진 선택의 결과를 보고 어느 프로젝트 팀에도 속하지 않는 학생들의 수를 계산하는 프로그램을 작성하라.

### 입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫 줄에는 학생의 수가 정수 n (2 ≤ n ≤ 100,000)으로 주어진다. 각 테스트 케이스의 둘째 줄에는 선택된 학생들의 번호가 주어진다. (모든 학생들은 1부터 n까지 번호가 부여된다.)

### 출력
각 테스트 케이스마다 한 줄에 출력하고, 각 줄에는 프로젝트 팀에 속하지 못한 학생들의 수를 나타내면 된다.

---

### 문제풀이
팀 프로젝트를 수행할 팀이 만들어지는 지 확인하려면?
모든 학생에 대해서 학생의 선택을 따라가서 학생 리스트를 만들고, 시작 학생으로 다시 돌아와  
팀이 만들어지는지 확인  
팀이 만들어진 경우, 팀으로 구성된 학생들을 리스트로 적용하고 선택에서 제외

### 시간초과
학생들을 찾아가는 도중에 사이클이 만들어지는지 확인하고, 미리 팀으로 구성하자
team_list에서 특정 부분부터 사이클이 발생하게 됨

```
"""
* Codes/0x09 BFS/BOJ_9466/9466_텀프로젝트.py
* Author : mireutale
"""


import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

if __name__ == "__main__":
    testcase_num = int(input())
    for _ in range(testcase_num):
        all_student_numbers = int(input())
        student_choose_list = list(map(int, input().split()))
        team_student = [False] * (all_student_numbers + 1)
        queue = deque()
        team_student_count = 0
        for i in range(all_student_numbers):
            team_list = deque()
            if not team_student[i+1]:
                team_list.append(i+1)
                queue.append([i+1, student_choose_list[i]])
                while queue:
                    student_num, student_choose = queue.popleft()
                    if student_choose == i + 1:
                        while team_list:
                            x = team_list.pop()
                            team_student[x] = True
                            team_student_count += 1
                    elif student_num == student_choose:
                        break
                    elif not team_student[student_choose] and student_choose not in team_list:
                        queue.append([student_choose, student_choose_list[student_choose-1]])
                        team_list.append(student_choose)
        print(all_student_numbers - team_student_count)
```

### 시간초과 문제2
여전히 해결되지 않음
while queue 부분이 문제가 있다고 생각.
새로운 방식 dfs
1번 학생을 방문 처리 및 팀 후보에 추가
1번 학생이 선택한 학생을 다시 dfs
- 이 중에서 만약 이전에 방문한 학생이면서 팀 후보에 있는 경우?
- 즉, 사이클이 발생한 경우 4 6 5 4 순으로 사이클이 생겨 팀이 된다면 4번 학생부터 5번학생까지는 팀에 추가해야 함

1번
1 → 3: 팀 [1, 3]
3 → 3: 팀 [3], 3은 이미 visited와 team에 있으므로 team[team.index(3):] = [3]을 팀으로 추가

2번
2 → 1: 팀 [], 2번의 경우 새로운 team []이 생성되고, 2번은 1번을 지목하지만, 1번은 이미 visited이므로 2번도 제외

3번
3번은 이미 1번에서 팀으로 확정

4번
4 → 7: 팀 [4, 7]
7 → 6: 팀 [4, 7, 6]
6 → 4: 팀 [4, 7, 6], team에 4가 포함되어 있고, 4는 이미 방문한 학생이므로 team으로 추가

5번
3번 이미 visited

6번 7번 모두 이미 visited로 해결

! slice를 사용하기 위해서 list로 team을 생성해야 함