def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
my_list = [1, 2, 3, 4, 5]
print(is_sorted(my_list))  # Output: True

my_list = [5, 4, 3, 2, 1]
print(is_sorted(my_list))  # Output: False