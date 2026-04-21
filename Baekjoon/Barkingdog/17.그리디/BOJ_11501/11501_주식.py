# Barkingdog/17.그리디/BOJ_11501/11501_주식.py

import sys
input = lambda: sys.stdin.readline().rstrip()

def stock(deck):
    profit = 0
    max_sale = 0
    for i in range(len(deck)-1, -1, -1):
        if max_sale < deck[i]:
            max_sale = deck[i]
        else:
            profit += max_sale-deck[i]
    return profit

if __name__ == "__main__":
    test_case = int(input())
    for _ in range(test_case):
        days = int(input())
        stocks_per_days = list(map(int, input().split()))
        print(stock(stocks_per_days))