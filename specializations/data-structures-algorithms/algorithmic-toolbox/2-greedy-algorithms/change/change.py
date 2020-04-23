# Uses python3
import sys

def get_change(m):
    n = 0
    while m > 9:
        m -= 10
        n += 1
    while m > 4:
        m -= 5
        n += 1
    while m > 0:        
        m -= 1
        n += 1
    return n

if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(get_change(n))
