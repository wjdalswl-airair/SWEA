# NxN 배열에서 + 혹은 x 형태로 M의 세기로 스프레이를 뿌릴 수 있다
# 한번에 잡을 수 있는 최대 파리수를 출력하라
# 배열 안의 숫자는 해당 영역에 존재하는 파리의 개체 수를 의미한다
# 뿌려진 일부가 영역을 벗어나도 상관없다
# 5<=N<=15
# 2<=M<=N
# 각 영역의 파리 개수 <= 30

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]

    Max = -21e8


    def cross(y, x): # + 형태의 최대 파리 수
        Sum = 0
        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]
        for l in range(4): # + 형태 세기 별 반복
            for k in range(1, M): # 각 세기 별 반복
                i = y + (dy[l] * k)
                j = x + (dx[l] * k)
                if 0 <= i < N and 0 <= j < N:
                    Sum += arr[i][j]
        return Sum


    def dia(y, x): # x 형태의 최대 파리 수
        Sum = 0
        dy = [-1, 1, 1, -1]
        dx = [-1, 1, -1, 1]
        for l in range(4): # 대각선 방향 별 반복
            for k in range(1, M): # 각 세기 별 반복
                i = y + (dy[l] * k)
                j = x + (dx[l] * k)
                if 0 <= i < N and 0 <= j < N:
                    Sum += arr[i][j]
        return Sum


    for i in range(N):
        for j in range(N):
            c_max = cross(i, j) + arr[i][j] # 정중앙 파리수 수 추가
            if Max < c_max:
                Max = c_max
            d_max = dia(i, j) + arr[i][j]
            if Max < d_max:
                Max = d_max

    print(f"#{test_case} {Max}")