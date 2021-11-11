n = int(input())
speed = [int(x) for x in input().split()]
speed = sorted(speed)

max_n = 1
i = 0
j = 0
while j < n:
    if speed[j] - speed[i] > 10:
        i += 1
    else:
        j += 1
    max_n = max(max_n, j-i)

print(max_n)