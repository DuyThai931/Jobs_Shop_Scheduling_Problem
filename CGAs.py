import random
#------------------------------[FUNCTION]------------------------------------
#Xây dựng hàm đọc dữ liệu - READ DATA
def Data(value):
    nj = len(value)         #số Job
    no = len(value[0])      #Số thao tác mỗi Job
    nm = len(value[0][0])   #Số máy
    D = [[[0 for k in range(nm)] for j in range(no)] for i in range(nj)]
    for i in range(nj):
        for j in range(no):
            for k in range(nm):
                D[i][j][k] = value[i][j][k]
    return D


#Xây dựng hàm tìm kiếm địa phương - APPROACH BY LOCALIZATION
def gen(Data):
    x = len(Data)
    y = len(Data[0])
    z = len(Data[0][0])
    D2 = [[[D[i][j][k] for k in range(z)] for j in range(y)] for i in range(x)]
    S = [[[0 for k in range(z)] for j in range(y)] for i in range(x)]
    for i in range(x):
        for j in range(y):
            if min(D2[i][j]) >= 99:
                continue
            Min = 99
            r = random.randint(0, z-1)
            position = 1
            for k in range(r, z):
                if D2[i][j][k] < Min:
                    Min = D2[i][j][k]
                    position = k
            for k in range(r):
                if D2[i][j][k] < Min:
                    Min = D2[i][j][k]
                    position = k
            S[i][j][position] = 1
            for q in range(j+1, y):
                D2[i][q][position] = D2[i][q][position] + D[i][j][position]
            for w in range(i+1, x):
                for q in range(y):
                    D2[w][q][position] = D2[w][q][position] + D[i][j][position]
    return S
class JSP:
    def __init__(self, gen):
        self.gen = gen
    #Xây dựng biểu đồ kế hoạch - ASSIGNMENT SCHEMATA
    def schemata(self):
        S = self.gen
        x = len(S)
        y = len(S[0])
        z = len(S[0][0])
        t = [0]*x
        m = [0]*z
        Wk = [0]*z
        S2 = [[[0 for k in range(z)] for j in range(y)] for i in range(x)]
        for j in range(y):
            for i in range(x):
                for k in range(z):
                    if S[i][j][k] == 1:
                        S2[i][j][k] = (max(t[i], m[k]), max(t[i], m[k]) + D[i][j][k])
                        t[i] = max(t[i], m[k]) + D[i][j][k]
                        m[k] = max(t[i], m[k])
                        Wk[k] = Wk[k] + D[i][j][k]
        for i in range(x):
            for j in range(y):
                print(f"J{[i+1]}{[j+1]}:", S2[i][j])
    #Xây dựng hàm đánh giá - EVALUATION
    def makespans(self):
        S = self.gen
        x = len(S)
        y = len(S[0])
        z = len(S[0][0])
        t = [0]*x
        m = [0]*z
        Wk = [0]*z
        S2 = [[[0 for k in range(z)] for j in range(y)] for i in range(x)]
        for j in range(y):
            for i in range(x):
                for k in range(z):
                    if S[i][j][k] == 1:
                        S2[i][j][k] = (max(t[i], m[k]), max(t[i], m[k]) + D[i][j][k])
                        t[i] = max(t[i], m[k]) + D[i][j][k]
                        m[k] = max(t[i], m[k])
                        Wk[k] = Wk[k] + D[i][j][k]
        return max(t)
    def workloads(self):
        S = self.gen
        x = len(self.Data)
        y = len(self.Data[0])
        z = len(self.Data[0][0])
        t = [0]*x
        m = [0]*z
        Wk = [0]*z
        S2 = [[[0 for k in range(z)] for j in range(y)] for i in range(x)]
        for j in range(y):
            for i in range(x):
                for k in range(z):
                    if S[i][j][k] == 1:
                        S2[i][j][k] = (max(t[i], m[k]), max(t[i], m[k]) + D[i][j][k])
                        t[i] = max(t[i], m[k]) + D[i][j][k]
                        m[k] = max(t[i], m[k])
                        Wk[k] = Wk[k] + D[i][j][k]
            for i in range(x):
                W = W + Wk[i]
        return W
# Xây dựng quần thể
def chromosome(Data_Input,target,loop):
    nE = [[0 for k in range(2)] for j in range(target)]
    x = len(Data_Input)
    y = len(Data_Input[0])
    z = len(Data_Input[0][0])
    n = 0
    n_while = 0
    while n< target:
        if n == 0:
            nE[n][0] = gen(Data_Input)
            n = n+1
        else:
            size = 0
            compare = 0
            value = gen(Data_Input)
            for l in range(0,n):
                for i in range(x):
                    for j in range(y):
                        for k in range(z):
                            if value[i][j][k] == nE[l][0][i][j][k]:
                                size = size + 1
                if size == x*y*z:
                    compare = compare +1
                else:
                    size = 0
            if compare == 0:
                nE[n][0] = value
                n = n+1
            else:
                n_while = n_while + 1
        if n_while == loop:
            break
    E = [[0 for k in range(2)] for j in range(n)]
    for i in range(n):
        E[i][0] = nE[i][0]
    for i in range(n):
        a = JSP(E[i][0])
        E[i][1] = a.makespans()
    E1 = sorted(E, key=lambda tup: tup[1])
    return E1

#-----------------------------[MAIN]--------------------------------------------------------
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
D = Data(values)    #Đưa dữ liệu vào mảng D
E = chromosome(D,10,1000)    #Xây dựng quần thể (bộ nhiễm sắc thể choromosome(dữ liệu vào, số lượng gen mong muốn, số vòng lặp random))
for i in range(len(E)):
    print(f"S{[i+1]}:\n", E[i])
print("--------------------------------")
E1 = JSP(E[0][0])    #Xây dựng các đặc tính của gen
E11 = E1.schemata()  #In ra bảng lược đồ kế hoạch
#-----------------------------[END]---------------------------------------------------------