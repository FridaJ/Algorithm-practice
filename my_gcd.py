# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d
    return current_gcd


def gcd_efficient(a, b):
    gcd = 1
    a, b = max(a, b), min(a, b)
    while a % b != 0:
        a, b = b, a % b
    gcd = b
    return gcd


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_efficient(a, b))
