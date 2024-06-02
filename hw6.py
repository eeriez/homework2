my_dict = {'Oleg': 2000, 'Anton': 1996, 'Olga': 1999}

print(my_dict)
print(my_dict['Oleg'])
print(my_dict.get('Maria', 'not found'))

my_dict.update({'Maria': 1989,
               'Anna': 1985})
deleted_pair = my_dict.pop('Anton')
print(deleted_pair)
print(my_dict)


my_set = {1, 3, 35, 7, 7, 8, 8, 9, 9, 9, 56, 67}

print(my_set)
my_set.add(5)
my_set.add(43)
my_set.remove(56)
print(my_set)
