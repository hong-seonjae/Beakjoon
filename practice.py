# 알림을 약속 시간에 -45분을 한다.

H, M = map(int, input().split())

# 0 < H =< 23
# 0 < M =< 59

if (M - 45 < 0) :
    if (H <= 0) : 
        H+=23
    else :
        H-=1
        M += 60
    M -= 45
else :
    M -=45
    
print(H , M)    