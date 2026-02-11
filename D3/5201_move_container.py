# 한대의 트럭에 하나의 컨테이너를 실을 수 있다
# 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼을 때 총 중량을 구하시오
# 컨테이너 수 N과 트럭 수 M이 주어지고, 다음 줄에 N개의 화물이 무게wi, 그 다음 줄에 M개 트럭의 적재용량 ti가 주어진다.
# 1<=N, M<=100, 1<=wi, ti<=50

import sys
sys.stdin = open('sample_input.txt','r')

t = int(input())
for tc in range(1,t+1):
    N,M = map(int,input().split())
    W = list(map(int,input().split()))
    T = list(map(int,input().split()))
    W = sorted(W,reverse = True) # 내림차순 정렬
    T = sorted(T,reverse=True) # 내림차순 정렬

    s=0
    for i in range(M):
        for j in range(len(W)):
            if T[i] >= W[j]: # 트럭 중량보다 작은 최대 무게
                s += W[j]
                W.remove(W[j]) # 컨테이너 실었으니깐 빼주기
                break
    print(f"#{tc} {s}")


# 부분집합으로 여러대의 컨테이너를 실을 수 있다면??

##     def container(weight):
#         arr = [[] for i in range(1 << len(W))]
#         for i in range(1 << len(W)):
#             for j in range(len(W)):
#                 if i & (1 << j):
#                     arr[i].append(W[j])
#         Max = -21e8
#         Sort = []
#         for i in range(len(arr)):
#             if sum(arr[i]) <= weight:
#                 if Max < sum(arr[i]):
#                     Max = sum(arr[i])
#                     Sort = arr[i]
#         for item in Sort:
#             W.remove(item)
#         return sum(Sort)
#
#     s=0
#     for i in range(len(T)):
#         if len(W) >0:
#             s += container(T[i])
#
#     print(f"#{tc} {s}")
# #
