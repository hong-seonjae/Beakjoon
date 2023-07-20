#long int 4bit 
#long long int 8bit

N = int(input())
count = 0

N_list = ["long", "int"]

if (N == 4) :
    print("long int")
else :
    while(N < 0) :
        N /= 4
        count += 1
    
print(count)