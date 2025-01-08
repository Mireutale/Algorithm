import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    """
    [설계]
    
    알파벳 소문자로 이루어진 N개의 단어 입력
    길이가 짧은 순, 같으면 사전 순으로 정렬
    단, 중복된 단어는 하나만 남기고 모두 제거

    시간제한 2초, 메모리 제한 256MB
    """
    N = int(input())
    strings = [input() for _ in range(N)]
    #set으로 중복 제거, len(x), x튜플을 반환해서 정렬 기준을 길이 -> 문자열 순서로 정렬
    result = sorted(set(strings), key=lambda x: (len(x), x))
    for i in result:
        print(i)

"""
내장 함수를 사용하지 않고 작성한 경우

-중복제거
def remove duplicates(strings):
    items = []
    for item in strings:
        if item not in items:
            items.append(item)
    return items
-정렬_버블
def bubble_sort_len_word(strings):
    #버블 정렬을 이용
    for i in range(len(items) - 1):
        for j in range(len(items) -i - 1):
            if len(items[j]) > len(items[j + 1]):
                items[j], items[j+1] = items[j+1], items[j]
            elif len(items[j]) == len(items[j+1]) and items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    return items
-정렬_퀵
def quick_sort_len_word(strings):
    if len(strings) <= 1:
        # 길이가 1 이하인 리스트는 정렬 완료
        return strings  

    # 피벗 선택 (리스트의 첫 번째 요소)
    pivot = lst[0]
    
    # 피벗을 기준으로 작은 그룹, 같은 그룹, 큰 그룹으로 분리
    # 길이가 같은 경우 문자열의 순서를 기준으로 분리
    less = [x for x in lst[1:] if len(x) < len(pivot) or (len(x) == len(pivot) and x < pivot)]
    equal = lst[0]
    greater = [x for x in lst[1:] if len(x) > len(pivot) or (len(x) == len(pivot) and x > pivot)]
    
    # 재귀적으로 정렬 후 합치기
    return quick_sort(less) + equal + quick_sort(greater)
"""