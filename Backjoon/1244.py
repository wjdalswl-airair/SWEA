# 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다.
# 즉, 스위치가 켜져 있으면 끄고, 꺼져 있으면 켠다.
# <그림 1>과 같은 상태에서 남학생이 3을 받았다면, 이 학생은 <그림 2>와 같이 3번, 6번 스위치의 상태를 바꾼다.
#
# 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꾼다.
# 이때 구간에 속한 스위치 개수는 항상 홀수가 된다.



n = int(input())
lst = list(map(int,input().split()))

student = int(input())
arr = [list(map(int,input().split())) for i in range(student)]

def boy(index): # 남자인 경우 배수 스위치 전환
    for i in range(n):
        if (i+1) % index ==0:
            if lst[i] == 0:
                lst[i] = 1
            elif lst[i] ==1:
                lst[i] =0

def girl(index): # 여자인 경우 대칭인 스위치 전환
    index -= 1
    if lst[index] == 0:
        lst[index] = 1
    elif lst[index] == 1:
        lst[index] = 0
    for i in range(1, n+1):
        if 0<=(index-i) and index +i <n:
            if lst[index-i] == lst[index+i]:
                if lst[index-i] == 0:
                    lst[index-i],lst[index+i] = 1,1
                elif lst[index-i] == 1:
                    lst[index-i],lst[index+i] = 0,0
            else:
                break



for i in range(student):
    if arr[i][0] == 1:
        boy(arr[i][1])
    elif arr[i][0] ==2:
        girl(arr[i][1])

for i in range(n): # 20개씩 나눠서 프린트
    print(lst[i],end=" ")
    if (i+1)%20 == 0:
        print()




