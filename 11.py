str1 = input("nhập chuỗi thứ nhất :")
str2 = input("nhập chuỗi thứ hai :")
def so_sanh (str1, str2) :
    global a
    a = []
    for i in range(len(min(str1, str2))) :
        if str1[i] == str2[i] :
          a.append(i)
    return a
so_sanh(str1, str2)
b = so_sanh(str1, str2)      
print(f"số kí tự giống nhau là: {len(b)}")
print("vị trí ở :", b)