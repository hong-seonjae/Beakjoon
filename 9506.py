import math

while(True) :
    n = int(input())
    if (n == -1) : break 
    divisors_sum = 0
    num_list = []
   
    for i in range(1,n) : 
        if (n % i == 0) : 
            num_list.append(i)

    for j in num_list :
        divisors_sum += j
    if (divisors_sum != n) : print(n, "is NOT perfect.")
    else :
        result = " + ".join(map(str,num_list))
        print(n, "=", result)


