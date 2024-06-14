list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

n = 0
while n < len(list):
    if list[n] == 0:
        n += 1
        continue
    elif list[n] > 0:
        print(list[n])
    elif list[n] < 0:
        break
    n += 1
