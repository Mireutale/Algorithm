# PG 76502 괄호 회전하기

import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def check_brackets(q):
    temp = deque()
    for i in range(len(q)):
        if q[i] == "[" or q[i] == "{" or q[i] == "(":
            temp.append(q[i])
        
        if q[i] == "]":
            if not temp:
                return 0
            
            if temp[-1] != "[":
                return 0
            else:
                temp.pop()
        
        if q[i] == "}":
            if not temp:
                return 0
            
            if temp[-1] != "{":
                return 0
            else:
                temp.pop()
            
        if q[i] == ")":
            if not temp:
                return 0
            
            if temp[-1] != "(":
                return 0
            else:
                temp.pop()

    if not temp:
        return 1
    else:
        return 0

def solution(s):
    answer = 0
    queue_s = deque(s)
    for _ in range(len(s)):
        queue_s.rotate(-1)
        if check_brackets(queue_s):
            answer += 1
    return answer

if __name__ == "__main__":
    s = input()
    print(solution(s))