# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l
    return a*b


def lcm_efficient(a, b):
    small = min(a, b)
    large = max(a, b)
    n = 2
    mult = large
    while mult % small != 0:
        mult = large*n
        n+=1
    lcm = mult
    return lcm


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_efficient(a, b))

