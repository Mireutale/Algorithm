# Barkingdog/13.시뮬레이션/BOJ_14889/14889_스타트와 링크.py

# import sys
# from math import inf
# from itertools import permutations, combinations
# input = lambda: sys.stdin.readline().rstrip()

# if __name__ == "__main__":
#     n = int(input())
#     status = [list(map(int, input().split())) for _ in range(n)]
#     select = list(combinations(list(i for i in range(n)), n//2))
#     gap = inf
#     for i in range(len(select)//2):
#         start_status = 0
#         link_status = 0
#         combination = select[i]
#         reverse_combination = select[len(select)-1-i]
#         start = list(permutations(combination, 2))
#         link = list(permutations(reverse_combination, 2))
#         for x, y in start:
#             start_status += status[x][y]
#         for x, y in link:
#             link_status += status[x][y]
#         gap = min(gap, abs(start_status - link_status))
#     print(gap)

from itertools import combinations
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    status = [list(map(int, input().split())) for _ in range(n)]
    reverse_status = list(zip(*status))
    ns = [sum(status[i]) + sum(reverse_status[i]) for i in range(n)]
    total = sum(ns) // 2
    ans = float('inf')
    print(ns)
    for comb in combinations(ns[:-1], n // 2):
        diff = abs(total - sum(comb))
        if diff < ans: ans = diff
    print(ans)

main()
