# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

x = max(a)
a.remove(x)
y = max(a)
result = x*y           

print(result)