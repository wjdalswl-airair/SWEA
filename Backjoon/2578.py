# 첫째 줄부터 다섯째 줄까지 빙고판에 쓰여진 수가 가장 위 가로줄부터 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다.
# 여섯째 줄부터 열째 줄까지 사회자가 부르는 수가 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다.
# 빙고판에 쓰여진 수와 사회자가 부르는 수는 각각 1부터 25까지의 수가 한 번씩 사용된다.
# 첫째 줄에 사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지 출력한다.

arr = [list(map(int,input().split())) for i in range(5)]
call = [list(map(int,input().split())) for i in range(5)]

def bingo(): # 빙고 검사
    result = [0,0,0,0,0]

    for i in range(5): # 가로 검사
        if arr[i] == result:
            return 1

    lst = list(map(list,zip(*arr))) # 세로 검사
    if lst == result:
        return 1

    for i in range(5): # 대각선 검사
        lst = []
        lst.append(arr[i][i])
    if lst == result:
        return 1

    for i in range(5): # 대각선 검사
        lst = []
        lst.append(arr[i][4-i])
    if lst == result:
        return 1



def check(y,x): # 부른 숫자를 0으로 만드는 함수
    for i in range(5):
        for j in range(5):
            if arr[i][j] == call[y][x]:
                arr[i][j] =0
                return

cnt = 0
flag = 0
for i in range(5):
    for j in range(5):
        cnt += 1
        check(i,j)
        if bingo()==1:
            flag =1
            break
    if flag == 1:
        break

print(cnt)
