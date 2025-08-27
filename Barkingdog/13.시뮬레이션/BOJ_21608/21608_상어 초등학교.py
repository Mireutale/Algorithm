"""
* CodingTest/Barkingdog/13.시뮬레이션/BOJ_21608/21608_상어 초등학교.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N = int(input())
    like = {}
    student = []
    for _ in range(N*N):
        stu, *likes = list(map(int, input().split()))
        like[stu] = likes
        student.append(stu)
    classroom = list([0] * N for _ in range(N))
    dx, dy = [-1,1,0,0], [0,0,-1,1]

    for stu in student:
        # * 학생이 앉을 수 있는 후보지
        candidates = []
        for i in range(N):
            for j in range(N):
                # * 좌석에 이미 학생이 있는 경우
                if classroom[i][j]: 
                    continue
                # * 빈 좌석
                like_sit, empty_sit = 0, 0
                for d in range(4):
                    ni, nj = i+dx[d], j+dy[d]
                    if 0 <= ni < N and 0 <= nj < N:
                        # * 인접한 경우
                        if classroom[ni][nj] in like[stu]:
                            like_sit += 1
                        # * 빈 자리인 경우
                        if classroom[ni][nj] == 0: 
                            empty_sit += 1
                candidates.append((like_sit, empty_sit, i, j ))
        # * 내림차순 정렬 -> '-'사용
        candidates.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
        x, y = candidates[0][2], candidates[0][3]
        classroom[x][y] = stu

    # 만족도 계산
    score = [0, 1, 10, 100, 1000]
    ans = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            for d in range(4):
                ni, nj = i+dx[d], j+dy[d]
                if 0 <= ni < N and 0 <= nj < N:
                    if classroom[ni][nj] in like[classroom[i][j]]:
                        cnt += 1
            ans += score[cnt]

    print(ans)