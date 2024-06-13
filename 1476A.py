t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    if n == k or n%k ==0:
        print(1)
    elif n == 1: #if n equals to one that means only one element then only non zero element divisible by k is k itself. 
        print(k)
    else:
        need = k - (n%k)
        if need <= n:
            print(2)
        else:
            if need%n == 0:
                print((need//n)+1)
            else:
                print((need//n)+2)
        
        

