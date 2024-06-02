immutable_var = 1, True, 'aaaaaaaaa', 76.86

print(immutable_var)

#immutable_var[0] = 8
#TypeError: 'tuple' object does not support item assignment
# Несмотря на то, что кортеж может содержать изменяемые элементы, такие как списки, сам кортеж изменяться не может

mutable_list = ['43563', 435, False]
mutable_list[1] = True

print(mutable_list)