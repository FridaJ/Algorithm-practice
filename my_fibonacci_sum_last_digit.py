# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    _sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10


def get_fibonacci_huge_efficient(n, m):
#output should be Fn mod m

    if n <= 1:
        return n

    prev_mod = 0
    curr_mod = 1
    for i in range(2, 4*n):
        prev_mod, curr_mod = curr_mod, (prev_mod + curr_mod) % m
        per = i-1  # per is Pisano period, always starts with 0,1
        if prev_mod == 0 and curr_mod == 1:
            break

    rest = n % per #result 1 means first number in period sequence, result 4 means 4th number in the period
    #only need to check fib numbers up to index per ()

    fib_num_mod = [0, 1]
    for i in range(2, rest+1):
        new = (fib_num_mod[i - 1] + fib_num_mod[i - 2]) % m
        fib_num_mod.append(new)

    ans = fib_num_mod[rest] #same as F(n) % m mathematically
    return ans


def fibonacci_sum_efficient(n):

    m = 10 # last digit means modulo 10

# use the formula for the sum of Fib numbers: Fib_sum(n) = Fib(n+2) - 1
    fib_sum = get_fibonacci_huge_efficient(n+2, m) - 1
    fib_sum_mod = fib_sum % m # m = 10 if analyzing last digit

    return fib_sum_mod


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_efficient(n))
