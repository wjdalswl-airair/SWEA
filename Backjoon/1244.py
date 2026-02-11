n = int(input())
lst = list(map(int,input().split()))

student = int(input())
arr = [list(map(int,input().split())) for i in range(student)]

def boy(index):








for i in range(student):
    if arr[i][0] == 1:
        boy(arr[i][1])
    elif arr[i][2] ==2:
        girl(arr[i][1])

print(*lst)

