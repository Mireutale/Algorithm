#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    """
    [설계]
    높이가 V미터인 나무 막대를 오른다.
    낮에는 A미터 올라가고, 밤에는 B미터 미끄러진다.
    정상에 올라간 후에는 미끄러지지 않고, 나무 막대를 모두 올라가려면
    몇일이 걸리는지?
    """

    A, B, V = map(int, input().split())
    current_height = A
    up_days = 1
    while(current_height >= V):
        current_height -= B
        current_height += A
        up_days += 1
    print(up_days)