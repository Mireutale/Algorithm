# 현대오토에버 Python 코딩테스트 준비 문제 모음

조사 기준일: **2026-10-22**

기존에 선정한 24문제에 공개 응시 후기에서 파악한 유형과 기초 보완 문제 33개를 추가했다. **총 57문제, 19개 유형**이며 백준 문제는 제외했다. 같은 유형 안에서는 Python 구현 기준으로 쉬운 순서로 배치했다.

## 1. 자료를 읽는 기준

- **공식 안내:** 회사의 채용 절차 안내. 알고리즘별 공식 출제 범위나 정답 해설은 확인하지 못했다.
- **후기 언급:** 실제 응시자가 자신의 풀이 또는 문제 성격을 설명한 내용. 공식 정답 알고리즘으로 확정한 것은 아니다.
- **후기 추정:** 작성자가 미해결·기억 불확실·다른 응시자의 의견임을 밝힌 내용.
- **사용자 제공:** 이전 대화에서 전달받은 아호–코라식, DP, TSP, 병렬 이분 탐색, 두 PQ 그리디, MST, 유니온 파인드, 문자열 분할. 이번 조사로 해당 유형 전체의 출제 연도·회차를 독립적으로 확인하지는 못했다.
- **기초 보완:** 후기와 기존 범위를 공부하기 위해 추가한 선행·응용 유형. 해당 문제나 세부 유형이 현대오토에버에 실제 출제되었다는 뜻은 아니다.

**아래 57문제는 모두 연습 문제이며, 현대오토에버 공식 기출로 확인된 문제 목록이 아니다.** 카카오 등 다른 출처의 공개 문제도 유형 연습을 위해 포함했다.

난이도는 플랫폼 공식 등급을 환산한 수치가 아니라 **입문 → 기초 → 중급 → 중상급 → 상급 → 최상급** 순의 예상 체감 난이도다. 동일 단계의 세부 순서는 개인차가 있다. 문제 링크와 설명은 확인했지만 Python 코드를 직접 제출해 통과를 검증한 목록은 아니다.

## 2. 과거·최근 응시 후기에서 확인한 내용

아래 표는 공개된 후기의 일부다. 모든 직무·회차를 포괄하지 않으며, 시험일과 게시일이 다른 경우 이를 구분했다.

| 시기 | 지원 구분·자료 | 언급된 유형 | 근거의 한계 |
|---|---|---|---|
| 2022-05-07 시험 | 신입 ICT 애플리케이션 개발·운영, [R1](https://reliablecho-programming.tistory.com/181) | 단순 구현, 순열·조합·부분집합, 문자열 구현·재귀 | 작성자가 조합 유형의 세부 기법과 재귀 사용 여부는 정확히 기억하지 못한다고 설명 |
| 2022-12-05 게시 | 개발·운영 경력, [R2](https://fire-programmer.tistory.com/146) | 구현 중심 | 특정 알고리즘명보다 구현에 가깝다는 개인 평가 |
| 2023-05-13 시험 | 웹 개발, [R3](https://ph-biginner.tistory.com/171) | 투 포인터, 문자열, 누적합 추정 | 누적합은 작성자도 물음표로 표현 |
| 2024-10 시험 | 직무 미명시, 2025-01-05 게시 결산의 현대오토에버 항목, [R4](https://kinggh.tistory.com/124) | 최소 도착 시간, 3차원 경로 탐색·BFS | 첫 문제는 DFS로 접근한 뒤 DP가 맞을 것 같다고 회고. 정답 검증 여부 불명 |
| 2024-11-02 시험 | 하반기, [R5](https://docsom.tistory.com/10) | 그리디, DFS | 작성자의 풀이 유형 설명이며 회사 해설은 아님 |
| 2025-02-08 게시 | 신입 지원 후기, [R6](https://nsbg.tistory.com/entry/후기-현대오토에버-코딩테스트HMAT) | BFS 접근, 백트래킹 추정 | 첫 문제 정답 여부를 확신하지 못했고, 둘째 문제는 미해결 |
| 2025-08-10 시험·게시 | 엔터프라이즈 직무, [R7](https://taetae99.tistory.com/66) | 최단 경로 + 추가 탐색/DP 추정, 위상정렬·재귀 추정 | 작성자가 두 문제 모두 미해결. 다익스트라+백트래킹, 플로이드–워셜+DP 등은 다른 응시자에게 들은 내용도 포함 |
| 2026-04-11 게시 | ACT·코딩테스트 후기, [R8](https://kingrang-e.tistory.com/60) | 특정 지점 경유 경로 탐색, 시뮬레이션 | 경로 문제는 BFS 풀이의 반례를 발견했다고 설명. 이를 단순 BFS 출제로 확정하면 안 됨 |

### 최근 정보와 플랫폼 설명 정정

- 이번 검색에서 **구체적인 유형을 읽을 수 있었던 가장 최근 응시 후기의 게시일은 2026-04-11**이다. 2026년 하반기·4분기의 구체적 출제 유형은 확인하지 못했다. 과거 목록을 최신 회차의 확정 범위로 해석하지 않는다.
- 앞선 대화에서 2025년 상반기 후기를 근거로 Softeer를 언급했지만, **2025-08-10 응시자는 프로그래머스에서 시험을 봤다고 기록했다.** 플랫폼은 회차별 응시 안내로 확인해야 한다. Softeer의 서비스 종료 여부 자체는 이 후기만으로 확정하지 않는다. [R7](https://taetae99.tistory.com/66)
- 회사 공식 안내는 직무에 따라 코딩테스트 또는 과제테스트를 운영한다고 설명한다. 특정 알고리즘 목록은 제공하지 않는다. 공식 페이지는 검색 결과에서 내용을 확인했으나 원문 직접 열기는 403으로 제한되었다. [현대오토에버 채용 절차](https://career.hyundai-autoever.com/ko/process1)
- 신입·경력·부트캠프·다른 현대차그룹 계열사의 시험을 섞어 출제 범위를 추정하지 않았다. Python 응시 가능 여부는 지원 직무의 모집요강과 응시 안내를 따른다.

## 3. 기존 목록에서 보완한 유형

| 추가·보완 유형 | 기존 목록의 빈 부분 | 근거·선정 이유 | 추가 문제 수 |
|---|---|---|---:|
| 구현·시뮬레이션·재귀 구현 | 문자열 분할 외 일반 구현 연습 부족 | R1·R2·R8의 구현·시뮬레이션 언급 | 3 |
| BFS·DFS·상태 공간 탐색 | 유니온 파인드와 MST만으로 탐색 연습을 대체하기 어려움 | R4·R5·R6. R8은 상태·조건 분석 필요성을 보여주는 사례 | 3 |
| 완전탐색·백트래킹 | 순열·조합, 탐색 후 상태 복구 연습 부족 | R1의 조합 탐색 언급, R6의 백트래킹 추정 | 3 |
| 다익스트라·최단 경로 + DP | MST와 최단 경로는 다른 목적 | R7의 추정 유형을 대비. 경유 조건 연습도 포함 | 4 |
| 플로이드–워셜·전이 폐쇄 | 모든 정점 쌍의 거리·도달 관계 연습 부족 | R7의 대안 풀이 추정에 대한 보완 | 3 |
| 투 포인터·슬라이딩 윈도우 | 연속 구간을 선형 시간으로 처리하는 연습 부족 | R3의 투 포인터 언급 | 3 |
| 누적합·차분 배열 | 구간 합·범위 갱신 연습 부족 | R3의 누적합 추정. 차분 배열은 응용 보완 | 3 |
| 일반 그리디 | 두 힙을 쓰지 않는 선택·구간·스택 그리디 부족 | R5의 그리디 언급 | 3 |
| 위상정렬·DAG DP | 선행 관계, 사이클 판별, 작업 완료 시간 연습 부족 | R7에서 언급된 추정 유형 | 3 |
| 일반 이분 탐색·매개변수 탐색 | 기존 병렬 이분 탐색에 앞선 기초 단계 부족 | **기초 보완. 이번 조사에서 특정 회차 출제로 확정하지 않음** | 3 |
| DP 세부 보완 | 기존 DP에 0/1 배낭·메모이제이션 탐색이 없음 | **기초 보완. 세부 유형의 실제 출제를 확정하지 않음** | 2 |
| **합계** | 기존 24문제에 추가 | 중복 없이 계산 | **33** |

## 4. 전체 연습 문제 57개

`기존`은 앞서 선정한 24문제, `추가`는 이번 조사 후 보완한 33문제다. 번호는 전체 식별용이며, 전체 난이도 순위는 아니다. 각 소제목 내부에서 쉬운 순서로 풀면 된다. 표의 문제명 링크는 해당 플랫폼의 공식 문제 원문이다.

### 4.1 문자열 분할 — 3문제

근거: 사용자 제공 범위. R1·R3에서도 문자열 처리를 언급하지만 동일한 분할 유형인지는 확인되지 않았다.

| 번호 | 구분 | 체감 난이도 | 문제 | 목표 풀이·핵심 |
|---:|---|---|---|---|
| 01 | 기존 | 입문 | [프로그래머스 140108 — 문자열 나누기](https://school.programmers.co.kr/learn/courses/30/lessons/140108) | 문자별 카운트와 분할 지점 |
| 02 | 기존 | 중급 | [프로그래머스 60057 — 문자열 압축](https://school.programmers.co.kr/learn/courses/30/lessons/60057) | 분할 단위 탐색, 연속 조각과 나머지 처리 |
| 03 | 기존 | 중급 | [LeetCode 139 — Word Break](https://leetcode.com/problems/word-break/) | 접두사 DP로 사전 단어 분할 가능 여부 판정 |

### 4.2 구현·시뮬레이션·재귀 구현 — 3문제

근거: R1·R2·R8. 괄호 변환은 재귀 구현 연습도 겸한다.

| 번호 | 구분 | 체감 난이도 | 문제 | 목표 풀이·핵심 |
|---:|---|---|---|---|
| 04 | 추가 | 기초 | [프로그래머스 67256 — 키패드 누르기](https://school.programmers.co.kr/learn/courses/30/lessons/67256) | 좌표·거리·손 위치 상태 갱신 |
| 05 | 추가 | 중급 | [프로그래머스 60058 — 괄호 변환](https://school.programmers.co.kr/learn/courses/30/lessons/60058) | 주어진 변환 규칙을 재귀로 구현 |
| 06 | 추가 | 상급 | [프로그래머스 60061 — 기둥과 보 설치](https://school.programmers.co.kr/learn/courses/30/lessons/60061) | 설치·삭제 후 불변 조건 검사와 롤백 |

### 4.3 BFS·DFS·상태 공간 탐색 — 3문제

근거: R4·R5·R6. BFS는 모든 이동 비용이 같을 때의 최단 거리부터 시작한다.

| 번호 | 구분 | 체감 난이도 | 문제 | 목표 풀이·핵심 |
|---:|---|---|---|---|
| 07 | 추가 | 기초 | [프로그래머스 43162 — 네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162) | BFS/DFS로 연결 요소 세기 |
| 08 | 추가 | 중급 | [프로그래머스 1844 — 게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844) | 격자 BFS, 방문 처리와 도달 불가 판정 |
| 09 | 추가 | 상급 | [프로그래머스 60063 — 블록 이동하기](https://school.programmers.co.kr/learn/courses/30/lessons/60063) | 로봇 위치·방향을 상태로 정의하고 이동·회전 BFS |

### 4.4 완전탐색·백트래킹 — 3문제

근거: R1의 순열·조합 계열 언급과 R6의 백트래킹 추정. 단순 순열 생성에서 조건 가지치기로 확장한다.

| 번호 | 구분 | 체감 난이도 | 문제 | 목표 풀이·핵심 |
|---:|---|---|---|---|
| 10 | 추가 | 중급 | [프로그래머스 42839 — 소수 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/42839) | 길이별 순열 생성, 중복 제거, 소수 판정 |
| 11 | 추가 | 중급 | [프로그래머스 87946 — 피로도](https://school.programmers.co.kr/learn/courses/30/lessons/87946) | 방문 순서 탐색과 진입 조건 가지치기 |
| 12 | 추가 | 중상급 | [프로그래머스 64064 — 불량 사용자](https://school.programmers.co.kr/learn/courses/30/lessons/64064) | 패턴별 후보 매칭, 사용 상태 복구, 집합 중복 제거 |

### 4.5 DP·배낭·메모이제이션 — 5문제

근거: 사용자 제공 범위, R4·R7의 DP 추정. 배낭과 행렬 경로 메모이제이션은 세부 패턴 보완용이다.

| 번호 | 구분 | 체감 난이도 | 문제 | 목표 풀이·핵심 |
|---:|---|---|---|---|
| 13 | 기존 | 기초 | [프로그래머스 43105 — 정수 삼각형](https://school.programmers.co.kr/learn/courses/30/lessons/43105) | 위치별 최댓값 전이 |
| 14 | 기존 | 기초 | [프로그래머스 42898 — 등굣길](https://school.programmers.co.kr/learn/courses/30/lessons/42898) | 격자 DP, 장애물·초기값·나머지 연산 |
| 15 | 추가 | 중급 | [AtCoder DP D — Knapsack 1](https://atcoder.jp/contests/dp/tasks/dp_d?lang=en) | 0/1 배낭, 무게 상태, 1차원 역순 갱신 |
| 16 | 기존 | 중상급 | [프로그래머스 42895 — N으로 표현](https://school.programmers.co.kr/learn/courses/30/lessons/42895) | 사용 횟수별 가능한 값 집합 합성 |
| 17 | 추가 | 상급 | [LeetCode 329 — Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | DFS+메모이제이션 또는 위상정렬. 증가 조건으로 DAG 구성 |

### 4.6 투 포인터·슬라이딩 윈도우 — 3문제

근거: R3. 구간에 들어오고 나가는 원소의 정보를 갱신한다.

| 번호 | 구분 | 체감 난이도 | 문제 | 목표 풀이·핵심 |
|---:|---|---|---|---|
| 18 | 추가 | 중급 | [프로그래머스 178870 — 연속된 부분 수열의 합](https://school.programmers.co.kr/learn/courses/30/lessons/178870) | 양수 수열의 구간 합, 최단 길이·시작점 동률 처리 |
| 19 | 추가 | 중상급 | [프로그래머스 67258 — 보석 쇼핑](https://school.programmers.co.kr/learn/courses/30/lessons/67258) | 빈도 딕셔너리로 모든 종류를 포함하는 최소 구간 |
| 20 | 추가 | 상급 | [LeetCode 76 — Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | 필요한 문자별 개수와 중복 조건을 만족하는 최소 구간 |

### 4.7 누적합·차분 배열 — 3문제

근거: R3에서 누적합을 추정으로 언급. 2차원 차분 배열은 연관 응용 문제로 추가했다.

| 번호 | 구분 | 체감 난이도 | 문제 | 목표 풀이·핵심 |
|---:|---|---|---|---|
| 21 | 추가 | 기초 | [LeetCode 303 — Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) | 1차원 누적합으로 구간 합 계산 |
| 22 | 추가 | 중급 | [LeetCode 304 — Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) | 2차원 누적합과 포함·배제 |
| 23 | 추가 | 상급 | [프로그래머스 92344 — 파괴되지 않은 건물](https://school.programmers.co.kr/learn/courses/30/lessons/92344) | 직사각형 차분 갱신 후 누적합 복원 |

### 4.8 일반 그리디 — 3문제

근거: R5. 두 힙 그리디와 별도로, 정렬·스택·구간 선택의 정당성을 설명하는 연습이다.

| 번호 | 구분 | 체감 난이도 | 문제 | 목표 풀이·핵심 |
|---:|---|---|---|---|
| 24 | 추가 | 중급 | [프로그래머스 42885 — 구명보트](https://school.programmers.co.kr/learn/courses/30/lessons/42885) | 정렬 후 가장 무거운 사람과 가벼운 사람의 짝 결정 |
| 25 | 추가 | 중급 | [프로그래머스 42884 — 단속카메라](https://school.programmers.co.kr/learn/courses/30/lessons/42884) | 구간 끝점 기준으로 최소 지점 선택 |
| 26 | 추가 | 중상급 | [프로그래머스 42883 — 큰 수 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/42883) | 단조 스택으로 앞자리 선택, 남은 삭제 수 처리 |

### 4.9 힙·스케줄링·두 PQ 그리디 — 4문제

근거: 사용자 제공 범위. 디스크 컨트롤러는 두 힙 문제에 앞선 연습으로, 정렬+힙 하나로도 구현할 수 있다.

| 번호 | 구분 | 체감 난이도 | 문제 | 목표 풀이·핵심 |
|---:|---|---|---|---|
| 27 | 기존 | 중급 | [프로그래머스 42627 — 디스크 컨트롤러](https://school.programmers.co.kr/learn/courses/30/lessons/42627) | 도착 시각과 대기 작업 우선순위 분리 |
| 28 | 기존 | 중급 | [LeetCode 2462 — Total Cost to Hire K Workers](https://leetcode.com/problems/total-cost-to-hire-k-workers/) | 양쪽 후보 최소 힙, 후보 보충과 겹침 방지 |
| 29 | 기존 | 중상급 | [LeetCode 502 — IPO](https://leetcode.com/problems/ipo/) | 필요 자본 최소 힙→이익 최대 힙으로 후보 이동 |
| 30 | 기존 | 중상급 | [LeetCode 2402 — Meeting Rooms III](https://leetcode.com/problems/meeting-rooms-iii/) | 빈 방 번호·사용 중 종료 시각을 두 힙으로 관리 |

### 4.10 최소·최대 힙 동기화 — 1문제

근거: 힙 기초 보완. 최솟값·최댓값 삭제 자료구조이며, 후보 이동을 사용하는 두 PQ 그리디와는 다르다.

| 번호 | 구분 | 체감 난이도 | 문제 | 목표 풀이·핵심 |
|---:|---|---|---|---|
| 31 | 기존 | 중급 | [프로그래머스 42628 — 이중우선순위큐](https://school.programmers.co.kr/learn/courses/30/lessons/42628) | 최소·최대 힙과 유효 원소 상태 동기화 |

### 4.11 일반 이분 탐색·매개변수 탐색 — 3문제

근거: 병렬 이분 탐색에 앞선 **기초 보완**. 이번 조사에서 특정 현대오토에버 회차의 출제로 확정하지 않았다.

| 번호 | 구분 | 체감 난이도 | 문제 | 목표 풀이·핵심 |
|---:|---|---|---|---|
| 32 | 추가 | 기초 | [LeetCode 704 — Binary Search](https://leetcode.com/problems/binary-search/) | 탐색 구간과 종료 조건 |
| 33 | 추가 | 중급 | [프로그래머스 43238 — 입국심사](https://school.programmers.co.kr/learn/courses/30/lessons/43238) | 주어진 시간의 처리 가능 인원으로 단조 판정 |
| 34 | 추가 | 상급 | [프로그래머스 43236 — 징검다리](https://school.programmers.co.kr/learn/courses/30/lessons/43236) | 최소 간격을 답으로 탐색하고 제거 개수로 판정 |

### 4.12 다익스트라·최단 경로 + DP — 4문제

근거: R7의 추정 풀이와 R8의 경유 경로 언급을 대비한다. 최단 거리 계산과 그 결과를 사용하는 후처리를 분리하는 것이 목표다.

| 번호 | 구분 | 체감 난이도 | 문제 | 목표 풀이·핵심 |
|---:|---|---|---|---|
| 35 | 추가 | 중급 | [프로그래머스 12978 — 배달](https://school.programmers.co.kr/learn/courses/30/lessons/12978) | 단일 시작점 다익스트라, 중복 간선 |
| 36 | 추가 | 중상급 | [프로그래머스 72413 — 합승 택시 요금](https://school.programmers.co.kr/learn/courses/30/lessons/72413) | 세 시작점의 거리와 분기점 열거. 플로이드–워셜로도 재풀이 가능 |
| 37 | 추가 | 상급 | [프로그래머스 118669 — 등산코스 정하기](https://school.programmers.co.kr/learn/courses/30/lessons/118669) | 다중 시작점, 경로 합 대신 최대 간선 비용을 최소화 |
| 38 | 추가 | 상급 | [LeetCode 1786 — Number of Restricted Paths From First to Last Node](https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/) | 도착점에서 다익스트라→거리 감소 방향의 DAG에서 경로 수 DP |

### 4.13 플로이드–워셜·전이 폐쇄 — 3문제

근거: R7에서 대안 풀이로 거론된 **추정 유형**. 순위 문제는 최단 거리가 아닌 도달 관계를 전파하는 응용이다.

| 번호 | 구분 | 체감 난이도 | 문제 | 목표 풀이·핵심 |
|---:|---|---|---|---|
| 39 | 추가 | 중급 | [LeetCode 2976 — Minimum Cost to Convert String I](https://leetcode.com/problems/minimum-cost-to-convert-string-i/) | 알파벳 26개의 모든 쌍 최소 변환 비용 |
| 40 | 추가 | 중급 | [LeetCode 1334 — Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) | 모든 쌍 최단 거리와 거리 제한·동률 조건 |
| 41 | 추가 | 중상급 | [프로그래머스 49191 — 순위](https://school.programmers.co.kr/learn/courses/30/lessons/49191) | 승패의 전이 폐쇄와 순위 확정 조건 |

### 4.14 위상정렬·DAG DP — 3문제

근거: R7의 **미확정 추정 유형**. 대비 범위에 포함하되, 정답 알고리즘으로 확인된 기출이라고 표현하지 않는다.

| 번호 | 구분 | 체감 난이도 | 문제 | 목표 풀이·핵심 |
|---:|---|---|---|---|
| 42 | 추가 | 중급 | [LeetCode 207 — Course Schedule](https://leetcode.com/problems/course-schedule/) | 진입 차수와 사이클 유무 판정 |
| 43 | 추가 | 중급 | [LeetCode 210 — Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | 실제 위상 순서 복원 |
| 44 | 추가 | 상급 | [LeetCode 2050 — Parallel Courses III](https://leetcode.com/problems/parallel-courses-iii/) | 위상정렬 + 선행 작업 완료 시간의 최댓값 DP |

### 4.15 유니온 파인드 — 3문제

근거: 사용자 제공 범위. 일반적인 집합 병합에서 다음 빈 위치 탐색으로 확장한다.

| 번호 | 구분 | 체감 난이도 | 문제 | 목표 풀이·핵심 |
|---:|---|---|---|---|
| 45 | 기존 | 기초 | [LeetCode 684 — Redundant Connection](https://leetcode.com/problems/redundant-connection/) | 집합 병합과 사이클 판별 |
| 46 | 기존 | 중급 | [LeetCode 721 — Accounts Merge](https://leetcode.com/problems/accounts-merge/) | 이메일 키를 이용한 계정 그룹 병합 |
| 47 | 기존 | 중상급 | [프로그래머스 64063 — 호텔 방 배정](https://school.programmers.co.kr/learn/courses/30/lessons/64063) | 희소한 방 번호를 딕셔너리·경로 압축으로 처리 |

### 4.16 MST — 3문제

근거: 사용자 제공 범위. 그래프 전체 연결 비용 최소화 문제이며 최단 경로와 구분한다.

| 번호 | 구분 | 체감 난이도 | 문제 | 목표 풀이·핵심 |
|---:|---|---|---|---|
| 48 | 기존 | 중급 | [프로그래머스 42861 — 섬 연결하기](https://school.programmers.co.kr/learn/courses/30/lessons/42861) | 크루스칼과 유니온 파인드 |
| 49 | 기존 | 중급 | [LeetCode 1584 — Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | 맨해튼 거리 MST, 크루스칼·프림 비교 |
| 50 | 기존 | 상급 | [LeetCode 1489 — Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/) | 간선 제외·강제 포함 시 MST 비용 비교 |

### 4.17 외판원 순회(TSP) — 2문제

근거: 사용자 제공 범위. `dp[방문 집합][현재 위치]`를 직접 구현한다.

| 번호 | 구분 | 체감 난이도 | 문제 | 목표 풀이·핵심 |
|---:|---|---|---|---|
| 51 | 기존 | 상급 | [AtCoder ABC180 E — Traveling Salesman among Aerial Cities](https://atcoder.jp/contests/abc180/tasks/abc180_e?lang=en) | 방향별 비용, 비트마스크 DP, 출발점 복귀 |
| 52 | 기존 | 상급 | [AtCoder ABC274 E — Booster](https://atcoder.jp/contests/abc274/tasks/abc274_e?lang=en) | 필수·선택 방문 지점, 방문 집합에 따른 이동 속도 |

### 4.18 아호–코라식 — 3문제

근거: 사용자 제공 범위. 다른 해법이 있더라도 트라이·실패 링크를 이용하는 것을 연습 목표로 삼는다.

| 번호 | 구분 | 체감 난이도 | 문제 | 목표 풀이·핵심 |
|---:|---|---|---|---|
| 53 | 기존 | 상급 | [CSES 2102 — Finding Patterns](https://cses.fi/problemset/task/2102/) | 실패 링크와 패턴별 포함 여부 |
| 54 | 기존 | 상급 | [CSES 2103 — Counting Patterns](https://cses.fi/problemset/task/2103/) | 실패 링크 역순으로 등장 횟수 집계 |
| 55 | 기존 | 최상급 | [LeetCode 3213 — Construct String with Minimum Cost](https://leetcode.com/problems/construct-string-with-minimum-cost/) | 다중 패턴 매칭 결과를 최소 비용 DP와 결합 |

### 4.19 병렬 이분 탐색 — 2문제

근거: 사용자 제공 범위. 일반 이분 탐색·유니온 파인드를 먼저 익힌 뒤, 여러 쿼리의 판정 시점을 묶는 방식으로 푼다.

| 번호 | 구분 | 체감 난이도 | 문제 | 목표 풀이·핵심 |
|---:|---|---|---|---|
| 56 | 기존 | 최상급 | [CSES 2101 — New Roads Queries](https://cses.fi/problemset/task/2101/) | 날짜별 중간값 버킷, 간선 추가, 최초 연결 시점 |
| 57 | 기존 | 최상급 | [AtCoder AGC002 D — Stamp Rally](https://atcoder.jp/contests/agc002/tasks/agc002_d?lang=en) | 두 연결 요소의 합집합 크기 판정과 병렬 이분 탐색 |

## 5. 학습 순서와 실전 연습

이 순서는 출제 확률 통계가 아니라, 선수 지식과 공개 후기에서 보인 빈 부분을 고려한 학습 제안이다.

| 단계 | 공부할 유형 | 완료 기준 |
|---|---|---|
| 1 | 문자열·구현·기본 BFS/DFS·기본 DP | 문제 조건을 상태와 전이로 옮기고 작은 반례를 직접 만들기 |
| 2 | 백트래킹·투 포인터·누적합·일반 그리디 | 완전탐색의 비용을 추정하고 가지치기·선형 처리의 근거 설명 |
| 3 | 힙·이분 탐색·유니온 파인드·MST | 불변 조건과 동률·경계 조건을 실수 없이 구현 |
| 4 | 다익스트라·플로이드–워셜·위상정렬·메모이제이션 | 가중치·방향·상태를 구분하고 그래프+DP 결합 문제 풀기 |
| 5 | TSP·아호–코라식·병렬 이분 탐색 | 기본 구현 이후 시간·메모리 비용과 응용 상태 설계 검토 |

### 먼저 풀 15문제

1. 키패드 누르기 — 구현 상태 갱신
2. 게임 맵 최단거리 — 격자 BFS
3. 피로도 — 백트래킹
4. 정수 삼각형 — 기본 DP
5. Knapsack 1 — 0/1 배낭
6. 연속된 부분 수열의 합 — 투 포인터
7. Range Sum Query 2D - Immutable — 2차원 누적합
8. 단속카메라 — 구간 그리디
9. 디스크 컨트롤러 — 힙 스케줄링
10. 입국심사 — 매개변수 탐색
11. Redundant Connection — 유니온 파인드
12. 섬 연결하기 — MST
13. 합승 택시 요금 — 경유점과 최단 거리
14. Course Schedule II — 위상정렬
15. Number of Restricted Paths From First to Last Node — 최단 경로 + DP

### Python에서 확인할 것

- BFS는 `collections.deque`, 가중치가 있는 최단 경로는 조건에 맞는 알고리즘을 선택한다. 좌표가 같아도 방향·방문 상태가 다르면 다른 상태일 수 있다.
- 다익스트라는 오래된 힙 항목을 건너뛰고, 거리 합인지 최대 간선 비용인지 목적함수를 먼저 구분한다.
- DFS·메모이제이션은 최악의 재귀 깊이를 확인한다. 긴 경로가 가능하면 반복형 탐색이나 위상정렬을 검토한다.
- 투 포인터의 단조성이 성립하는지 확인한다. 양수 수열에서 가능한 이동 규칙을 음수가 섞인 수열에 그대로 적용하지 않는다.
- 그리디는 작은 입력을 완전탐색한 결과와 비교하고, 선택이 최적해를 유지하는 이유를 설명한다.
- TSP·아호–코라식·병렬 이분 탐색은 Python의 리스트·딕셔너리 객체 비용과 반복 횟수도 고려한다. 특히 CSES 문제는 제한을 읽고 구현·인터프리터 선택을 검토한다.
- 프로그래머스의 함수형 제출과 AtCoder·CSES의 표준입출력을 모두 연습한다. 실제 시험의 플랫폼·시간·허용 언어·참고 자료 범위는 해당 회차 안내를 따른다.

## 6. 출처와 확인 범위

아래는 출제 유형을 조사한 원문이다. 문제의 공식 원문은 4절의 각 링크를 사용한다.

| ID | 출처 | 확인한 핵심 |
|---|---|---|
| R1 | [2022 상반기 신입 합격 후기](https://reliablecho-programming.tistory.com/181), 2022-07-06 게시 | 2022-05-07 시험의 구현·조합 탐색·문자열 처리 |
| R2 | [경력 인적성·코딩테스트 후기](https://fire-programmer.tistory.com/146), 2022-12-05 게시 | 경력 시험의 구현 중심이라는 개인 평가 |
| R3 | [2023-05-13 코딩테스트 후기](https://ph-biginner.tistory.com/171) | 투 포인터·문자열, 누적합은 추정 |
| R4 | [2024 하반기 코딩테스트 결산](https://kinggh.tistory.com/124), 2025-01-05 게시 | 여러 기업 중 **현대오토에버 2024.10 항목만** 사용. BFS·경로 문제와 DP 추정 |
| R5 | [2024 하반기 현대오토에버 후기](https://docsom.tistory.com/10), 2024-11-10 게시 | 2024-11-02 시험의 그리디·DFS |
| R6 | [현대오토에버 코딩테스트·HMAT 후기](https://nsbg.tistory.com/entry/후기-현대오토에버-코딩테스트HMAT), 2025-02-08 게시 | BFS 접근과 백트래킹 추정. 정답 여부 불확실 |
| R7 | [2025 하반기 엔터프라이즈 코딩테스트 후기](https://taetae99.tistory.com/66), 2025-08-10 게시 | 프로그래머스 사용 경험, 최단 경로 복합 유형·위상정렬 등의 추정 |
| R8 | [ACT 합격 및 코딩테스트 회고](https://kingrang-e.tistory.com/60), 2026-04-11 게시 | 경유 경로에서 BFS 반례를 발견한 경험, 시뮬레이션 풀이 |
| O1 | [현대오토에버 공식 채용 절차](https://career.hyundai-autoever.com/ko/process1) | 직무별 코딩·과제테스트 안내. 검색 결과 확인, 원문 직접 열기는 403 제한 |

조사 범위의 한계: 공식 기출 원문·정답·연도별 전체 문제 목록은 확인하지 못했다. 후기의 접근 알고리즘은 정답 알고리즘과 다를 수 있다. 사용자에게 전달받은 고급 알고리즘 목록의 실제 회차를 추정해서 연도표에 넣지 않았다. 이 문서는 특정 유형의 재출제나 합격 기준을 보장하지 않는다.

## 7. 전체 57문제 권장 풀이 순서

아래 **풀이 순서 1~57**을 따라 진행한다. 같은 유형의 기본 문제를 먼저 풀고 응용 문제로 확장하며, 후반에 고급 알고리즘을 배치했다. 절대적인 난이도 순위보다 **선수 지식과 학습 흐름**을 우선한 순서다.

5절의 먼저 풀 15문제는 시간이 부족할 때의 압축 코스이고, 이 절은 전체를 공부할 때의 완주 코스다. `기존 번호`는 4절의 문제 번호이므로 상세 학습 목표를 찾아볼 때 사용한다. 각 문제명에 공식 문제 URL을 연결했다.

### 7.1 기본 구현·탐색·DP 익히기

| 풀이 순서 | 기존 번호 | 체감 난이도 | 문제 | 학습 목표 |
|---:|---:|---|---|---|
| 1 | 01 | 입문 | [프로그래머스 140108 — 문자열 나누기](https://school.programmers.co.kr/learn/courses/30/lessons/140108) | 문자별 카운트와 분할 지점 |
| 2 | 04 | 기초 | [프로그래머스 67256 — 키패드 누르기](https://school.programmers.co.kr/learn/courses/30/lessons/67256) | 좌표·거리·손 위치 상태 갱신 |
| 3 | 21 | 기초 | [LeetCode 303 — Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) | 1차원 누적합으로 구간 합 계산 |
| 4 | 32 | 기초 | [LeetCode 704 — Binary Search](https://leetcode.com/problems/binary-search/) | 탐색 구간과 종료 조건 |
| 5 | 07 | 기초 | [프로그래머스 43162 — 네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162) | BFS/DFS로 연결 요소 세기 |
| 6 | 08 | 중급 | [프로그래머스 1844 — 게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844) | 격자 BFS, 방문 처리와 도달 불가 판정 |
| 7 | 13 | 기초 | [프로그래머스 43105 — 정수 삼각형](https://school.programmers.co.kr/learn/courses/30/lessons/43105) | 위치별 최댓값 전이 |
| 8 | 14 | 기초 | [프로그래머스 42898 — 등굣길](https://school.programmers.co.kr/learn/courses/30/lessons/42898) | 격자 DP, 장애물·초기값·나머지 연산 |
| 9 | 10 | 중급 | [프로그래머스 42839 — 소수 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/42839) | 길이별 순열 생성, 중복 제거, 소수 판정 |
| 10 | 11 | 중급 | [프로그래머스 87946 — 피로도](https://school.programmers.co.kr/learn/courses/30/lessons/87946) | 방문 순서 탐색과 진입 조건 가지치기 |
| 11 | 05 | 중급 | [프로그래머스 60058 — 괄호 변환](https://school.programmers.co.kr/learn/courses/30/lessons/60058) | 주어진 변환 규칙을 재귀로 구현 |
| 12 | 02 | 중급 | [프로그래머스 60057 — 문자열 압축](https://school.programmers.co.kr/learn/courses/30/lessons/60057) | 분할 단위 탐색, 연속 조각과 나머지 처리 |

### 7.2 구간 처리·그리디·DP 응용

| 풀이 순서 | 기존 번호 | 체감 난이도 | 문제 | 학습 목표 |
|---:|---:|---|---|---|
| 13 | 18 | 중급 | [프로그래머스 178870 — 연속된 부분 수열의 합](https://school.programmers.co.kr/learn/courses/30/lessons/178870) | 양수 수열의 구간 합, 최단 길이·시작점 동률 처리 |
| 14 | 22 | 중급 | [LeetCode 304 — Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) | 2차원 누적합과 포함·배제 |
| 15 | 24 | 중급 | [프로그래머스 42885 — 구명보트](https://school.programmers.co.kr/learn/courses/30/lessons/42885) | 정렬 후 가장 무거운 사람과 가벼운 사람의 짝 결정 |
| 16 | 25 | 중급 | [프로그래머스 42884 — 단속카메라](https://school.programmers.co.kr/learn/courses/30/lessons/42884) | 구간 끝점 기준으로 최소 지점 선택 |
| 17 | 26 | 중상급 | [프로그래머스 42883 — 큰 수 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/42883) | 단조 스택으로 앞자리 선택, 남은 삭제 수 처리 |
| 18 | 19 | 중상급 | [프로그래머스 67258 — 보석 쇼핑](https://school.programmers.co.kr/learn/courses/30/lessons/67258) | 빈도 딕셔너리로 모든 종류를 포함하는 최소 구간 |
| 19 | 15 | 중급 | [AtCoder DP D — Knapsack 1](https://atcoder.jp/contests/dp/tasks/dp_d?lang=en) | 0/1 배낭, 무게 상태, 1차원 역순 갱신 |
| 20 | 03 | 중급 | [LeetCode 139 — Word Break](https://leetcode.com/problems/word-break/) | 접두사 DP로 사전 단어 분할 가능 여부 판정 |
| 21 | 16 | 중상급 | [프로그래머스 42895 — N으로 표현](https://school.programmers.co.kr/learn/courses/30/lessons/42895) | 사용 횟수별 가능한 값 집합 합성 |
| 22 | 12 | 중상급 | [프로그래머스 64064 — 불량 사용자](https://school.programmers.co.kr/learn/courses/30/lessons/64064) | 패턴별 후보 매칭, 사용 상태 복구, 집합 중복 제거 |

### 7.3 힙·이분 탐색·집합과 MST

| 풀이 순서 | 기존 번호 | 체감 난이도 | 문제 | 학습 목표 |
|---:|---:|---|---|---|
| 23 | 27 | 중급 | [프로그래머스 42627 — 디스크 컨트롤러](https://school.programmers.co.kr/learn/courses/30/lessons/42627) | 도착 시각과 대기 작업 우선순위 분리 |
| 24 | 28 | 중급 | [LeetCode 2462 — Total Cost to Hire K Workers](https://leetcode.com/problems/total-cost-to-hire-k-workers/) | 양쪽 후보 최소 힙, 후보 보충과 겹침 방지 |
| 25 | 31 | 중급 | [프로그래머스 42628 — 이중우선순위큐](https://school.programmers.co.kr/learn/courses/30/lessons/42628) | 최소·최대 힙과 유효 원소 상태 동기화 |
| 26 | 29 | 중상급 | [LeetCode 502 — IPO](https://leetcode.com/problems/ipo/) | 필요 자본 최소 힙→이익 최대 힙으로 후보 이동 |
| 27 | 30 | 중상급 | [LeetCode 2402 — Meeting Rooms III](https://leetcode.com/problems/meeting-rooms-iii/) | 빈 방 번호·사용 중 종료 시각을 두 힙으로 관리 |
| 28 | 33 | 중급 | [프로그래머스 43238 — 입국심사](https://school.programmers.co.kr/learn/courses/30/lessons/43238) | 주어진 시간의 처리 가능 인원으로 단조 판정 |
| 29 | 45 | 기초 | [LeetCode 684 — Redundant Connection](https://leetcode.com/problems/redundant-connection/) | 집합 병합과 사이클 판별 |
| 30 | 46 | 중급 | [LeetCode 721 — Accounts Merge](https://leetcode.com/problems/accounts-merge/) | 이메일 키를 이용한 계정 그룹 병합 |
| 31 | 47 | 중상급 | [프로그래머스 64063 — 호텔 방 배정](https://school.programmers.co.kr/learn/courses/30/lessons/64063) | 희소한 방 번호를 딕셔너리·경로 압축으로 처리 |
| 32 | 48 | 중급 | [프로그래머스 42861 — 섬 연결하기](https://school.programmers.co.kr/learn/courses/30/lessons/42861) | 크루스칼과 유니온 파인드 |
| 33 | 49 | 중급 | [LeetCode 1584 — Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | 맨해튼 거리 MST, 크루스칼·프림 비교 |

### 7.4 최단 경로·위상정렬·그래프 DP

| 풀이 순서 | 기존 번호 | 체감 난이도 | 문제 | 학습 목표 |
|---:|---:|---|---|---|
| 34 | 35 | 중급 | [프로그래머스 12978 — 배달](https://school.programmers.co.kr/learn/courses/30/lessons/12978) | 단일 시작점 다익스트라, 중복 간선 |
| 35 | 39 | 중급 | [LeetCode 2976 — Minimum Cost to Convert String I](https://leetcode.com/problems/minimum-cost-to-convert-string-i/) | 알파벳 26개의 모든 쌍 최소 변환 비용 |
| 36 | 40 | 중급 | [LeetCode 1334 — Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) | 모든 쌍 최단 거리와 거리 제한·동률 조건 |
| 37 | 41 | 중상급 | [프로그래머스 49191 — 순위](https://school.programmers.co.kr/learn/courses/30/lessons/49191) | 승패의 전이 폐쇄와 순위 확정 조건 |
| 38 | 36 | 중상급 | [프로그래머스 72413 — 합승 택시 요금](https://school.programmers.co.kr/learn/courses/30/lessons/72413) | 세 시작점의 거리와 분기점 열거. 플로이드–워셜로도 재풀이 가능 |
| 39 | 42 | 중급 | [LeetCode 207 — Course Schedule](https://leetcode.com/problems/course-schedule/) | 진입 차수와 사이클 유무 판정 |
| 40 | 43 | 중급 | [LeetCode 210 — Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | 실제 위상 순서 복원 |
| 41 | 44 | 상급 | [LeetCode 2050 — Parallel Courses III](https://leetcode.com/problems/parallel-courses-iii/) | 위상정렬 + 선행 작업 완료 시간의 최댓값 DP |
| 42 | 17 | 상급 | [LeetCode 329 — Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | DFS+메모이제이션 또는 위상정렬. 증가 조건으로 DAG 구성 |
| 43 | 38 | 상급 | [LeetCode 1786 — Number of Restricted Paths From First to Last Node](https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/) | 도착점에서 다익스트라→거리 감소 방향의 DAG에서 경로 수 DP |
| 44 | 37 | 상급 | [프로그래머스 118669 — 등산코스 정하기](https://school.programmers.co.kr/learn/courses/30/lessons/118669) | 다중 시작점, 경로 합 대신 최대 간선 비용을 최소화 |

### 7.5 복잡한 상태·구현·최적화 응용

| 풀이 순서 | 기존 번호 | 체감 난이도 | 문제 | 학습 목표 |
|---:|---:|---|---|---|
| 45 | 06 | 상급 | [프로그래머스 60061 — 기둥과 보 설치](https://school.programmers.co.kr/learn/courses/30/lessons/60061) | 설치·삭제 후 불변 조건 검사와 롤백 |
| 46 | 09 | 상급 | [프로그래머스 60063 — 블록 이동하기](https://school.programmers.co.kr/learn/courses/30/lessons/60063) | 로봇 위치·방향을 상태로 정의하고 이동·회전 BFS |
| 47 | 20 | 상급 | [LeetCode 76 — Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | 필요한 문자별 개수와 중복 조건을 만족하는 최소 구간 |
| 48 | 23 | 상급 | [프로그래머스 92344 — 파괴되지 않은 건물](https://school.programmers.co.kr/learn/courses/30/lessons/92344) | 직사각형 차분 갱신 후 누적합 복원 |
| 49 | 34 | 상급 | [프로그래머스 43236 — 징검다리](https://school.programmers.co.kr/learn/courses/30/lessons/43236) | 최소 간격을 답으로 탐색하고 제거 개수로 판정 |
| 50 | 50 | 상급 | [LeetCode 1489 — Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/) | 간선 제외·강제 포함 시 MST 비용 비교 |

### 7.6 고급 알고리즘과 복합 문제

| 풀이 순서 | 기존 번호 | 체감 난이도 | 문제 | 학습 목표 |
|---:|---:|---|---|---|
| 51 | 51 | 상급 | [AtCoder ABC180 E — Traveling Salesman among Aerial Cities](https://atcoder.jp/contests/abc180/tasks/abc180_e?lang=en) | 방향별 비용, 비트마스크 DP, 출발점 복귀 |
| 52 | 52 | 상급 | [AtCoder ABC274 E — Booster](https://atcoder.jp/contests/abc274/tasks/abc274_e?lang=en) | 필수·선택 방문 지점, 방문 집합에 따른 이동 속도 |
| 53 | 53 | 상급 | [CSES 2102 — Finding Patterns](https://cses.fi/problemset/task/2102/) | 실패 링크와 패턴별 포함 여부 |
| 54 | 54 | 상급 | [CSES 2103 — Counting Patterns](https://cses.fi/problemset/task/2103/) | 실패 링크 역순으로 등장 횟수 집계 |
| 55 | 55 | 최상급 | [LeetCode 3213 — Construct String with Minimum Cost](https://leetcode.com/problems/construct-string-with-minimum-cost/) | 다중 패턴 매칭 결과를 최소 비용 DP와 결합 |
| 56 | 56 | 최상급 | [CSES 2101 — New Roads Queries](https://cses.fi/problemset/task/2101/) | 날짜별 중간값 버킷, 간선 추가, 최초 연결 시점 |
| 57 | 57 | 최상급 | [AtCoder AGC002 D — Stamp Rally](https://atcoder.jp/contests/agc002/tasks/agc002_d?lang=en) | 두 연결 요소의 합집합 크기 판정과 병렬 이분 탐색 |

## 8. 프로그래머스 전용 30문제 권장 풀이 순서

7절에서 프로그래머스 문제만 추린 목록이다. 기존 학습 순서를 유지하고 풀이 순서를 1~30로 다시 매겼다. `기존 번호`는 4절의 문제 번호이며, 난이도·학습 목표·공식 문제 링크는 그대로 유지했다.

이 목록은 연습 문제 모음이며 공식 기출 목록이 아니다. 다른 플랫폼의 선행 문제를 제외했으므로 누적합·유니온 파인드 등의 기초 개념은 필요에 따라 별도로 보완한다.

| 풀이 순서 | 기존 번호 | 체감 난이도 | 문제 | 학습 목표 |
|---:|---:|---|---|---|
| 1 | 01 | 입문 | [프로그래머스 140108 — 문자열 나누기](https://school.programmers.co.kr/learn/courses/30/lessons/140108) | 문자별 카운트와 분할 지점 |
| 2 | 04 | 기초 | [프로그래머스 67256 — 키패드 누르기](https://school.programmers.co.kr/learn/courses/30/lessons/67256) | 좌표·거리·손 위치 상태 갱신 |
| 3 | 07 | 기초 | [프로그래머스 43162 — 네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162) | BFS/DFS로 연결 요소 세기 |
| 4 | 08 | 중급 | [프로그래머스 1844 — 게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844) | 격자 BFS, 방문 처리와 도달 불가 판정 |
| 5 | 13 | 기초 | [프로그래머스 43105 — 정수 삼각형](https://school.programmers.co.kr/learn/courses/30/lessons/43105) | 위치별 최댓값 전이 |
| 6 | 14 | 기초 | [프로그래머스 42898 — 등굣길](https://school.programmers.co.kr/learn/courses/30/lessons/42898) | 격자 DP, 장애물·초기값·나머지 연산 |
| 7 | 10 | 중급 | [프로그래머스 42839 — 소수 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/42839) | 길이별 순열 생성, 중복 제거, 소수 판정 |
| 8 | 11 | 중급 | [프로그래머스 87946 — 피로도](https://school.programmers.co.kr/learn/courses/30/lessons/87946) | 방문 순서 탐색과 진입 조건 가지치기 |
| 9 | 05 | 중급 | [프로그래머스 60058 — 괄호 변환](https://school.programmers.co.kr/learn/courses/30/lessons/60058) | 주어진 변환 규칙을 재귀로 구현 |
| 10 | 02 | 중급 | [프로그래머스 60057 — 문자열 압축](https://school.programmers.co.kr/learn/courses/30/lessons/60057) | 분할 단위 탐색, 연속 조각과 나머지 처리 |
| 11 | 18 | 중급 | [프로그래머스 178870 — 연속된 부분 수열의 합](https://school.programmers.co.kr/learn/courses/30/lessons/178870) | 양수 수열의 구간 합, 최단 길이·시작점 동률 처리 |
| 12 | 24 | 중급 | [프로그래머스 42885 — 구명보트](https://school.programmers.co.kr/learn/courses/30/lessons/42885) | 정렬 후 가장 무거운 사람과 가벼운 사람의 짝 결정 |
| 13 | 25 | 중급 | [프로그래머스 42884 — 단속카메라](https://school.programmers.co.kr/learn/courses/30/lessons/42884) | 구간 끝점 기준으로 최소 지점 선택 |
| 14 | 26 | 중상급 | [프로그래머스 42883 — 큰 수 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/42883) | 단조 스택으로 앞자리 선택, 남은 삭제 수 처리 |
| 15 | 19 | 중상급 | [프로그래머스 67258 — 보석 쇼핑](https://school.programmers.co.kr/learn/courses/30/lessons/67258) | 빈도 딕셔너리로 모든 종류를 포함하는 최소 구간 |
| 16 | 16 | 중상급 | [프로그래머스 42895 — N으로 표현](https://school.programmers.co.kr/learn/courses/30/lessons/42895) | 사용 횟수별 가능한 값 집합 합성 |
| 17 | 12 | 중상급 | [프로그래머스 64064 — 불량 사용자](https://school.programmers.co.kr/learn/courses/30/lessons/64064) | 패턴별 후보 매칭, 사용 상태 복구, 집합 중복 제거 |
| 18 | 27 | 중급 | [프로그래머스 42627 — 디스크 컨트롤러](https://school.programmers.co.kr/learn/courses/30/lessons/42627) | 도착 시각과 대기 작업 우선순위 분리 |
| 19 | 31 | 중급 | [프로그래머스 42628 — 이중우선순위큐](https://school.programmers.co.kr/learn/courses/30/lessons/42628) | 최소·최대 힙과 유효 원소 상태 동기화 |
| 20 | 33 | 중급 | [프로그래머스 43238 — 입국심사](https://school.programmers.co.kr/learn/courses/30/lessons/43238) | 주어진 시간의 처리 가능 인원으로 단조 판정 |
| 21 | 47 | 중상급 | [프로그래머스 64063 — 호텔 방 배정](https://school.programmers.co.kr/learn/courses/30/lessons/64063) | 희소한 방 번호를 딕셔너리·경로 압축으로 처리 |
| 22 | 48 | 중급 | [프로그래머스 42861 — 섬 연결하기](https://school.programmers.co.kr/learn/courses/30/lessons/42861) | 크루스칼과 유니온 파인드 |
| 23 | 35 | 중급 | [프로그래머스 12978 — 배달](https://school.programmers.co.kr/learn/courses/30/lessons/12978) | 단일 시작점 다익스트라, 중복 간선 |
| 24 | 41 | 중상급 | [프로그래머스 49191 — 순위](https://school.programmers.co.kr/learn/courses/30/lessons/49191) | 승패의 전이 폐쇄와 순위 확정 조건 |
| 25 | 36 | 중상급 | [프로그래머스 72413 — 합승 택시 요금](https://school.programmers.co.kr/learn/courses/30/lessons/72413) | 세 시작점의 거리와 분기점 열거. 플로이드–워셜로도 재풀이 가능 |
| 26 | 37 | 상급 | [프로그래머스 118669 — 등산코스 정하기](https://school.programmers.co.kr/learn/courses/30/lessons/118669) | 다중 시작점, 경로 합 대신 최대 간선 비용을 최소화 |
| 27 | 06 | 상급 | [프로그래머스 60061 — 기둥과 보 설치](https://school.programmers.co.kr/learn/courses/30/lessons/60061) | 설치·삭제 후 불변 조건 검사와 롤백 |
| 28 | 09 | 상급 | [프로그래머스 60063 — 블록 이동하기](https://school.programmers.co.kr/learn/courses/30/lessons/60063) | 로봇 위치·방향을 상태로 정의하고 이동·회전 BFS |
| 29 | 23 | 상급 | [프로그래머스 92344 — 파괴되지 않은 건물](https://school.programmers.co.kr/learn/courses/30/lessons/92344) | 직사각형 차분 갱신 후 누적합 복원 |
| 30 | 34 | 상급 | [프로그래머스 43236 — 징검다리](https://school.programmers.co.kr/learn/courses/30/lessons/43236) | 최소 간격을 답으로 탐색하고 제거 개수로 판정 |
