"""
* Codes\starcoin\24883_자동완성.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    user_input = input()
    if user_input == "N" or user_input == "n":
        print("Naver D2")
    else:
        print("Naver Whale")