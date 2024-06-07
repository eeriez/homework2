first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')

if first == second and second == third:
    print('Среди введенных чисел есть три одинаковых.')
elif first == second or second == third or first == third:
    print('Средди введенных чисел есть 2 одинаковых.')
else:
    print("Среди введенных чисел одинаковых нет.")