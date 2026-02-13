# # pass code를 sample에서 순차적으로 검출 가능하면 1, 아님 0 출력

import sys
sys.stdin = open("input.txt",'r')

T = int(input())
for tc in range(1,T+1):
    N,M1,M2 = map(int,input().split())
    lst = list(map(int,input().split()))

    lst = sorted(lst,reverse=True)

    bucket1 = []

    if M1 > M2:
        M1,M2 = M2,M1 # 무조건 적은 수의 블록을 먼저 작업하도록


    for i in range(M1):
        bucket1.append(lst[2*i]) # 짝수번째 인덱스 bucket에 넣기

    for j in range(M1):
        for i in range(N):
            if lst[i] == bucket1[j]:
                lst.remove(bucket1[j]) # bucket에 넣은 것 지우기
                break


    s = 0
    for i in range(len(lst)):
        s += (i+1) * lst[i]
    for i in range(len(bucket1)):
        s += (i+1) * bucket1[i]

    print(f"#{tc} {s}")




