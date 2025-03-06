#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
import math
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    """
    [설계]
    
    수학여행 남학생끼리 여학생끼리 방 배정 + 같은 학년의 학생들 배정

    한 방에 배정할 수 있는 최대 인원 K

    필요한 방의 최소 개수를 구하는 프로그램

    수학여행 참가 학생 수 N(1 ~ 1000)
    한 방에 배정할 수 있는 최대 인원 K(1 ~ 1000)
    다음 N개의 줄에 학생의 성별 S와 학년 Y(1 ~ 6)이 공백으로 분리되어 주어짐.
    S의 경우 여학생 0, 남학생 1

    1 ~ 6까지의 배열에 이중 리스트로 [0, 0]을 입력
    S값에 따라서 앞 또는 뒤 값을 +1해서 학생 수 파악하기
    """
    N, K = map(int, input().split())
    #! student = [[0, 0]] * 6으로 사용하는 경우, 모든 원소가 동일한 리스트를 참조하게 되어
    #! 모든 원소의 값이 동시에 바뀌는 문제 있음
    student = [[0, 0] for _ in range(6)]
    for i in range(N):
        S, Y = map(int, input().split())
        student[Y-1][S] += 1
    rooms = 0
    for i in range(6):
        for j in range(2):
            #? 무조건 올림 ceil사용
            rooms += math.ceil(student[i][j] / K)
    print(rooms)

