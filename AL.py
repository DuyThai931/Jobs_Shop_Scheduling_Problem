import random
import openpyxl

# Tạo một mảng 3D có 3 chỉ số
D = [[[0 for k in range(8)] for j in range(4)] for i in range(8)]

# Tạo một danh sách giá trị

values = [
    [   # Job 1
        [5, 3, 5, 3, 3, 99, 10, 9],
        [10, 99, 5, 8, 3, 9, 9, 6],
        [99, 10, 99, 5, 6, 2, 4, 5],
        [99, 99, 99, 99, 99, 99, 99, 99]
    ],
    [   # Job 2
        [5, 7, 3, 9, 8, 99, 9, 99],
        [99, 8, 5, 2, 6, 7, 10, 9],
        [99, 10, 99, 5, 6, 4, 1, 7],
        [10, 8, 9, 6, 4, 7, 99, 99]
    ],
    [   # Job 3
        [10, 99, 99, 7, 6, 5, 2, 4],
        [99, 10, 6, 4, 8, 9, 10, 99],
        [1, 4, 5, 6, 99, 10, 99, 7], 
        [99, 99, 99, 99, 99, 99, 99, 99]
    ],
    [   # Job 4
        [3, 1, 6, 5, 9, 7, 8, 4],
        [12, 11, 7, 8, 10, 5, 6, 9],
        [4, 6, 2, 10, 3, 9, 5, 7], 
        [99, 99, 99, 99, 99, 99, 99, 99]
    ],
    [   # Job 5
        [3, 6, 7, 8, 9, 99, 10, 99],
        [10, 99, 7, 4, 9, 8, 6, 99],
        [99, 9, 8, 7, 4, 2, 7, 99], 
        [11, 9, 99, 6, 7, 5, 3, 6]
    ],
    [   # Job 6
        [6, 7, 1, 4, 6, 9, 99, 10],
        [11, 99, 9, 9, 9, 7, 6, 4],
        [10, 5, 9, 10, 11, 99, 10, 99], 
        [99, 99, 99, 99, 99, 99, 99, 99]
    ],
    [   # Job 7
        [5, 4, 2, 6, 7, 99, 10, 99],
        [99, 9, 99, 9, 11, 9, 10, 5],
        [99, 8, 9, 3, 8, 6, 99, 10], 
        [99, 99, 99, 99, 99, 99, 99, 99]
    ],
    [   # Job 8
        [2, 8, 5, 9, 99, 4, 99, 10],
        [7, 4, 7, 8, 9, 99, 10, 99],
        [9, 9, 99, 8, 5, 6, 7, 1], 
        [9, 99, 3, 7, 1, 5, 8, 99]
    ]
]

    # Gán giá trị từ danh sách values vào mảng 3D
for i in range(8):
    for j in range(4):
        for k in range(8):
            D[i][j][k] = values[i][j][k]
Cmax = 999
Wmax = 999
W = 0
for e in range(100000):
    D2 = [[[D[i][j][k] for k in range(8)] for j in range(4)] for i in range(8)]
    S = [[[0 for k in range(8)] for j in range(4)] for i in range(8)]
    S2 = [[[0 for k in range(8)] for j in range(4)] for i in range(8)]
    # Thuật toán lựa chọn
    for i in range(8):
        for j in range(4):
            if min(D2[i][j]) >= 99:
                continue
            Min = 99
            r = random.randint(0, 7)
            position = 1
            for k in range(r, 8):
                if D2[i][j][k] < Min:
                    Min = D2[i][j][k]
                    position = k
            for k in range(r):
                if D2[i][j][k] < Min:
                    Min = D2[i][j][k]
                    position = k
            S[i][j][position] = 1
            for x in range(j+1, 4):
                D2[i][x][position] = D2[i][x][position] + D[i][j][position]
            for y in range(i+1, 8):
                for x in range(4):
                    D2[y][x][position] = D2[y][x][position] + D[i][j][position]
    t = [0, 0, 0, 0, 0, 0, 0, 0]
    m = [0, 0, 0, 0, 0, 0, 0, 0]
    Wk = [0, 0, 0, 0, 0, 0, 0, 0]
    for j in range(4):
        for i in range(8):
            for k in range(8):
                if S[i][j][k] == 1:
                    S2[i][j][k] = (max(t[i], m[k]), max(t[i], m[k]) + D[i][j][k])
                    t[i] = max(t[i], m[k]) + D[i][j][k]
                    m[k] = max(t[i], m[k])
                    Wk[k] = Wk[k] + D[i][j][k]
    if max(t) < Cmax:    
        Cmax = max(t)
    if Cmax == 16:
        for i in range(8):
            W = W + Wk[i]
        if W < Wmax:
            Wmax = W
        if Wmax == 83:
            break
for i in range(8):
    for j in range(4):
        print(f"S[{i+1}][{j+1}]:", S2[i][j])
print("Time per Job:", t)
print("Workloads per Machine:", Wk)
print("Makespan-Cmax = ", Cmax)
print("Total Workloads-Wmax = ", Wmax)
