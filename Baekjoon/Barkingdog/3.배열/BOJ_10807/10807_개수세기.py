# Barkingdog/3.배열/BOJ_10807/10807_개수세기.py

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    """
    [설계]

    총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램

    첫째줄 정수의 개수 N (1 ~ 100)
    둘째줄 정수가 공백으로 구분, 셋째줄 찾으려고하는 정수 v

    입력으로 주어지는 정수와 v (-100 ~ 100)

    디렉토리를 통해 key와 value를 설정해서 값을 할당하는 방법도 있고, 쉽게 배열로하는 방법도 있음
    배열로 풀어봄
    
    -100부터 100까지 201개의 수수
    """
    int_list = [0] * 201
    N = int(input())
    data = input().split()
    for i in range(N):
        int_list[int(data[i]) + 100] += 1
    v = int(input())
    print(int_list[v + 100])
