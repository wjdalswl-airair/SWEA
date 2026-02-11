# 남학생은 남학생끼리, 여학생은 여학생끼리 방을 배정해야 한다. 또한 한 방에는 같은 학년의 학생들을 배정해야 한다.
# 한 방에 배정할 수 있는 최대 인원 수 K가 주어졌을 때, 조건에 맞게 모든 학생을 배정하기 위해 필요한 방의 최소 개수를 구하는 프로그램을 작성하시오
# 첫 번째 줄에는 수학여행에 참가하는 학생 수를 나타내는 정수 N(1 ≤ N ≤ 1,000)과 한 방에 배정할 수 있는 최대 인원 수 K(1 < K ≤ 1,000)가 공백으로 분리되어 주어진다. 다음 N 개의 각 줄에는 학생의 성별 S와 학년 Y(1 ≤ Y ≤ 6)가 공백으로 분리되어 주어진다. 성별 S는 0, 1중 하나로서 여학생인 경우에 0, 남학생인 경우에 1로 나타낸다.

#
# import sys
# sys.stdin = open('sample_input.txt','r')
#
t = int(input())
for tc in range(1,t+1):
    N,K = map(int,input().split())
    arr = [list(map(int,input().split())) for i in range(N)]

    girl = [0]*7
    boy = [0]*7

    for i in range(N):
        if arr[i][0] == 0:
            girl[arr[i][1]] += 1 #DAT활용
        elif arr[i][0] == 1:
            boy[arr[i][1]] += 1 #DAT활용
    s=0
    for i in range(7): # 각 학년/성별 별 방의 개수 구하기
        if girl[i]%2 ==1:
            s+= (girl[i]//2)+1
        else:
            s+= girl[i]//2
        if boy[i]%2 ==1:
            s+= (boy[i]//2)+1
        else:
            s+= boy[i]//2

    print(f"#{tc} {s}")
