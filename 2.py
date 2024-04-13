# không thay đổi chuỗi cũ
chuoi = input("nhap chuoi :")
lst = [i for i in chuoi]
print(lst)
def add_excitement (lst) :
    for i in lst :
        print (i + "!" + "\t", end ="") 
add_excitement(lst)  
# trả lại chuỗi mới
x = []
def add_excitement2 (lst) :
    global x 
    for i in lst :
      b =  str (i + "!" )
      x.append(b)
    print(x)      
add_excitement2(lst)
