T = int(input())
for _ in range(T):
    t = int(input())
    pi = [float(x) for x in input().split()]
    P = []
    for ___ in range(3):
        P.append([float(x) for x in input().split()])
    
    for __ in range(t):
        new_pi = []
        for i in range(3):
            new_pi.append(pi[0] * P[i][0] + pi[1] * P[i][1] + pi[2] * P[i][2])
        pi = new_pi
    print(int(pi[2] > 0.5))
