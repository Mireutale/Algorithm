# Barkingdog/12.백트래킹/BOJ_15663/15663_N과 M(9).py

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n, m = map(int, input().split())
    number_list = list(map(int, input().split()))
    number_list.sort()
    ary = []
    user = [False] * n

    """set을 활용한 중복 제거"""
    # ans = set()
    
    # def back_tracking():
    #     if len(ary) == m:
    #         temp = tuple(ary)
    #         if temp not in ans:
    #             print(*ary)
    #             ans.add(temp)
    #         return
        
    #     for i in range(len(number_list)):
    #         if user[i] == 0:
    #             user[i] = True
    #             ary.append(number_list[i])
    #             back_tracking()
    #             user[i] = False
    #             ary.pop()

    """prev를 활용한, 같은 depth에서의 중복 제거"""
    def back_tracking():
        if len(ary) == m:
            print(*ary)
            return
        
        prev = None

        for i in range(len(number_list)):
            if user[i] or prev == number_list[i]:
                continue
            else:
                user[i] = True
                ary.append(number_list[i])
                back_tracking()
                user[i] = False
                ary.pop()
                prev = number_list[i]

    back_tracking()
