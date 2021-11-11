N = int(input())
strs = []
for _ in range(N):
    s = input()
    s1 = ''
    for i in range(len(s)//2+1):
        s1 += min(s[i], s[len(s)-i-1])
    strs.append((s, s1))
res = sorted(strs, key=lambda x: x[1])
for x in res:
    print(x[0])