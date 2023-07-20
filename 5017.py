N = int(input())

num_list = [0] * 5

for _ in range(N) :
    A, B = map(int, input().split())
    if (A > 0 and B > 0) :num_list[0] += 1
    elif (A < 0 and B > 0) : num_list[1] += 1
    elif (A < 0 and B < 0) : num_list[2] += 1
    elif (A > 0 and B < 0) : num_list[3] += 1
    else : num_list[4] += 1
print("Q1:",num_list[0])
print("Q2:",num_list[1])
print("Q3:",num_list[2])
print("Q4:",num_list[3])    
print("AXIS:",num_list[4])  