# 원하는 패턴이 나올 때까지 눌러야 하는 조명의 최소 클릭 횟수
# M번 조명 클릭 시 M 배수 조명이 켜지거나 꺼진다

import sys
sys.stdin = open("input.txt", 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    last = list(map(int, input().split()))
    origin = [0] * N

    def turn(index): # 배수 인덱스의 불 켰다 끄기
        for i in range(index+1,N+1,index+1):
            origin[i-1] = 1-origin[i-1]

    cnt = 0
    for i in range(N):
        if last[i] != origin[i]: # 정답과 다르면 불끄기 진행
            turn(i)
            cnt+=1

    print(f"#{tc} {cnt}")




