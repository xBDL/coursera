# Uses python3
import sys

def gcd(a, b):
    if b == 0:
        return a
    else:
        p = a % b
        return gcd(b, p) 

def lcm(a, b):
    return (a*b) // gcd(a,b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))