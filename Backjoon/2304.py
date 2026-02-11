# N 개의 막대 기둥이 일렬로 세워져 있다. 기둥들의 폭은 모두 1 m이며 높이는 다를 수 있다.
# 이 기둥들을 이용하여 양철로 된 창고를 제작하려고 한다. 창고에는 모든 기둥이 들어간다.
# 이 창고의 지붕을 다음과 같이 만든다.
#
# 지붕은 수평 부분과 수직 부분으로 구성되며, 모두 연결되어야 한다.
# 지붕의 수평 부분은 반드시 어떤 기둥의 윗면, 수직 부분은 옆면과 닿아야한다.
# 어떤 부분도 오목하게 들어간 부분이 없어야 한다.
# 가장 작은 창고 다각형의 면적은?

N = int(input())

arr = [list(map(int,input().split())) for i in range(N)]

lst = [0]*(max(arr)[0]+1)
M = len(lst)

for i in range(N):
    lst[arr[i][0]]=arr[i][1]

top = max(lst)
st,ed = 0,0

s=0

for i in range(1,M):
    if lst[i] == top:
        st = i
        break
    if lst[i-1]>lst[i]:
        lst[i] = lst[i-1]
    s += lst[i]
s += lst[0]


for i in range(M-1,-1,-1):
    if lst[i] == top:
        ed = i
        break
    if lst[i-1]<lst[i]:
        lst[i-1] = lst[i]
    s += lst[i]

result = (ed-st+1)*top + s
print(result)