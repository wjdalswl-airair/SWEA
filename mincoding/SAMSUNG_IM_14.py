# N명의 선수들에 대해 선수들의 실력값이 주어질 때
# 실력 차이가 K 이하이면서 인원이 최대인 팀을 구성할때, 팀의 인원수

import sys
sys.stdin = open("input.txt", 'r')

T = int(input())
for tc in range(1, T + 1):
    N,K = map(int,input().split())
    lst = list(map(int, input().split()))
    lst = sorted(lst) # 실력 순서로 나열

    Max = -21e8
    for i in range(N-1):
        cnt = 1 # 일단 선수 1 포함
        for j in range(i+1,N):
            if lst[j]-lst[i]<=K: # 실력 차이가 K 이하인 사람의 수 세기
                cnt+=1
            else: # 기준 선수와 실력 차이가 K 이상이면 그만 세기
                break
        if Max<cnt: # 최대값 갱신
            Max = cnt

    print(f"#{tc} {Max}")




