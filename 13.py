def swapcase(s):
    x = ''
    for i in s:
        if i.isupper():
            i = i.lower()
        else:
            i = i.upper()
        x += ''.join(i)
    return x
s = "Nguyen Thi Thanh Tuyen"    
res = s.swapcase()    
print(res)
