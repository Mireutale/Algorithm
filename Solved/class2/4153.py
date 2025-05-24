import sys
input = lambda: sys.stdin.readline().rstrip()

while(True):
    numbers = input().split()
    numbers = [int(i) for i in numbers]
    numbers.sort()
    if numbers[0] == numbers[1] == numbers[2] == 0:
        break
    a2 = numbers[0]*numbers[0]
    b2 = numbers[1]*numbers[1]
    c2 = numbers[2]*numbers[2]
    if a2 + b2 == c2:
        print('right')
    else:
        print('wrong')


"""
출처 백준 아이디 : hraverals
while True:
    r = list(map(int, input().split()))
    r.sort()
    a = r[0]
    b = r[1]
    c = r[2]
    if a**2 + b**2 == c**2 and a != 0:
        print('right')
    elif a == b == c == 0:
        break
    else:
        print('wrong')
"""