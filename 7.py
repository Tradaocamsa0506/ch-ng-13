import random

def random_integer_with_n_digits(n):
    lower_bound = 10 ** (n - 1)
    upper_bound = 10 ** n - 1
    return random.randrange(lower_bound, upper_bound + 1)
n = 8
random_num = random_integer_with_n_digits(n)
print(random_num)