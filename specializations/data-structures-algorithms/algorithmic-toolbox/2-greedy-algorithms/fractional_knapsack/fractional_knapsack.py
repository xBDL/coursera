# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    items = []
    for i in range(n):
        v = values[i]
        w = weights[i]
        p = v / w
        items.append((p,v,w))
    items.sort()
    while capacity > 0:
        if items == []:
            break
        best = items[-1]
        if capacity < best[2]:
            value += best[0]*capacity
            break
        else:
            value += best[1]
            capacity -= best[2]
            items = items[:-1]
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
