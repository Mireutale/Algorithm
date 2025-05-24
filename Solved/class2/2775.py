import sys
input = lambda : sys.stdin.readline().rstrip()
"""
    조건 : a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 
    b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다

    빈 집은 없음.
    k층의 n호에 몇명이 살고 있는지 출력.

    재귀로 풀려고 하면 시간초과

    리스트 형태로 층과 호수에 맞는 인원의 수를 입력 -> 
    테이블을 보고 값을 합쳐서 출력
    """
def people(k, n):
    list = [[] for _ in range(k+1)]
    #층수
    for i in range(k+1):
        #n호
        for j in range(1, n+1):
            #0층
            if(i == 0):
                list[i].append(j)
            else:
                sum_people = 0
                for l in range(j):
                    sum_people += list[i-1][l]
                list[i].append(sum_people)
    return list[k][n-1]

if __name__ == "__main__":
    #T
    number_of_testcase = int(input())
    for i in range(number_of_testcase):
        #k
        apt_level = int(input())
        #n
        room_number = int(input())
        #k층의 n호에 사는 사람 출력
        print(people(apt_level, room_number))