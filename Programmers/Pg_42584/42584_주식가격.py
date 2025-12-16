# PG 42584 주식가격

import sys
input = lambda: sys.stdin.readline().rstrip()

def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                answer[i] += 1
                break
            else:
                answer[i] += 1
    return answer

if __name__ == "__main__":
    prices = list(map(int, input().split(",")))
    print(solution(prices))