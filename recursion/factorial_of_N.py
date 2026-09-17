### Find the factorial of a given number

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

f = fact(5)
print(f)


## Using parameterized recursion


def fact1(ans, i, n):
    if i > n:
        print(ans)
        return
    fact1(ans * i, i+1, n)

fact1(1, 1, 5)