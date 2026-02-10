# import sys
# sys.stdin = open('sample_input.txt','r')
#
# T = int(input())
# for tc in range(1,T+1):
#     N,M = map(int,input().split())
#     W = list(map(int,input().split()))
#     T = list(map(int,input().split()))
#     arr = [[] for i in range(1<<N)]
#
#     for i in range(1<<N):
#         for j in range(N):
#             if i & (1<<j) :
#                 arr[i].append(W[j])
#
#     w_list = list(map(sum,arr))
#
#     print(w_list)
#
#     s=0
#     for j in range(M):
#         Max = -21e8
#         for i in range(len(w_list)):
#             if T[j]>=w_list[i] and Max<w_list[i]:
#                 if Max < w_list[i]:
#                     Max = w_list[i]
#         s+=Max
#
#     print(f"#{tc} {s}")
#
a = [5,4,3,2,1]
b = [5,2,1]

for i in b:
    a.remove(i)

print(a)
