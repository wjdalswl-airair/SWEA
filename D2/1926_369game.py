# 369 게임
# 3,6,9가 들어가 있는 수는 '-'를 출력한다
# 박수 한 번 칠 떄는 -이며, 박수를 두번 칠 때는 --이다
# 예를 들어 35의 경우 박수 1번, 숫자 36의 경우 박수를 두번 쳐야 한다.

# 10 <= N <= 1000
# 1 ~ N까지의 숫자를 게임 규칙에 맞게 출력한다

N = int(input())
lst = []

for i in range(1, N + 1):
    lst.append(str(i)) # lst에 숫자 채우기

def game(value): # 먼저 3,6,9를 박수로 바꾼 후 '- + 숫자'의 경우 -로 바꿈
    value = value.replace('3', '-')
    value = value.replace('6', '-')
    value = value.replace('9', '-')
    for i in range(10):
        value = value.replace(str(i), '')
    return value

for i in range(N):
    if ('3' in lst[i]) or ('6' in lst[i]) or ('9' in lst[i]):
        lst[i] = game(lst[i]) # 3,6,9가 포함된 수는 함수에 넣기
    print(lst[i], end=" ")