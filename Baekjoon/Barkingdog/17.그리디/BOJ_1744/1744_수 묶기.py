# Barkingdog/17.그리디/BOJ_1744/1744_수 묶기.py

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())
    positive = list()
    negative = list()
    one = 0
    zero = 0
    for _ in range(n):
        new_num = int(input())
        if new_num > 1:
            positive.append(new_num)
        elif new_num == 1:
            one += 1
        elif new_num == 0:
            zero += 1
        else:
            negative.append(new_num)
    
    ans = 0

    # 양수
    if positive:
        positive.sort(reverse=True) # 내림차순 정렬
        if len(positive) % 2 == 0: #짝수
            for i in range(0, len(positive), 2):
                ans += positive[i] * positive[i+1]
        else:
            for i in range(0, len(positive)-1, 2):
                ans += positive[i] * positive[i+1]
            ans += positive[-1]
    
    # 1
    ans += one

    # 음수
    if negative:
        negative.sort()
        if len(negative) % 2 == 0:
            for i in range(0, len(negative), 2):
                ans += negative[i] * negative[i+1]
        else:
            for i in range(0, len(negative)-1, 2):
                ans += negative[i] * negative[i+1]
            if zero == 0:
                ans += negative[-1]
    
    print(ans)
