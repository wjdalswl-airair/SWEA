# 1 이상 9 이하의 정수로 이루어진 수열 A와 B가 주어질 때, 수열 B가 A의 부분수열인지 확인
# 항상 A의 길이는 B의 길이보다 같거나 길다
# 1<=N<=15, 1<=M<=5

# import sys
# sys.stdin = open("sample_in.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    st = 0

    for i in range(M): # B의 모든 데이터를 검색
        flag = 0
        for j in range(st,N): # B와 같은 데이터의 다음 인덱스 부터 탐색
            if B[i] == A[j]:
                st =j+1
                flag =1 # 공통된 숫자가 있다면 표시
                break # 그 뒤는 볼 필요 x
        if flag == 0: # 만약 반복문을 다 돌았는데 맞는 숫자가 없었다면 탐색종료
            break

    if flag == 1:
        print(f"#{test_case} YES")
    else:
        print(f"#{test_case} NO")
