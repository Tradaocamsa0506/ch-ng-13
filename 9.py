def number_of_factors(num):
    lst = []
    for i in range(1, num + 1):
        if num % i == 0:
            lst.append(i)
    return lst

num = int(input("mời người dùng nhập số:"))
result = number_of_factors(num)
print(f"The number of factors for {num} is:", result)