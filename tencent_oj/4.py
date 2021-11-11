n, t = [int(x) for x in input().split()]
tower = []
MAX = 2**(n+1)
for i in range(n):
    layer = []
    for j in range(i+1):
        layer.append(0)
    tower.append(layer)
for _ in range(t):
    tower[0][0] += MAX
    for layer in range(n):
        for i in range(layer+1):
            if tower[layer][i] >= MAX:
                extra = tower[layer][i] - MAX
                tower[layer][i] = MAX
                if layer + 1 < n:
                    tower[layer+1][i] += extra / 2
                    tower[layer+1][i+1] += extra / 2
res = 0
for i in range(n):
    for j in range(i+1):
        if tower[i][j] >= MAX:
            res += 1
print(res)