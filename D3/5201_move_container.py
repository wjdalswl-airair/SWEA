import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    W = list(map(int,input().split()))
    T = list(map(int,input().split()))
    arr = [[] for i in range(1<<N)]
    T = sorted(T,reverse=True)

    for i in range(1<<N):
        for j in range(N):
            if i & (1<<j) :
                arr[i].append(W[j])

    def container(weight):
        Min = 21e8
        for i in range(len(arr)):
            if sum(arr[i]) <= weight:
                if Min > weight - sum[arr[i]]:
                    Min = weight - sum[arr[i]]
                    Sort = arr[i]
        for i in Sort:
            W.remove[i]
        return Min

    s=0
    for i in range(len(T)):
        if len(W) >0:
            s += container(T[i])

    print(f"#{tc} {s}")
#
a = [5,4,3,2,1]
b = [5,2,1]

for i in b:
    a.remove(i)

print(a)
