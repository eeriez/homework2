def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()
    return 0
test_function()
#inner_function()
#* Traceback (most recent call last):
#  File "C:\Users\eerie\PycharmProjects\pythonProject\module_4_2.py", line 7, in <module>
#    inner_function()
#    ^^^^^^^^^^^^^^
#NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
