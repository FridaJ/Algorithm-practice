# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    previous = 0
    current = 1
    last_digit_fib = [0, 1]
    for i in range(2, n+1):
        current = (current + previous) % 10
        last_digit_fib.append(current)
        previous = last_digit_fib[i-1]
    return last_digit_fib[n]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
