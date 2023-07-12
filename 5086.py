# 첫 번째 숫자가 두 번째 숫자의 약수이다.
# 첫 번째 숫자가 두 번째 숫자의 배수이다.
# 첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다.

while (True) :
    A, B = map(int, input().split())

    if (A == 0 and B == 0) :break

    if (A % B == 0) : print("multiple")
    elif (B % A == 0) : print("factor")
    else : print("neither")