#!/usr/bin/python 


n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

mean_val = sum(a[:k])/k
max_val = max([mean_val] + a[k:])
min_val = min([mean_val] + a[k:])
res = max_val - min_val
print(mean_val, max_val, min_val)
for i in range(k, n):
    mean_val = (mean_val * k - a[i-k]+a[i]) / k
    if abs(max_val - a[i]) < 1e-7:
        max_val = max([mean_val] + a[:i-k+1] + a[i+1:])
    else:
        max_val = max(max_val, a[i-k], mean_val)
        
    if abs(min_val - a[i]) < 1e-7:
        min_val = min([mean_val] + a[:i-k+1] + a[i+1:])
    else:
        min_val = min(min_val, a[i-k], mean_val)
    res = min(res, max_val - min_val)

print(res)

