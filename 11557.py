t = int(input())
 
for _ in range(t) :
    univ_list = []
    univ_num_list = []
    max_value = 0
    s = int(input())
    for _ in range(s) :
        A,B = input().split()
        univ_list.append(A)
        univ_num_list.append(int(B))
        
        num = 0

    max_value = max(univ_num_list)
    
    for i in univ_num_list :
        if max_value == i :
            num == int(i)   
        
    print(univ_list[num])
