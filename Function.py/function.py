'''Ввведение в функции'''

'''Аннотации -> помогают сделать код информативным и избавиться от некоторых проблем динамической типизации, никак не влияет на работу кода'''

# num: int = 10 # предупредить какой тип данных нужно передавать, присваивать
# num = 'hello'
# print(num)

'''========== Функции =========='''
# Функция -> именованный блок кода (есть имя), которыйвыполняет одну задачу
# Может принимать в себя аргументы и возвращать результат
# вызывается многократно, по имени.


# def -> ключевое слово для объявления функции (указывает питону, что мы хотим создать функцию)

'''Синтаксис'''
# def <название_функции>(параметры):
#     <тело функции>


# def my_len(obj):
#     count = 0
#     for i in obj:
#         count += 1
#     print(count)
#     return count


# my_len([1, 2, 3, 4, 5])
# a = my_len([1, 2, 3, 4, 5])
# print(a)

# func = my_len
# print(func([1, 2, 3, 4, 5]))
# print(func)
# a = print
# a('hello')
# b = 10
# b()
# print(type(my_len))


# def sum_(num1: int, num2: int):
#     res = num1 + num2
#     print(res)
#     return res

# a = sum_(2, 3)
# print(a)
# # sum_(4, 'he')
# print(sum_(1, 2))

# sum_(sum_(2, 3), sum_(1, 2))
# a = sum_(1, 2) #без return None (3)
# b = sum_(9, 8) # без return None (17)
# c = sum_(9, 45) # без return None (54)

'''return -> используется для возвращения результата, который можно сохранить в переменной и где-то использовать, после return функция завершает свою работу, если в функции не прописан return -> функция возвращает None'''

# str_ = 'hello'
# print(str_.replace('h', 'hello')) # helloello

# list_ = [1, 2, 3, 4]
# print(list_.append([7, 8, 9]))
# print(list_)


'''======= Параметры и аргументы ======'''

# Параметры -> локальные переменные внутри функи, значения параметрам задаются при вызове фукции
# Аргументы -> значения, которые мы задаем параметрам

# def a(параметр):
#     pass

# a(аргумент)

''' ====== Виды параметров ======'''

# 1. обязательные (a, b, list_) -> определяют, какие аргументы нужно передать
# 2. не обязательные 
# 2.1 с дефолтом (имеет значение по умолчанию)
# 2.2 args -> принимает (все) неименованные аргументы, которые не относятся к обязательным (tuple)
# 2.3 kwargs -> принимает (все) именованные аргументы (dict)
# a=17

# def func(a = 0, *args, **kwargs):
#     print(a)
#     print(args)
#     print(kwargs)

# func(3, 4, 4, n = 0, m = 7)


'''========= Виды аргументов ========='''
# 1. позиционные -> по позиции (a, b, c) -> (1,2,3) a = 1 b = 2 c = 3 
# 2. именнованные (по названию) 

# 2.
# def test(a, b, c):
#     print(a, b, c)

# test(1, b = 4, c = 2)

# 1.
# def test(a: int, b: int, c: list, n=4):
#     print(a, b, c)

# test()


# Pаспаковка
# list_ = [*range(1, 11)]
# print(list_)

# dict1 = {'a':1, 'b': 2, 'c': 3}
# dict2 = {*dict1}
# dict2 = {**dict1}
# print(dict2)

# def print(a):
#     return a

# print(2)
# print('hello')

# sum 

# def sum_numbers(number1, number2, *args, **kwargs):
#     print(args, kwargs)
#     print(kwargs.values())
#     return number1 + number2 + sum(args) + sum(kwargs.values())

# # print(sum_numbers(1, 7))
# print(sum_numbers(1, 7, 99, 8, 5, n = 9, k = 87, o = 0))



# def to_fahrenheit(k:int) -> float: 
#     assert k>=0,'Холоднее абсолютного нуля!' 
#     res=(k-273.15)*9/5+32 
#     return res 
#     print(to_fahrenheit(3))



# def calculator(num1,num2,act):
#         if act=='+':
#             print(f'{num1} + {num2} =',num1+num2)
#         elif act=='-':
#             print(f'{num1} - {num2} =',num1-num2)
#         elif act=='*':
#             print(f'{num1} * {num2} =',num1*num2)
#         elif act=='/':
#             print(f'{num1} / {num2} =',num1/num2)


# while True:
#     try:
#         num1=int(input('введите первое число:'))
#         num2=int(input('введите второе число:'))
#         act=input('Выберите действие + , - , * , / : ')
#         calculator(num1,num2,act)
#         if num1==0 and num2==0:
#               break
#     except ValueError:
#         print('Вы ввели не число!')
#         num1=int(input('введите первое число:'))
#         num2=int(input('введите второе число:'))
#         act=input('Выберите действие + , - , * , / : ')
#         calculator(num1,num2,act)
#         if num1==0 and num2==0:
#               break
#     except ZeroDivisionError:
#         print('На ноль делить нельзя!')
#         num1=int(input('введите первое число:'))
#         num2=int(input('введите второе число:'))
#         act=input('Выберите действие + , - , * , / : ')
#         calculator(num1,num2,act)
#         if num1==0 and num2==0:
#               break
#     finally:
#          continue


# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
# b = {} 
# for k, v in a.items(): 
#     if v%2==0: 
#         b.setdefault(k, 2) 
#     else: 
#         b.setdefault(k,v) 
#         print(b)


# import random

# def generate_password(firstname, lastname):
#     password = firstname + lastname
#     for i in range(7):
#         password += str(random.randint(0, 9))
#     return password

# def get_info():
#     firstname = input("Введите имя: ")
#     lastname = input("Введите фамилию: ")
#     password = generate_password(firstname, lastname)
#     print("Ваш пароль:", password)
#     return password


# def ice_cream(flavor, size, *toppings):
#     print("Вы заказали мороженое вкуса", flavor, "размера", size)
#     if toppings:
#         print("С дополнительными топпингами:")
#         for topping in toppings:
#             print("- " + topping)
#     else:
#         print("Без дополнительных топпингов")