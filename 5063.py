# 첫째 줄에 테스트 케이스의 개수 N이 주어진다. 다음 N개의 줄에는 3개의 정수 r, e, c가 주어진다. 
# r은 광고를 하지 않았을 때 수익, e는 광고를 했을 때의 수익, c는 광고 비용이다. (-106 ≤ r,e ≤ 106, 0 ≤ c ≤ 106)

# e - r > c -> advertise
# e - r == c -> does not matter
# e - r < c -> do not advertise

t = int(input())

for _ in range(t) :
    r, e, c = map(int, input().split())
    
    if (e - r > c) : print("advertise")
    elif (e - r == c) : print("does not matter")
    else : print("do not advertise")