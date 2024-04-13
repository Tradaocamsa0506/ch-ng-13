total = []

def nhap_ds () :
    global total, n 
    a = int(input("bạn muốn nhập bao nhiêu phần tử cho danh sách số:"))
    for i in range(a) :
        b = int(input(f"nhập giá trị cho phần tử thứ {i+1} :"))
        total.append(b)
    n = int(input("nhập số n cần so sánh với danh sách:"))
  
     
def kiem_tra (total, n) :
    lst = []
    for i in total :
        b = n - i
        if b > 0 :
         lst.append(i)      
    return (max(lst))

nhap_ds ()
kiem_tra (total, n)
c = kiem_tra(total, n) 
print(f"số trong danh sách gần với n nhất là : {c}")    
    