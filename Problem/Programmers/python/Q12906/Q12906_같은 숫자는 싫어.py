"""
arr 에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거
단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 함
"""

def solution(arr):
    answer = []
    for i in range(len(arr) -1):
        if arr[i] != arr[i+1]:
            answer.append(arr[i])
    answer.append(arr[-1])
    return answer