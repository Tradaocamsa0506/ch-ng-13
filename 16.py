def one_away (str1, str2) :
    if len(str1) == len(str2) :
        b = 0
        for i in range (len(str1)) :
            if str1[i] != str2[i] :
             b+=1
        if b > 1 :
           print("có lớn hơn một kí tự khác nhau ở cả hai chuỗi")
        if b ==1 :
           print("TRUE")
    else :
       print("hai chuỗi có độ dài khác nhau")       
str1 = input("nhập chuỗi thứ 1:")
str2 = input("nhập chuỗi thứ 2:")
one_away(str1, str2)              
       
