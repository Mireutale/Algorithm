def solution(n, results):
    # wins[a][b]: a 선수가 b 선수를 이길 수 있는지 여부
    wins = [[False] * (n + 1) for _ in range(n + 1)]
    for winner, loser in results:
        wins[winner][loser] = True

    # a가 middle을 이기고 middle이 b를 이기면 a는 b를 이긴다.
    for middle in range(1, n + 1):
        for a in range(1, n + 1):
            if not wins[a][middle]:
                continue
            for b in range(1, n + 1):
                if wins[middle][b]:
                    wins[a][b] = True

    answer = 0
    for player in range(1, n + 1):
        known = sum(
            wins[player][other] or wins[other][player]
            for other in range(1, n + 1)
            if other != player
        )
        # 자신을 제외한 모든 선수와의 승패를 알면 순위가 확정된다.
        if known == n - 1:
            answer += 1

    return answer


if __name__ == "__main__":
    print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
