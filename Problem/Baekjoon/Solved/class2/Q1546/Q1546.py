import sys

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    """
    [설계]
    최고점을 M으로 설정
    모든 점수를 점수/M * 100을 수정
    새로운 평균을 구하는 프로그램 작성
    """
    exam_dept = int(input())
    exam_score = list(map(int, input().split()))
    M = max(exam_score)
    for i in range(exam_dept):
        exam_score[i] = exam_score[i]/M * 100
    print(sum(exam_score)/len(exam_score))