n = int(input())
mat = []
for _ in range(n):
    mat.append([int(x) for x in input().split()])
    
def print_mat():
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end=' ')
        print()
    print()

def explore(x, y):
    global mat
    print(x, y)
    print_mat()
    # if mat[x][y] == 2:
    #     return True
    if mat[x][y] == 1:
        return True
    if x - 1 < 0 or x + 1 >= n or y - 1 < 0 or y + 1 >= n:
        return False
    mat[x][y] = 2
    s1, s2, s3, s4 = True, True, True, True
    if x - 1 >= 0 and mat[x - 1][y] != 2:
        s1 = explore(x - 1, y)
    if x + 1 < n and mat[x + 1][y] != 2:
        s2 = explore(x + 1, y)
    if y - 1 >= 0 and mat[x][y - 1] != 2:
        s3 = explore(x, y - 1)
    if y + 1 < n and mat[x][y + 1] != 2:
        s4 = explore(x, y + 1)
    if not(s1 and s2 and s3 and s4):
        mat[x][y] = 0
        print(x, y)
        print_mat()
        return False
    else:
        return True


for i in range(n):
    for j in range(n):
        print('###',i, j)
        explore(i, j)
        print('~~~~~~~~~~~~~~~~~~~~~~~~')
        
