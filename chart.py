def Read_Data(filename='data.txt'):
    # Khởi tạo mảng để lưu dữ liệu
    data_rows = []
    # Đọc từng dòng của tệp và thêm vào mảng data_rows
    with open(filename, 'r') as file:
        for line in file:
            # Tách các giá trị trong dòng và chuyển thành số nguyên
            row = list(map(int, line.strip().split()))
            data_rows.append(row)
    # Chuyển mảng thành mảng NumPy
    structure = [[[0 for i in range(data_rows[0][2])] for j in range(data_rows[0][1])] for k in range(data_rows[0][0])]
    print(len(data_rows))
    for i in range(len(data_rows)-1):
        print(f'vong {i}')
        no = 1
        print(data_rows[i+1][0])
        for j in range(data_rows[i+1][0]):
            for k in range(no + 1,2*data_rows[i+1][no]+no,2):
                structure[i][j][data_rows[i+1][k]-1] = data_rows[i+1][k+1]
            no = no + 2*data_rows[i+1][no]+1
    for i in range(len(structure)):
        for j in range(len(structure[i])):
            for k in range(len(structure[i][j])):
                if structure[i][j][k] == 0:
                    structure[i][j][k] = 99
    return structure
# Sử dụng hàm Read_Data để đọc dữ liệu từ tệp 'data.txt'
data_array = Read_Data('mk3.txt')

