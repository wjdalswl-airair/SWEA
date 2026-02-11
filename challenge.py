# 미로찾기
# 0,0,0,0
# 1,0,1,0
# 1,0,1,0
# 0,0,0,0

# 0,0 에서 출발해서 3,3까지 도착하고자 한다.
# 방탈출이 가능한지 불가능 한지 출력해 주세요
arr=[[0,0,0,0,1],
     [1,0,1,0,1],
     [1,0,1,0,1],
     [0,0,0,0,0]]
visited=[[0]*5 for _ in range(5)]
flag=0
directy=[0,0,-1,1]
directx=[-1,1,0,0]
cnt = 0
Min = 21e8
def dfs(nowy,nowx):
     global flag
     global cnt
     global Min
     cnt += 1
     if nowy==1 and nowx==3: # 도착했다면
          flag=1
          if cnt < Min:
              cnt = Min
          return

     for i in range(4):
          dy=nowy+directy[i]
          dx=nowx+directx[i]
          if dy < 0 or dy > 4 or dx < 0 or dx > 4: continue  # 범위 check
          if arr[dy][dx]==1: continue # 벽 x
          if visited[dy][dx]==1: continue # 방문 check
          visited[dy][dx]=1
          dfs(dy,dx)
          if flag==1:
               return

visited[0][0]=1 # 시작점 좌표에 방문체크하고
dfs(0,0) # 시작 인덱스로 dfs 탐색 시작

print(Min)