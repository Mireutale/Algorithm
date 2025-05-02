from collections import deque

# 가능한 연산
def operations(n):
    return [n * 2, n + 1, n - 1]

# BFS를 이용해서 경로 탐색
def find_paths(start, target, steps):
    queue = deque()
    queue.append((start, [start]))

    results = []

    while queue:
        current, path = queue.popleft()
        if len(path) > steps + 1:
            continue
        if len(path) == steps + 1 and current == target:
            results.append(path)
            continue
        for next_val in operations(current):
            queue.append((next_val, path + [next_val]))
    
    return results

"""
18 58 4

18 66 4

16 50 4
    
34 0 8
"""
# 실행
start = 34
target = 0 + 10 + 5 + 6 + 7 + 8
steps = 4

paths = find_paths(start, target, steps)

# 결과 출력
if paths:
    for i, path in enumerate(paths, 1):
        print(f"경로 {i}: {' -> '.join(map(str, path))}")
else:
    print("조건을 만족하는 경로가 없습니다.")
