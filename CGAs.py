import random
import copy
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
# cach tao gen 2
def gen2(Data):
    x = len(Data)
    y = len(Data[0])
    z = len(Data[0][0])
    D_2 = [[[D[i][j][k] for k in range(z)] for j in range(y)] for i in range(x)]
    S_2 = [[[0 for k in range(z)] for j in range(y)] for i in range(x)]
    w = 1
    while w <= x*y:
        min = 99
        r = random.randint(0,z-1)
        PositionK = r
        for i in range(len(D_2)):
            for j in range(len(D_2[i])):
                for k in range(r, z):
                    if D_2[i][j][k] < min and D_2[i][j][k] != 0:
                        min = D_2[i][j][k]
                        PositionK = k
                        PositionI = i
                        PositionJ = j
                for k in range(0,r):
                    if D_2[i][j][k] < min and D_2[i][j][k] != 0:
                        min = D_2[i][j][k]
                        PositionK = k
                        PositionI = i
                        PositionJ = j
        if min < 99:
            S_2[PositionI][PositionJ][PositionK] = 1
        D_2[PositionI][PositionJ] = [0 for i in range(len(D_2[0][0]))]
        for i in range(len(D_2)):
            for j in range(len(D_2[i])):
                if D_2[i][j][PositionK] != 0:
                    D_2[i][j][PositionK] = D_2[i][j][PositionK] + Data[PositionI][PositionJ][PositionK]
        w += 1
    return S_2
#Ham danh gia
class JSP:
    def __init__(self,gen,job_priority):
        self.gen = gen
        self.job_priority = job_priority
        self.time_per_job = None
        self.workload_per_machine = None
        self.schemata = None
    #Xây dựng biểu đồ kế hoạch - ASSIGNMENT SCHEMATA
        S = gen
        jp = job_priority
        x = len(S)
        y = len(S[0])
        z = len(S[0][0])
        t = [0]*x
        m = [0]*z
        Wk = [0]*z
        S2 = [[[0 for k in range(z)] for j in range(y)] for i in range(x)]
        for j in range(y):
            E1 = [0 for _ in range(x)]
            for i in range(jp,x):
                for k in range(z):
                    if S[i][j][k] == 1:
                        E1.append([i, k, D[i][j][k]])
            for i in range(0,jp):
                for k in range(z):
                    if S[i][j][k] == 1:
                        E1.append([i, k, D[i][j][k]])
            E1 = [item for item in E1 if item != 0]
            E1 = sorted(E1, key=lambda x: x[2])
            for r in range(len(E1)):
                i = E1[r][0]
                k = E1[r][1]
                S2[i][j][k] = (max(t[i], m[k]), max(t[i], m[k]) + D[i][j][k])
                t[i] = max(t[i], m[k]) + D[i][j][k]
                m[k] = max(t[i], m[k])
                Wk[k] = Wk[k] + D[i][j][k]
        self.time_per_job = t
        self.workload_per_machine = Wk
        self.schemata = S2
    def show_schemata(self):
        SS = self.schemata
        for i in range(len(SS)):
            for j in range(len(SS[0])):
                print(f"J{[i+1]}{[j+1]}:", SS[i][j])
    def makespans(self):
        max_t = max(self.time_per_job)
        return max_t
    def processing_time(self):
        return self.time_per_job
    def workloads(self):
        Workload = self.workload_per_machine
        return sum(Workload)
    def workloads_per_machine(self):
        return self.workload_per_machine
# Xay dung quan the
def chromosome(Data_Input,loop):
    nE = []
    n = 0
    n2 = 0
    while n < loop:
        EE = []
        EE = gen(Data_Input)
        if EE not in nE :
            nE.append(EE)
            n = 0
        else:
            n += 1
    while n2 < loop:
        EE = []
        EE = gen2(Data_Input)
        if EE not in nE :
            nE.append(EE)
            n2 = 0
        else:
            n2 += 1
    E = [[0 for k in range(2)] for j in range(len(nE))]
    for i in range(len(nE)):
        E[i][0] = nE[i]
        a = JSP(E[i][0],0)
        E[i][1] = a.makespans()
    E1 = sorted(E, key=lambda tup: tup[1])
    return E1
#Xay dung ham Crossover
def crossover(D,E):
    a = random.randint(0,len(E)-1)
    b = random.randint(0,len(E)-1)
    while a == b:
        b = random.randint(0,len(E)-1)
    S1 = E[a][0]
    S2 = E[b][0]
    # Lựa chọn vị trí lai ghép
    i1 = i2 = j1 = j2 = 0
    while i1 > i2:
        i1 = random.randint(0,len(D)-1)
        i2 = random.randint(0,len(D)-1)
        j1 = random.randint(0,len(D[0])-1)
        j2 = random.randint(0,len(D[0])-1)
        while i1 == i2 and j1 > j2:
            j1 = random.randint(0,len(D[0])-1)
            j2 = random.randint(0,len(D[0])-1)
    C1 = [[[0 for k in range(len(D[0][0]))] for j in range(len(D[0]))] for i in range(len(D))]
    C2 = [[[0 for k in range(len(D[0][0]))] for j in range(len(D[0]))] for i in range(len(D))]
    for a in range(0, i1):
        C1[a] = S2[a]
        C2[a] = S1[a]
    for a in range(i1+1, i2):
        C1[a] = S1[a]
        C2[a] = S2[a]
    for a in range(i2+1, len(D)):
        C2[a] = S1[a]
        C1[a] = S2[a]
    if i1 < i2:
        for b in range(0,j1):
            C1[i1][b] = S2[i1][b]
            C2[i1][b] = S1[i1][b]
        for b in range(j1,len(D[0])):
            C1[i1][b] = S1[i1][b]
            C2[i1][b] = S2[i1][b]
        for b in range(0,j2+1):
            C1[i2][b] = S1[i2][b]
            C2[i2][b] = S2[i2][b]
        for b in range(j2+1,len(D[0])):
            C1[i2][b] = S2[i2][b]
            C2[i2][b] = S1[i2][b]
    if i1 == i2:
        for b in range(0,j1):
            C1[i1][b] = S2[i1][b]
            C2[i1][b] = S1[i1][b]
        for b in range(j1,j2+1):
            C1[i1][b] = S1[i1][b]
            C2[i1][b] = S2[i1][b]
        for b in range(j2+1,len(D[0])):
            C1[i2][b] = S2[i2][b]
            C2[i2][b] = S1[i2][b]
    return [C1,C2]
# Xây dựng hàm đột biến
def mutation1(E,D):
    a = random.randint(0,len(E)-1)
    S = E[a][0]
    value_S = JSP(S,0)
    t = value_S.processing_time()
    max_pt = max(t)
    i = t.index(max_pt)
    r = 0
    j = 0
    while j < len(S[0]) and r == 0:
        position = 0
        for k in range(len(S[0][0])):
            if S[i][j][k] == 1:
                position = k
        for k in range(len(S[0][0])):
            if D[i][j][k] < D[i][j][position]:
                S[i][j][position] = 0
                S[i][j][k] = 1
                r = 1
        j += 1
    return S
# Xây dựng hàm đột biến 2
def mutation2(E):
    a = random.randint(0,len(E)-1)
    S = E[a][0]
    value_S = JSP(S,0)
    w = value_S.workloads_per_machine()
    max_wl = max(w)
    indices_of_max = [o for o, x in enumerate(w) if x == max_wl]
    min_wl = min(w)
    indices_of_min = [o for o, x in enumerate(w) if x == min_wl]
    k1 = random.choice(indices_of_max)
    k2 = random.choice(indices_of_min)
    r = 0
    while r == 0:
        i = random.randint(0,len(S)-1)
        position = random.randint(0,len(S[0])-1)
        for j in range(position,len(S[0])):
            if S[i][j][k1] == 1:
                r = 1
                positioni = i
                positionj = j
            else:
                r = 0
        if r == 0:
            for j in range(0, position):
                if S[i][j][k1] == 1:
                    r = 1
                    positioni = i
                    positionj = j
                else:
                    r = 0
    S[positioni][positionj][k1] = 0
    S[positioni][positionj][k2] = 1
    return S
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
#Lựa chọn kích thước quần thể
D = Data(values)    #Đưa dữ liệu vào mảng D
E = chromosome(D,10000)    #Xây dựng quần thể (bộ nhiễm sắc thể choromosome(dữ liệu vào, số lượng gen mong muốn, số vòng lặp random))
print(len(E))
print("______________________________")
n = 20
c = 10
m1 = 5
m2 = 5
x = 1
#Lựa chọn quần thể
Q = E[:n]
#Lai ghép
while x <= 1000:
    QQ = copy.deepcopy(Q)
    #Đột biến kiểu 1
    M1 = [0 for j in range(m1)]
    for i in range(m1):
        M1[i] = mutation1(Q,D)
    #Đột biến kiểu 2
    M2 = [0 for j in range(m2)]
    for i in range(m2):
        M2[i] = mutation2(Q)
    #Lai ghép
    C1 = [0 for j in range(c)]
    for i in range(0,c,2):
        F = crossover(D,Q)
        C1[i] = F[0]
        C1[i+1] = F[1]
    #Gộp các tổ hợp
    C1.extend(M1)
    C1.extend(M2)
    # Tạo mảng Q2 bao gồm cả chỉ số đánh giá Makespans
    Q2 = [[0 for j in range(2)] for k in range(n)]
    for i3 in range(len(Q2)):
        Q2[i3][0] = C1[i3]
        Q2[i3][1] = JSP(C1[i3],0).makespans()
    # Gộp G2 vào tập quần thể ban đầu
    Q2.extend(QQ)
    # Sắp xếp các phần tử tỏng Q2 theo thứ tự tăng dần Cmax
    QQ2 = sorted(Q2, key=lambda tup: tup[1])
    # Loại bỏ các phần tử giống nhau trong QQ2 lưu vào QQ3
    QQ3 = []
    for element in QQ2:
        if element not in QQ3:
            QQ3.append(element)
    # Lấy n phần tử đầu của QQ3 thay vào Q
    Q = QQ3[:n]
    x += 1
for i in range(len(Q)):
    print(Q[i])
print("__________________________ASSIGNMENT_______________________")
Assignment = Q[0][0]
for i in range(len(Assignment)):
    for j in range(len(Assignment[0])):
        print(f"O[{i+1}][{j+1}]",Assignment[i][j])
print("________________________SCHEMATE GEN 1_____________________")
JSP(Assignment,0).show_schemata()
#-----------------------------[END]---------------------------------------------------------