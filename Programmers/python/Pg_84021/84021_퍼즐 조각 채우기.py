from collections import deque

dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def nomalize(piece):
    # 원점에서 가장 가까운 위치 잡고
    min_r = min(p[0] for p in piece)
    min_c = min(p[1] for p in piece)
    # 해당 값 만큼 빼서, 원점으로 이동시키고 정렬
    return sorted([(r - min_r, c - min_c) for r, c in piece])

def rotate_block(piece):
    # 90도 회전, [x=y축 대칭 -> x축 대칭]
    rotated = sorted([c, -r] for r, c in piece)
    return nomalize(rotated)

# 테이블에서 블럭 찾기
def get_block(grid, target_val):
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    blocks = []
    # 전체 값 중에서 target_val을 찾기
    for i in range(n):
        for j in range(n):
            if grid[i][j] == target_val and not visited[i][j]:
                queue = deque([(i, j)])
                visited[i][j] = True
                piece = [(i, j)]
                # bfs를 수행해서 블럭을 확인
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in dir:
                        nx, ny = x + dx, y + dy
                        # 테이블 안에 있고, 방문하지 않은 점 중
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                            # 동일하게 타겟인 위치만 찾기
                            if grid[nx][ny] == target_val:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
                                piece.append((nx, ny))
                # 찾은 조각을 모아 하나의 블럭으로 저장
                blocks.append(nomalize(piece))
    return blocks

def check_match(space, block):
    temp = block
    for _ in range(4):
        if space == temp:
            return True # 맞으면 즉시 종료하고 True 반환
        temp = rotate_block(temp)
    return False

def solution(game_board, table):
    blocks = get_block(table, 1)
    spaces = get_block(game_board, 0)
    
    used_blocks = [False] * len(blocks)
    answer = 0
    
    # game_board에서 찾은 빈 공간들에 대해서
    for space in spaces:
        for i, block in enumerate(blocks):
            # 이미 사용된 블럭이거나, 매치에 성공하면
            if not used_blocks[i] and check_match(space, block):
                # 점수 추가 및 블럭 사용 체크
                answer += len(block)
                used_blocks[i] = True
                break
            
    return answer