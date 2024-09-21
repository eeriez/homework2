def is_prime(func):
    def wrapper(a, b, c):
        prime_flag = True
        func_result = func(a, b, c)
        for i in range(2, func_result):
            if func_result % i == 0:
                prime_flag = False
        if prime_flag is True:
            print('Простое')
        else:
            print('Составное')
        return func_result
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 4, 0)
print(result)
