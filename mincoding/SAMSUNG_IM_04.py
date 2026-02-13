# [1] 특정 좌표를 기준으로, "우측 하단"의 방향으로 사각형을 그릴 수 있다.
# [2] 왼쪽 상단 좌측의 값과 우측 하단 좌표의 값이 동일해야 한다.
# NxN 크기의 게임판이 주어졌을 때, 최대 면적의 사각형을 규칙대로 그릴 수 있는 총 사각형의 개수는?

import sys
sys.stdin = open("input.txt", 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int,input().split())) for i in range(N)]

    lst = []


    def area(y,x): # 우측 하단으로 나아가며 면적 구하여 lst에 넣기
        for i in range(y,N):
            for j in range(x,N):
                if arr[y][x] == arr[i][j]:
                    sur = (i - y + 1) * (j - x + 1)
                    lst.append(sur)


    for i in range(N):
        for j in range(N):
            area(i,j)

    Max = max(lst) # 구해진 면적들 중 최대 면적

    cnt = 0
    for i in lst:
        if i == Max: # 최대 면적의 개수 구하기
            cnt += 1

    print(f"#{tc} {cnt}")




