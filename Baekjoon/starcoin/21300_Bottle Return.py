import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    beer, malt, wine_products, carbonated_soft_drinks, seltzer, water = map(int, input().split())
    print(5 * (beer + malt + wine_products + carbonated_soft_drinks + seltzer + water))