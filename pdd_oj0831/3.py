T = int(input())
nums = [4, 7, 10, 12]
for i in range(5, 100000):
    import math
    a = int(math.sqrt(i))
    b = i - a*a
    x = 4+ 2* 3*(a-1) + 2*(a-1)*(a-1)
    if b <= a:
        x += (b>0)*3+ max(0, 2*(b-1))
    else:
        x += 3 + 2*(a-1) + 3 + 2*(b-a-1)
    nums.append(x)
    if x > 10000000000000000:
        break
print(nums[:10])
for _ in range(T):
    n = int(input())
    for i in range(len(nums)):
        if nums[i] > n:
            print(i)
            break