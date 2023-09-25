import random
while True:
    # Tạo một mảng 3D có 3 chỉ số
    D = [[[0 for k in range(4)] for j in range(3)] for i in range(3)]
    S = [[[0 for k in range(4)] for j in range(3)] for i in range(3)]
    # Tạo một danh sách giá trị
    values = [
        [   # Layer 0
            [1, 3, 4, 1],
            [3, 8, 2, 1],
            [3, 5, 4, 7]
        ],
        [   # Layer 1
            [4, 1, 1, 4],
            [2, 3, 9, 3],
            [9, 1, 2, 2]
        ],
        [   # Layer 2
            [8, 6, 3, 5],
            [4, 5, 8, 1],
            [99, 99, 99, 99]
        ]
    ]

        # Gán giá trị từ danh sách values vào mảng 3D
    for i in range(3):
        for j in range(3):
            for k in range(4):
                D[i][j][k] = values[i][j][k]
    D2 = [[[D[i][j][k] for k in range(4)] for j in range(3)] for i in range(3)]

    Cmax = 999
    Wmax = 999
    W = 0
    S2 = [[[0 for k in range(4)] for j in range(3)] for i in range(3)]
    # Thuật toán lựa chọn
    for i in range(3):
        for j in range(3):
            min = 99
            r = random.randint(0, 3)
            position = 1
            for k in range(r, 4):
                if D2[i][j][k] < min:
                    min = D2[i][j][k]
                    position = k
            for k in range(r):
                if D2[i][j][k] < min:
                    min = D2[i][j][k]
                    position = k
            S[i][j][position] = 1
            for x in range(j+1, 3):
                D2[i][x][position] = D2[i][x][position] + D[i][j][position]
            for y in range(i+1, 3):
                for x in range(3):
                    D2[y][x][position] = D2[y][x][position] + D[i][j][position]
    for k in range(4):
        S[2][2][k] = 0

    t = [0, 0, 0]
    m = [0, 0, 0, 0]
    Wk = [0, 0, 0, 0]
    for j in range(3):
        for i in range(3):
            for k in range(4):
                if S[i][j][k] == 1:
                    S2[i][j][k] = (max(t[i], m[k]), max(t[i], m[k]) + D[i][j][k])
                    t[i] = max(t[i], m[k]) + D[i][j][k]
                    m[k] = max(t[i], m[k])
                    Wk[k] = Wk[k] + D[i][j][k]
    if max(t) < Cmax:    
        Cmax = max(t)
    for i in range(4):
        W = W + Wk[i]
    if W < Wmax:
        Wmax = W
        print("W max :", Wmax)
    if Wmax == 14:
        for i in range(3):
            for j in range(3):
                print(f"S[{i+1}][{j+1}]:", S2[i][j])
        print("Tf = ", t)
        print("Wk = ", Wk)
        break
print("Cmax = ", Cmax)
print("Wmax = ", Wmax)
