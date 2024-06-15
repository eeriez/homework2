def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(5, 6)
print_params(c = 6)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [1, 'f', False]
values_dict = {'a': 423, 'b': 'fgshdj', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [2, 'b56']

print_params(*values_list_2, 42)
