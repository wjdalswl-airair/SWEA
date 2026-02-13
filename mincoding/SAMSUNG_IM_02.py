# 총 M개의 문제에서 정답을 맞출경우 1점, 연속으로 맞출 경우 보너스 1점 가산
# M개의 문제에 대한 N명의 학생들의 답안지가 주어졌을 때, 가장 높은 점수를 받은 학생과, 가장 낮은 점수를 받은 학생의 점수차는?

#
# import sys
# sys.stdin = open("input.txt",'r')

from collections import deque

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    answer = list(map(int,input().split()))

    def grade(lst): # 한 학생의 점수를 계산하는 함수
        cnt = 0
        num=0
        for i in range(M):
            if answer[i]==lst[i]:
                cnt += 1 # 각 문제의 점수
                num+=cnt # 점수 누적합
            else:
                cnt = 0 # 연속 정답이 끝났다면 0부터 시작

        return num


    score=[]
    for i in range(N):
        student = list(map(int,input().split()))
        total=grade(student) # 한 학생씩 입력받고 점수 계산하기
        score.append(total)

    result = max(score)-min(score)
    print(f"#{tc} {result}")

