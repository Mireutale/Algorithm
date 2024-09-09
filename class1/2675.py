n = int(input())
R = []
S = []
for i in range(n):
    r, s = input().split()
    R.append(r)
    S.append(s)

for i in range(n):
    for j in range(len(S[i])): #문자열 크기
        for k in range(int(R[i])): #반복 횟수
            print(S[i][j], end = "")
    print("\n", end = "")