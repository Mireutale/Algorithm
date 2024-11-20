import sys
input = lambda : sys.stdin.readline().rstrip()

if __name__ == "__main__":
    """
    조건 : a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 
    b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다

    빈 집은 없음.
    k층의 n호에 몇명이 살고 있는지 출력.

    아파트는 0층부터 있고, 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.
    """
    #T
    number_of_testcase = int(input())
    for i in range(number_of_testcase):
        #k
        apt_level = int(input())
        #n
        apt_level_room_number = int(input())

        #k층의 n호에 사는 사람 출력                                                                                                                                                                                                 
        for j in range(apt_level):
