# 근접 8개 구역 중 4개 이상이 중심보다 작은 숫자일 경우 후보지 선택
# 후보지의 개수는?
# 첫 줄에 구역의 크기 N,M, 다음 줄부터 N줄에 거쳐 M개 씩의 높이 정보(Aij)가 제공된다
# 3<=N,M <= 100, 0<=Aij<10

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for i in range(N)]

    cnt = 0
    for y in range(N):
        for x in range(M):
            s=0
            for i,j in (1,1),(-1,-1),(1,-1),(-1,1),(1,0),(-1,0),(0,1),(0,-1): # 근접 8개 검사
                dy = y+i
                dx = x+j
                if 0<=dy<N and 0<=dx<M: # 영역을 나가지 않는 것들만 검사
                    if arr[y][x]>arr[dy][dx]:
                        s+=1 # 중심 보다 낮은 영역의 수 세기
            if s >= 4:
                cnt += 1 # 후보지의 개수 세기
    print(f"#{tc} {cnt}")

