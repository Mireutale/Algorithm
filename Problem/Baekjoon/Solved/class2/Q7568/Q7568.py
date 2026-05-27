#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    """
    [설계]
    키와 몸무게로 사람의 덩치를 표현하여 등수를 매김

    어떤 사람의 몸무게 x kg, 키 y cm인 경우 
    덩치는 (x, y)로 표현

    x와 y값 모두 커야 덩치가 더 크다고 표현
    따라서 덩치 등수가 같은 사람이 존재 가능
    
    시간 제한 1초, 메모리 제한 128MB
    2 <= people <= 50
    10 <= x, y <= 200
    """
    people = int(input())
    weight = []
    height = []
    # 순서대로 사람들의 키와 몸무게 저장
    for _ in range(people):
        x, y = map(int, input().split())
        weight.append(x)
        height.append(y)
    # 모든 사람 저장 후, 크기 비교
    size_rank = []    
    for i in range(people):
        big_people_count = 0
        for j in range(people):
            if i != j:
                # 덩치가 더 큰 사람을
                if weight[i] < weight[j] and height[i] < height[j]:
                        big_people_count += 1
        size_rank.append(big_people_count+1)
    for i in size_rank:
        print(i, end=" ")