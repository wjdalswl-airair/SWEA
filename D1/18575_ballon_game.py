# 보너스 스테이지 : NxN 격자에 숫자가 써진 풍선이 존재
# 어떤 풍선을 터트리면 같은 행과 열의 풍선이 모두 터진다.
# 같은 풍선 배치가 두 번 주어지며 각각 풍선을 하나씩 터트려 얻는 점수의 차이가 보너스 점수
# 보너스 스테이지가 주어졌을 때 얻을 수 있는 최대 보너스 점수를 출력
# 4<=N<=20
# 1<=Ai,j<=min(N,9)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    Max = -21e8
    Min = 21e8
    Max_result = -21e8

    for y in range(N):
        for x in range(N):
            s = 0
            for power in range(1, N): # +형태의 행과 열의 합 구하기
                for i, j in (0, 1), (0, -1), (1, 0), (-1, 0):
                    dy = y + i * power
                    dx = x + j * power
                    if 0 <= dy < N and 0 <= dx < N:
                        s += arr[dy][dx]
            if Max < s + arr[y][x]:
                Max = s + arr[y][x]
            if Min > s + arr[y][x]:
                Min = s + arr[y][x]
            score = Max - Min
            if Max_result < score:
                Max_result = score

    print(f"#{test_case} {Max_result}")