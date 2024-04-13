def find_all () :
    string = input("nhập kí tự cho chuỗi :")
    a = input("nhập kí tự cần tìm kiếm :")
    b = []
    for i in range(len(string)) :
        if string[i] == a :
            b.append(i)
    return b
ket_qua = find_all()
print(ket_qua)        
