"""
* CodingTest/Barkingdog/11.재귀/BOJ_1780/1780_종이의개수.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

Counter = {
    -1 : 0, 
    0 : 0, 
    1 : 0 
}

def rules(row: int, col:int, input_number:int) -> None:
    first = paper[row][col]
    for i in range(row, row + input_number):
        for j in range(col, col + input_number):
            if first != paper[i][j]:
                for x in range(3):
                    for y in range(3):
                        rules(row + (input_number//3)* x, col + (input_number//3) * y, input_number//3)
                return # ? 분할하기 전 종이에 대해서도 Counter값을 추가
    Counter[first] += 1

if __name__ == "__main__":
    n = int(input())
    paper = [list(map(int, input().split())) for _ in range(n)]
    rules(0, 0, n)
    print(Counter[-1])
    print(Counter[0])
    print(Counter[1])

"""리팩토링 전
import sys
input = lambda: sys.stdin.readline().rstrip()

matrix = list[list[int]]

minus_one_paper = 0
zero_paper = 0
one_paper = 0

def plus_paper(data):
    global minus_one_paper, zero_paper, one_paper
    if data == -1:
        minus_one_paper += 1
        return 0
    elif data == 0:
        zero_paper += 1
        return 0
    elif data == 1:
        one_paper += 1
        return 0
    else:
        raise Exception("-1, 0, 1만 입력될 수 있습니다.")

def divide_paper_to_nine_parts(input_number:int, paper: matrix):
    if input_number % 3 == 0:
        input_number //= 3
    else:
        raise Exception("3의 배수여야 합니다.")
    
    for i in range(3):
        for j in range(3):
            slice_paper = [row[j*input_number:(j+1)*input_number] for row in paper[i*input_number:(i+1)*input_number]]
            rules(input_number, slice_paper)
    

def check_all_wirtes_same(input_number: int , paper: matrix):
    first = paper[0][0]
    for i in range(input_number):
        for j in range(input_number):
            if first == paper[i][j]:
                if i == input_number -1 and j == input_number - 1:
                    plus_paper(first)
                    return True
                else:
                    pass
            else:
                return False

def rules(input_number: int, paper: matrix):
    if check_all_wirtes_same(input_number, paper):
        pass
    else:
        divide_paper_to_nine_parts(input_number, paper)

if __name__ == "__main__":
    n = int(input())
    paper = [list(map(int, input().split())) for _ in range(n)]
    rules(n, paper)
    print(minus_one_paper)
    print(zero_paper)
    print(one_paper)
"""