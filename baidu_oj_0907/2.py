a, b, x, y = [int(x) for x in input().split()]
max_val = (a+b) //(x+y)
res = 0
# for m in range(max_val+1):
#     for n in range(max_val+1-m):
#         if m*x + n*y <= a and m * y + n * x <=b:
#             res = max(res, m+n)
#print((a+b) //(x+y))
for m in range(min(a//x, b//y)+1):
    for n in range(min((a-m*x)//y, (b-m*y)//x)+1):
        res = max(res, m + n)

print(res)