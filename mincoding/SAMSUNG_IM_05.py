# # pass code를 sample에서 순차적으로 검출 가능하면 1, 아님 0 출력

import sys
sys.stdin = open("input.txt",'r')

T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    Sample = list(map(int,input().split()))
    PassCode = list(map(int,input().split()))

    result = 0
    st = 0

    for i in range(K):
        flag = 0 # 해당 단어 없다고 가정
        for j in range(st,N):
            if Sample[j]==PassCode[i]:
                st = j+1
                flag = 1
                break
        if flag==0: # sample 다 돌았는데 없으면 더 이상 검사할 필요 없음
            break
        if i==K-1 and flag == 1: # 마지막까지 돌았을 때 flag = 1이면 결과 1
            result = 1

    print(f"#{tc} {flag}")




