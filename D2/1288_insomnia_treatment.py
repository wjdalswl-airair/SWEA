# N의 배수 번호인 양을 셀 때
# 이전에 셌던 번호들의 각 자리수에서 0에서 9까지의 모든 숫자를 보는 것은 최소 몇 번 양을 센 시점일까?
# ex. N = 1295 일 때 5N번 양을 세면 0에서 9까지 모든 숫자를 보게 됨

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N =input()
    result =set(N) # 숫자가 중복되지 않도록 set 처리
    i = 0
    Next = N
    while True:
        Next_value = set(Next)
        result.update(Next_value) # 정답 set에 다음번 양의 숫자 추가
        if len(result) == 10: # 정답 set가 0~9를 모두 가지고 있을 시 반복문 종료
            print(f"#{test_case} {Next}")
            break
        else:
            i += 1
            Next = str(int(N)*i) # 양의 숫자의 배수를 Next로 설정