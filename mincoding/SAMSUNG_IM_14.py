# 원하는 패턴이 나올 때까지 눌러야 하는 조명의 최소 클릭 횟수
# M번 조명 클릭 시 M 배수 조명이 켜지거나 꺼진다

import sys
sys.stdin = open("input.txt", 'r')

T = int(input())
for tc in range(1, T + 1):
    N,K = map(int,input().split())
    lst = list(map(int, input().split()))
    lst = sorted(lst)

    Max = -21e8
    for i in range(N):
        cnt = 0
        for j in range(i,N):
            cnt+=1
            if lst[j]==i+K:
                break
            elif Max <cnt:
                Max = cnt

    print(f"#{tc} {Max}")




