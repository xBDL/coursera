# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    k = (right-left)//2
    le = get_majority_element(a, left, left+k)
    re = get_majority_element(a, left+k, right)
    lc, rc = 0, 0
    for i in range(left,right):
        if a[i] == le:
            lc += 1
        if a[i] == re:
            rc += 1
    if lc > k:
        return le
    elif rc > k:
        return re
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
