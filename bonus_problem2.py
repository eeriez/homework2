import random

slot1 = random.randint(3, 20)

numbers = []   #список чисел от 1 до выпавшего числа из первой вставки
for i in range(1, slot1):
    numbers.append(i)
"""в примечании к задаче сказано "Пары чисел подбираются от 1 до 20 для текущего числа.", но я сделала
перебор только до выпавшего в первой вставке числа (slot1), исключая его самого, потому что смысла идти
дальше него не вижу. в этом была бы польза, если бы мы включали пары с нулем (например, slot1 = 9, пара
9 и 0 подходит т.к 9+0=9 и 9 % 9 == 0 и тд), а суммы, которые больше самого числа точно не будет ему кратными.
получается, гоняем точно неверные числа по приколу."""

all_pairs = []   #список всех уникальных пар
for i in numbers:
    j = i + 1
    for j in range(j, slot1):
        pair = []
        pair.append(i)
        pair.append(j)
        all_pairs.append(pair)
        pair = []

final_pairs = [pair for pair in all_pairs if slot1 % sum(pair) == 0]   #список пар, подходящих под условие

result = ""
for pair in final_pairs:
    for i in pair:
        number = str(i)
        result += number

print(slot1)
print(result)
