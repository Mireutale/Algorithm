"""
* CodingTest\starcoin\29863_Arno'sSleepSchedule.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    sleep = int(input())
    wake = int(input())
    if sleep < 4:
        print(wake - sleep)
    elif sleep > 19:
        print(wake + 24 - sleep)