'''
Декораторы -> функция высшего порядка 
(в качестве аргумента принимает функцию и возвращает функцию), 
которая оборачивает другую функцию для расширения
ее функционала при этом не изменяя ее код 
'''

'''функция высшего порядка -> это функция которая может 
принимать в качестве аргумента другую функцию или возвращать 
функцию как результат'''

# def test_func(func)
#     def inner_test_func():
#         func()
#     return inner_test_func


# def hello(func):
#     <Тело>
#     pass

# def benchmark(func: callable) -> None:
#     def wrapper(*args, **kwargs):
#         import time
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print(f'Время работы функции{func.__name__}, заняло {end - start}')
#     return wrapper()


'''
@ -> синтаксический сахар, позволяет нам явно 
указать какой декаратор применяется для функции 


под капотом вызывает функцию decarator и результат выполнения 
этой функции сохраняет в переменной с точно таким же нзванием 
как и обернутая функция 

say_hi = decorator
(say_hi) say_hi()
'''

# def uppercase_decorator(func): 
#     def wrapper():
#         func_ = func()
#         upper_str = func_.upper()
#         return upper_str
#     return wrapper

# @uppercase_decorator
# def inp_str():
#     str_ = input('Введите текст ')
#     return str_

# print(inp_str())

# def decor(x):
#     def inner(y):
#         return x +y 
#     return inner
# test = decor(int(input()))
# print(test(1))


def uppercase(func):
    def innercase():
        print("func start")
        func()
        print("func end")
    return innercase
@uppercase
def sum():
    print("hello world")
sum()


