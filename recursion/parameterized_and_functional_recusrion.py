### Parameterized recursion and Functional Recursion are to different methods to solve the problems


### Here we have a problem to find the sum og no. 1 to N we solve it with both methods


# 1. parameterized recursion

def parameterized_sum(sum,i,n):
    if i > n:
        print(sum)
        return
    parameterized_sum(sum + i, i + 1, n)


# 2. functional recursion

def functional_sum(n):
    if n == 1:
        return 1
    return n + functional_sum(n-1)

parameterized_sum(0, 1, 5)
f = functional_sum(5)
print(f)