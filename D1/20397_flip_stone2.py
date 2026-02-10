# 동전처럼 생긴 돌의 양면은 각각 흰색과 검은색으로 되어있고, 게임의 규칙은 다음과 같다.
#
# i번째 돌을 사이에 두고 마주보는 j개의 돌에 대해, 각각 같은 색이면 뒤집고, 다른 색이면 그대로 둔다.
# 주어진 돌을 벗어나는 경우 뒤집기는 중지된다.
#
# 첫 줄에 게임의 개수 T, 다음 줄부터 게임별로 첫 줄에 돌의 수 N, 뒤집기 횟수 M, 다음 줄에 N개 돌의 초기상태, 이후 M개의 줄에 걸쳐 i, j가 주어진다.
# (1<=T<=50, 3<=N<=20,   1<=M<=10, 1<=i, j<=N)

T = int(input())
for tc in range(1,T+1):

    N,M = map(int,input().split())
    lst = list(map(int,input().split()))
    arr = [list(map(int,input().split())) for i in range(M)]

    for m in range(M):
        i = arr[m][0] # i와 j 배열에서 꺼내주기(편의)
        i -= 1 # 문제에서 인덱스가 1부터 시작하므로 조정
        j = arr[m][1]
        for n in range(1,j+1): # j번 반복
            if 0<=i-n and i+n<N: # 0~N-1을 벗어나지 않을 때
                if (lst[i-n] == 1) and (lst[i+n] == 1):
                    lst[i-n],lst[i+n] = 0,0 # 둘 다 1이라면 0으로 변환
                elif (lst[i-n] == 0) and (lst[i+n] == 0):
                    lst[i-n],lst[i+n] = 1,1 # 둘 다 0이라면 1로 변환


    print(f"#{tc}",end=" ")
    print(*lst)


