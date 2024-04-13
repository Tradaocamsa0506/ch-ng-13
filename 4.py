num = int(input("nhập vào một dãy số : "))
def cong(num) :
 while num >= 10 :
  num = sum(int(digit) for digit in str(num))
 return num
a = cong(num)
print (f"tổng các chữ số {a}")  