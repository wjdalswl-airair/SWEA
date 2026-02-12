# 가로와 세로가 N*N 크기인 정사각형 모양의 한 마을에서 중계기를 설치한다
# 중계기의 통신 범위 안에 포함되지만, 통신 범위를 최소화 할 수 있는 중계기 통신 범위의 반지름 R의 최소값을 구하라
# 빈 공간은 0, 집이 있는 공간은 1, 중계기가 설치된 공간은 2로 표시
# 집과 중계기의 좌표가 각각 (hy, hx),(y,x)일 경우, 거리 D의 제곱은 D^2=(hy-y)^2 + (hx-x)^2

# import sys
# sys.stdin = open("input.txt",'r')

T = int(input())
for tc in range(1,T+1):
     N=int(input())
     arr = [list(map(int,input().split())) for i in range(N+1)]

     y,x,hy,hx=0,0,0,0
     Max=-21e8
     result = 0

     def distance(hy,hx): # hy,hx : 집의 좌표, y,x : 중계기의 좌표
         dis= ((hy-y)**2)+((hx-x)**2) # 집과 중계기 간의 거리 D의 제곱
         return dis

     for k in range(N+1): # 중계기의 좌표 구하기
          for l in range(N+1):
               if arr[k][l]==2:
                    y,x=k,l
                    break
          if y==True and x == True:
               break


     for i in range(N+1): # 집이 있다면 거리를 구하기 -> 가장 먼 집의 거리 기억하기
          for j in range(N+1):
               if arr[i][j] == 1:

                    D2 = distance(i,j)

                    if Max < D2:
                         Max = D2

     R=0
     while True: # 가장 먼 집을 포함하는 원의 반지름 구하기
          if R**2 >= Max:
               result = R
               break
          else:
               R+=1

     print(f"#{tc} {result}")