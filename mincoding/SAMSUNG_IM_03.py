# P의 크기만큼 가로, 세로방향으로 바이러스를 해독할 때, NxN 마을에서 한 위치에 해독제를 줬을떄
# 가장 많은 바이러스를 제거할 수 있을 경우 바이러스의 개수

import sys
sys.stdin = open("input.txt",'r')

T = int(input())
for tc in range(1,T+1):
    N,P = map(int,input().split())
    arr = [list(map(int,input().split())) for i in range(N)]

    def char(y,x): # 죽은 바이러스의 수
        cnt = 0
        vir = 0
        for i,j in (1,0),(-1,0),(0,1),(0,-1):
            for power in range(1,P+1):
                dy = y + i * power
                dx = x + j * power
                if 0<=dy<N and 0<=dx<N:
                    cnt += arr[dy][dx] #바이러스의 수 누적
        vir=cnt+arr[y][x] # 원점 더하기 잊지 말기
        return vir

    Max = -21e8
    for i in range(N):
        for j in range(N):
            die = char(i,j) # 모든 경우에서 바이러스의 수 구한 후 최대값 출력
            if Max<die:
                Max = die

    print(f"#{tc} {Max}")




