str1 = input("nhập chuỗi thứ nhất :")
str2 = input("nhập chuỗi thứ hai :")
def kiem_tra(str1, str2) :
    global i
    for i in range (min(len(str1), len(str2))) :
        if str1[i] != str2[i] :
          return i
    if str1 == str2 : 
     return -1
a = kiem_tra(str1, str2)
if a == -1 :
   print("hai chuoi giống nhau") 
else :
   print (f"vị trí khác nhau là: {i}")   

    