from math import sqrt

def calc_factore(num):
    ## Brute Force approach TC -> O(N)
    result = []
    for i in range(1, num+1):
        if num % i == 0:
            result.append(i)
    return result

def calc_factore_better(num):
    ## Better Approach
    result = []
    for i in range(1,num//2 + 1): ## TC -> O(N/2)
        if num % i == 0:
            result.append(i)
    result.append(num)
    return result

def calc_factore_optimal(num):
    ## Optimal Approach TC -> O(sqrt(N))
    res = []
    for i in range(1,int(sqrt(num))):
        remander = 0
        if num % i == 0:
            remander = num // i
            res.append(i)
            res.append(remander)
    res.append(int(sqrt(num)))
    return res

num = int(input("Enter your number: "))
C = calc_factore_optimal(num)
print(C)