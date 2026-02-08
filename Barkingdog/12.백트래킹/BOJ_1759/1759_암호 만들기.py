# Barkingdog/12.백트래킹/BOJ_1759/1759_암호 만들기.py

import sys
input = lambda: sys.stdin.readline().rstrip()

def is_valid():
    vowel = ["a", "e", "i", "o", "u"]
    vowel_count = sum(True for char in ans if char in vowel)
    consonant_count = l - vowel_count
    return vowel_count >= 1 and consonant_count >= 2

if __name__ == "__main__":
    l, c = map(int, input().split())
    chars = input().split()
    ans = []
    def make_pw():
        if len(ans) == l:
            if is_valid():
                print(*ans, sep = "")
                return

        for char in sorted(chars):
            if not ans or ans[-1] < char:
                ans.append(char)
                make_pw()
                ans.pop()
    
    make_pw()
