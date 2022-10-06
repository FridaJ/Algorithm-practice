# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


# Try formula sum = F(n-1)/F(n) * F(n+1)^2

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


def fibonacci_sum_squares_efficient(n):

    m = 10  # last digit means modulo 10

    # Otherwise, use the formula for the sum of squared Fib numbers as a rectangle area:
    # A = Fib(n) * (Fib(n+1))

    fib_n_mod = get_fibonacci_huge_efficient(n, m) # Last digit of n
    fib_next_mod = get_fibonacci_huge_efficient(n+1, m)  # Last digit of n+1
    fib_sum_mod = (fib_n_mod * fib_next_mod) % m # Last digit of sum of squares

    return fib_sum_mod


if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_efficient(n))
