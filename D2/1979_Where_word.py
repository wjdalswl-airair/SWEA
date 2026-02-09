# NxN 크기의 단어퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다
# 주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력
# 5 <= N <= 15
# 2 <= K <= N
# 퍼즐의 각 셀 중 흰색 부분은 1, 검은색 부분은 0

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, k = map(int, input().split())
    past_arr = [list(map(int, input().split())) for i in range(N)]
    arr = [[0] * (N + 2) for i in range(N + 2)]
    for i in range(N): # 0으로 padding
        arr[i + 1] = [0] + past_arr[i] + [0]

    cnt = 0
    correct = [0] + [1] * k + [0] # 정답 배열을 padding

    for i in range(1, N + 1): # 가로로 검사
        for j in range(0, N + 1 - k):
            if arr[i][j:j + k + 2] == correct:
                cnt += 1

    for i in range(1, N + 1): # 세로로 검사
        for j in range(0, N + 1 - k):
            col = []
            for y in range(k + 2):
                col.append(arr[j + y][i]) # 세로 배열 만들기
            if col == correct:
                cnt += 1

    print(f"#{test_case} {cnt}")