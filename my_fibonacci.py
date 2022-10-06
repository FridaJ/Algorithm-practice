# Uses python3

def calc_fib(n):
    fib_num = [0, 1]
    for i in range(2, n+1):
        new = fib_num[i-1] + fib_num[i-2]
        fib_num.append(new)
    return fib_num[n]


n = int(input())
print(calc_fib(n))
