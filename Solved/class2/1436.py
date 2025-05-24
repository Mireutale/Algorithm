import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    """
    [설계]
    첫째 줄에 N이 주어진다.
    N번째 영화의 제목에 들어간 수를 출력
    종말의 수는 6이 적어도 3개 이상 연속으로 들어가는 수를 의미

    666, 1666, 2666, 3666, 4666, 5666, 6661, 6662, 6663, ..., 6669, 7666, ...

    브루트포스 외 더 시간을 줄일 방법은?
    10의 배수를 더하는 방식을 생각했으나, 5666이후에는 6660이 다음 수가 되어야 한다.
    근데, 10의 배수를 더하는 방식을 사용하는 경우 6666을 다음 수로 선택하게 된다.
    다른 방식을 생각해 보아도 오히려 더 복잡해진다..
    결국 브루트포스를 사용해야 풀 수 있는 문제
    """
    N = int(input())
    apocalypse = [666]
    current_number = 666
    while len(apocalypse) < N:
        new_apocalypse_number = current_number + 1
        if '666' in str(new_apocalypse_number):
            apocalypse.append(new_apocalypse_number)
            current_number = new_apocalypse_number
        else:
            current_number += 1
    print(apocalypse[N-1])
        