# 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다.
# 설탕 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
# 정확하게 N킬로그램 배달해야 할 때, 봉지의 최소 개수를 구하시오

# N = int(input())
# lst = [3,5]
# Min= 21e8
# cnt = 0
# def sugar(level,Sum):
#     global Min, cnt
#
#     if Sum > N: # N Kg이 넘었다면 백트래킹
#         return
#
#     if level > Min: # 최소가 아니라면 백트래킹
#         return
#
#     if Sum == N:
#         if Min > level:
#             Min = level # level 은 봉지의 개수와 같다
#         return
#
#     for i in range(2):
#         sugar(level+1,Sum+lst[i])
#
# sugar(0,0)

# if Min == 21e8:
#     print(-1)
# else:
#     print(Min)



N = int(input())
cnt=0
while N>0:
    if N%5 == 0: # 5 Kg 봉지가 최대가 되도록
        cnt += N//5
        print(cnt)
        break
    else:
        N = N-3
        cnt += 1
        if N==0:
            print(cnt)
            break
else:
    print(-1)



