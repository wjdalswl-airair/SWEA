# 홀수 날에는 물을 준 나무는 키가 1만큼 자라고, 짝수 날에 물을 준 나무는 키가 2만큼 자란다
# 어떤 날에는 물을 주지 않을 수도 있다.
# 모든 나무의 키가 초기의 키가 가장 컸던 나무와 같아지도록 만들기 위한 최소 날짜 수

import sys
sys.stdin = open("input.txt",'r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    trees = list(map(int,input().split()))

    target = max(trees)

    one,two = 0,0
    for i in range(N):
        two += (target - trees[i])//2
        one += (target - trees[i])%2

    day = 0
    while True:
        odd = (day+1)//2
        even = day//2

        if one <= odd:
            lack = max(0,two-even)
            if 2*lack <= (odd-one):
                break

        day+=1

    print(f"#{tc} {day}")