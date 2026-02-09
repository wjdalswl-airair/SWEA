# N개의 숫자로 구성된 숫자열 A와 M개의 숫자로 구성된 숫자열 B
# A와 B의 마주보는 위치를 변경하여 서로 마주보는 숫자들을 곱한 뒤 모두 더할 떄의 최댓값을 구하라
# 단, 더 긴 쪽의 양끝을 벗어나서는 안된다.
# 3<= N,M<=20


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    if N > M: # 항상 Bj의 길이가 더 길도록 한다.
        N, M = M, N
        Ai, Bj = Bj, Ai

    MAX = -21e8

    for i in range(M + 1 - N): # Ai를 1칸씩 이동시키며 반복
        s = 0
        arr = [0] * M
        result = [0] * M
        for j in range(N): # M개의 배열에 N개의 숫자 입력하기
            arr[j + i] = Ai[j]
        for k in range(M):
            result[k] = arr[k] * Bj[k]
            s += result[k] # 곱의 총합 구하기
        if MAX < s: # 최댓값 구하기
            MAX = s

    print(f"#{test_case} {MAX}")