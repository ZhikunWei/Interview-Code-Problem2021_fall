n, q = [int(x) for x in input().split()]
deps = {}
states = [0] * (n+1)
stop_table = {}
for i in range(1, n+1):
    stop_table[i] = []
for i in range(n):
    line = [int(x) for x in input().split()]
    deps[i+1] = line[1:]
    for node in line[1:]:
        stop_table[node].append(i+1)


def op(node, signal, visited):
    if visited[node] == 1:
        return
    visited[node] = 1
    if signal == 0:
        states[node] = 0
        for sub_node in stop_table[node]:
            op(sub_node, signal, visited)
    elif signal == 1:
        states[node] = 1
        for sub_node in deps[node]:
            op(sub_node, signal, visited)
    
    

for i in range(q):
    x, y = [int(x) for x in input().split()]
    visited = [0] * (n+1)
    op(y, x, visited)

    print(sum(states))
