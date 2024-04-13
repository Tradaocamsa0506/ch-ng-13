from math import pow
def root(x, n = 2) :
   b = pow(x, 1/n)
   return b

x = float(input("nhập giá trị cho x :"))   
ket_qua = root(x)
print(ket_qua) 