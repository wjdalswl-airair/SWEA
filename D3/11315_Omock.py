# N X N 크기의 판이 있다. 판의 각 칸에는 돌이 있거나 없을 수 있다. 돌이 가로, 세로, 대각선 중 하나의 방향으로 다섯 개 이상 연속한 부분이 있는지 없는지 판정하는 프로그램을 작성하라.
# 5<=N<=20
# 각 문자는 'o' 또는 '.' 으로 'o'는 돌이 있는 칸을 의미하고 '.'는 돌이 없는 칸을 의미한다ㅏ
# 돌이 다섯 개 이상 연속한 부분이 있으면 'YES'를, 아니면 'NO'를 출력한다.


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    arr = [list(input()) for i in range(N)]
    result = 0


    def omock(y, x):
        p = 0
        for i, j in (1, 0), (-1, 1), (1, -1), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1): # 각 방향에 대해 검사 반복
            for power in range(1, 5):
                dy = y + i * power
                dx = x + j * power
                if 0 <= dy < N and 0 <= dx < N:
                    if arr[dy][dx] == 'o': # 가까운 영역이 'o'라면 검사 계속
                        p = power
                    else: # '.'가 발견되면 검사 중지
                        break
            if p == 4: # 연속된 'o'가 4개라면 오목 발견
                return 1
        return 0


    for y in range(N):
        for x in range(N):
            if arr[y][x] == 'o':
                result = omock(y, x)
                if result == 1:
                    break
        if result == 1:
            break

    if result == 1:
        print(f"#{test_case} YES")
    else:
        print(f"#{test_case} NO")