# 버튼 A, B, C에 지정된 시간은 각각 5분, 1분, 10초이다.
# A = 5분, 300초
# B = 1분, 60초
# C = 10초


t = int(input())

A = 300
B = 60
C = 10

num_a = 0
num_b = 0
num_c = 0

while(t >= A) :
    t -= 300
    num_a += 1
while(t >= B) :
    t -= 60
    num_b += 1
while(t >= C) :
    t -= 10
    num_c +=1

if (t == 0) : print(num_a ,num_b ,num_c)
else : print(-1)