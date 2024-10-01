from random import randint


class Test:
    def __init__(self, name):
        self.name = name
        self.num = randint(1,100)


def introspection_info(obj):
    info = {
        'type': type(obj),
        'attributes': [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
        'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
        }
    try:
        info['module'] = obj.__module__
    except AttributeError:
        info['module'] = None

    return info


a = 1
test_obj_1 = Test('aaa')
test_obj_2 = Test('bbb')

print(introspection_info(a))
print(introspection_info(test_obj_1))
print(introspection_info(test_obj_2))
