'''========== обработка исключений  ========='''

'''
Ошибки -> проблемы с синтаксисом
1. SyntaxError: забыли двоеточие, скобку
2. IndentationError: неправильный отступ 
3. TabError: неправильная табуляция 
'''

# Исключение: (код написан правильноб но он неправильно работает не так, как ожидалось)
# 1. ArithmeticError ZeroDivisionError
# 2. ValueError
# 3. NameError
# 4. TypeError
# 5. KeyError
# 6. IndexError
# 7. AttributeError
# 8. ImportError 
# 9. BaseException (прородитель)

ZeroDivisionError # при делении на 0
# 8 / 0
# 4 // 0
# 3 % 0

ValueError # Вызывается при распаковки, переводе одного типа данных в другой 
# int('hello')

NameError # когда обращаемся к несуществующей переменной 
# print(b)

TypeError # когда передаем в функцию, метод меньше или больше аргументов, чем требуется 
# for i in 123456789: 
#     print(i)
# [].append()
# [].append(1, 2, 3)
# '5' + 5

KeyError # при обращению к несуществуещему ключу 
# dict_ = {'a' : 1}
# dict_['b']
# dict_.pop('b')

IndexError # при обрашении к несуществующему индексу
# list_ = ['a', 'b', 'c']
# list_[4]
# list_.pop(3)

AttributeError # когда обращаемся к несуществующему методу или атрибуту объекта 
# a = 12345
# a.upper()
# b = [1, 2, 3]
# b.discard()

ImportError # неправильный импорт 
# import math
# from math import pi2

# BaseException -> прородитель

'''====== try except ======'''

# чтобы код не прекращал свою работу 

''' Синтаксис '''

# try:
#     тело try
#     код, который может вызвать исключение 
# except:
#     тело except 
#     код который сработает, если в try возникает ошибка 
# else: 
#     тело else
#     код, который отработает, если в блоке try не возникло ошибки
# finally:
#     тело finally
#     код, который отработает в любом случае 



# try:
#     num1 = int(input('Введите первое число:'))
#     num2 = int(input('Введите второе число:'))
#     res = num1 / num2
# except ValueError:
#     print('Вы ввели не число!')
#     num1 = int(input('Введите число:'))
# except ZeroDivisionError:
#     print('На ноль делить нельзя')
# else:
#     print(f'{num1} / {num2} = {res}')
# finally:
#     print('Пока')

# try:
#     while True:
#         print('a')
# except KeyboardInterrupt:
#     print('ctrl + c')

# try:
#     dict_={key: key**2 for key in range(11) if key%a==0}
#     print(dict_)
# except NameError:
#     print('Переменная а не объявлена')

# Задание 

# try:
#     num1 = int(input('Введите первое число:'))
#     num2 = int(input('Введите второе число:'))
#     res = num1 + num2
#     print(res)
# except ValueError:
#     print('Вы ввели не число')

'''====== raise ======'''
# исскусытенно вызывать ошибки

# try:
#     age = int(input('введите возраст: '))
#     if age < 18:
#         raise ValueError('Доступ закрыт')
#     print('чек')
# except ValueError:
#     print('вы ввели не число или вам нет 18')






# inp1 = input() 
# inp2 = input() 
# inp3 = input() 
# inp4 = input() 
# inp5 = input() 
# list0 = [] 
# list0.append(inp1) 
# list0.append(inp2) 
# list0.append(inp3) 
# list0.append(inp4) 
# list0.append(inp5) 
# list1 = [] 
# target = ' ' 
# for i in list0: 
#     t = i.find(target) 
#     r = i.rfind(target) 
# if i.count(target) > 1: 
#     list1.append(i[r+1:]) 
# else: 
#     list1.append(i[t+1:]) 
#     print(sorted(list1))             
            


            
            
try:
    cash = int(input())
    if cash < 0:
        raise Exception  ('VallueError')
    print(cash)
except:
    print('Сумма не может быть отрицательной! ')

    



