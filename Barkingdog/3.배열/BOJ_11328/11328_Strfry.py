"""
* CodingTest/Barkingdog/3.배열/BOJ_11328/11328_Strfry.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def count_alpabet(word, alpabet):
    for i in word:
        alpabet[ord(i) - ord('a')] += 1
    return

if __name__ == "__main__":
    """
    [설계]
    
    strfry 함수는 입력된 문자열을 무작위로 재배열하여 새로운 문자열을 생성하는
    함수, 입력된 문자열과 재배열된 문자열이 다를 필요는 없음

    2개의 문자열에 대해서 2번째 문자열이 1번째 문자열에 strfry함수를 적용하여 얻어질 수 있는지 판단

    사용 알파벳의 개수가 동일하다면 가능한 것.
    """
    N = int(input())

    for i in range(N):
        word1, word2 = input().split()
        alpabet1 = [0] * 26
        alpabet2 = [0] * 26
        count_alpabet(word1, alpabet1)
        count_alpabet(word2, alpabet2)
        if alpabet1 == alpabet2:
            print("Possible")
        else:
            print("Impossible")



