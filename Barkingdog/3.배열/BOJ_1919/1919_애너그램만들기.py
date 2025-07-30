"""
* CodingTest/Barkingdog/3.배열/BOJ_1919/1919_애너그램만들기.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]

두 영어 단어가 철자의 순서를 바뀌어서 같아질 수 있는 경우 애너그램

두 단어가 서로 애너그램 관계에 있도록 만들기 위해서 
제거해야 하는 최소 개수의 문자 수를 구하는 프로그램

입력 받은 두 문자의 알파벳 개수를 파악
이후, 같은 개수를 가진 알파벳 제외 전부 삭제 수행
"""

def count_alpabet(word, alpabet):
    for i in word:
        alpabet[ord(i) - ord('a')] += 1
    return

if __name__ == "__main__":
    word1 = input()
    word2 = input()
    alpabet1 = [0] * 26
    alpabet2 = [0] * 26
    count_alpabet(word1, alpabet1)
    count_alpabet(word2, alpabet2)
    delete_alpabet = 0
    for i in range(26):
        delete_alpabet += abs(alpabet1[i] - alpabet2[i])
    print(delete_alpabet)