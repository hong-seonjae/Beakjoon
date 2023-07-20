from sympy import Integer

A, B = map(int, input().split())

result = Integer(A) + Integer(B)
print(result)
