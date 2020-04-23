# Uses python3
import sys

def get_fibonacci_last_digit(n):
    F = list(range(n+1))
    for i in range(2,n+1):
        F[i] = (F[i-1] + F[i-2]) % 10
    return F[n]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))