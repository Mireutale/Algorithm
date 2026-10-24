"""
문자열 s를 여러 문자열로 분해

1. 첫 글자 x를 읽음
2. 이 문자열을 왼쪽에서 오른쪽으로 읽어나가며, x와 x가 아닌 다른 글자가 나온 횟수를 셈
3. 처음으로 두 횟수가 같이지는 순간 멈추고, 지금까지 읽은 문자열을 분리
4. s에서 분리한 문자열을 빼고 남은 부분에 대해서 반복
5. 남은 부분이 없거나, 횟수가 다른 상태에서 더 읽을 글자가 없으면 분리하고 종료

분해한 문자열의 개수를 return
"""

def stringSplit(s: list):
    x = s[0]
    cursor = 1
    same, diff = 1, 0
    while True:
        if cursor == len(s):
            return 0
        if x == s[cursor]: # 같은 글자
            same += 1
        else: # 다른 글자
            diff += 1

        cursor += 1
        if same == diff:
            return cursor

def solution(s):
    answer = 0
    cursor = 0
    split = False
    while True:
        ans = stringSplit(s[cursor:])
        if ans == 0:
            break
        else:
            answer += 1
            cursor += ans

        if cursor == len(s):
            split = True
            break

    if split:
        return answer
    else:
        return answer + 1

# LLM의 간결한 풀이
"""
문자열을 자르지 않기

balance는 문자열의 차를 둔 것.

balance가 0이면 문자열의 첫 글자를 선택하는 것이고 >> 새로운 문자열을 분리시키기 때문에 answer += 1을 수행
이후, balance가 다시 0될 때마다 분리를 반복.
"""
def solution(s):
    answer = 0
    balance = 0

    for char in s:
        if balance == 0:
            x = char
            answer += 1

        if char == x:
            balance += 1
        else:
            balance -= 1

    return answer
