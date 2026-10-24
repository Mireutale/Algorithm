"""
왼손 엄지는 *, 오른손 엄지는 #에 위치

규칙
1. 엄지는 상하좌우 4가지 방향으로만 이동할 수 있고, 거리는 1칸만 이동 가능
2. 왼쪽 열 3개의 숫자 1, 4, 7을 입력할때는 왼손
3. 오른쪽 열 3개의 숫자 3, 6, 9를 입력할때는 오른손
4. 가운데 열 4개의 숫자 2, 5, 8, 0을 입력할때는 두 엄지 중 현재 키패드 위치에서 더 가까운 엄지 사용
- 만약 거리가 동일하면 오른손잡이는 오른 엄지, 왼손잡이는 왼 엄지 사용

각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return
"""
def solution(numbers, hand):
    # 미리 숫자별 위치 지정
    positions = {
        1: (3, 0), 2: (3, 1), 3: (3, 2),
        4: (2, 0), 5: (2, 1), 6: (2, 2),
        7: (1, 0), 8: (1, 1), 9: (1, 2),
                   0: (0, 1),
    }

    left = (0, 0)
    right = (0, 2)
    answer = []

    for number in numbers:
        row, col = positions[number]

        if col == 0:
            use_left = True
        elif col == 2:
            use_left = False
        else: # 가운데 있는 숫자
            d_left = abs(row - left[0]) + abs(col - left[1])
            d_right = abs(row - right[0]) + abs(col - right[1])

            # 왼손 거리가 더 짧거나, 동일한 거리일때 왼손잡이인 경우
            use_left = (
                d_left < d_right
                or (d_left == d_right and hand == 'left')
            )

        if use_left:
            answer.append('L')
            left = (row, col)
        else:
            answer.append('R')
            right = (row, col)

    return ''.join(answer)
