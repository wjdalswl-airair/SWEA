# 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다.
# 즉, 스위치가 켜져 있으면 끄고, 꺼져 있으면 켠다.
# <그림 1>과 같은 상태에서 남학생이 3을 받았다면, 이 학생은 <그림 2>와 같이 3번, 6번 스위치의 상태를 바꾼다.
#
# 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꾼다.
# 이때 구간에 속한 스위치 개수는 항상 홀수가 된다.



L = int(input())
N = int(input())
arr = [list(map(int,input().split())) for i in range(N)]
L += 1

Max_p = -21e8 # 가장 많은 조각을 받을 것으로 기대하고 있던 방청객의 번호
for i in range(N):
    expect = arr[i][1]-arr[i][0]+1
    if expect > Max_p:
        Max_p = expect
        Max_people = i+1

cake = [0]*L # 케이크에 손님 번호 매기기
for i in range(N):
    for j in range(arr[i][0],arr[i][1]+1):
        if cake[j] == 0:
            cake[j] = i+1

cnt =0
Max = -21e8
for j in range(N): # 손님 별 케이크 수 구하기 + MAX 갱신
    cnt = 0
    for i in range(L):
       if cake[i] == j+1:
           cnt += 1
    if cnt > Max:
        Max = cnt
        Max_real = j+1

print(Max_people)
print(Max_real)





