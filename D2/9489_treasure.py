# NxM 배열에서 고대 구조물이 있는 자리는 1, 빈 땅은 0으로 표시
# 직선인 구조물만 고려(교차/만나는 것처럼 보일 경우 무시)
# 가장 긴 구조물의 길이를 출력
# 3<= N,M <= 100


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]


    def treasure_row(y, x): # 가로로 검사
        Max = -21e8
        for i, j in (0, 1), (0, -1):
            cnt = 0
            for power in range(M):
                dy = y + i * power
                dx = x + j * power
                if 0 <= dy < N and 0 <= dx < M:
                    if arr[dy][dx] == 1:
                        cnt += 1
                        if Max < cnt:
                            Max = cnt
                    else:
                        break
        return Max


    def treasure_col(y, x): # 세로로 검사
        Max = -21e8
        for i, j in (1, 0), (-1, 0):
            cnt = 0
            for power in range(N):
                dy = y + i * power
                dx = x + j * power
                if 0 <= dy < N and 0 <= dx < M:
                    if arr[dy][dx] == 1:
                        cnt += 1
                        if Max < cnt:
                            Max = cnt
                    else:
                        break
        return Max


    Max = -21e8
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1: # 값이 1인 영역에 대해 가로, 세로로 모두 검사해 최대값 출력
                cnt = treasure_row(i, j)
                if Max < cnt:
                    Max = cnt
                cnt = treasure_col(i, j)
                if Max < cnt:
                    Max = cnt

    print(f"#{test_case} {Max}")
