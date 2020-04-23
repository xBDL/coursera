# Uses python3
import sys

def get_fibonaccihuge(n, m):
    p = 1
    F = [0,1]
    if m==2:
        p = 3        
    else:
        for i in range(2,m**3):
            F.append((F[i-1] + F[i-2]) % m)
            if (F[-2:]==[0,1]):
                p = len(F) - 2
                break
    r = n % p
    return (F[r])

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonaccihuge(n, m))
