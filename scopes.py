'''Области видимости и простанства имен'''

# def func():
#     a=0
#     print('Функция питон')
# print(a)

'''Пространства имен'''

# 1. builtins -> все что встроенно в стандартную библиотеку питона

# 2. Global -> все пеоменные внутри файла которые мы создали

# 3. Enclosed -> (не локальное, замкнутое) находится между двумя пространствами 

# 4. Local -> (лоакльное)

# print(globals()) -> возвращает все глобальные переменные 

# print(dir(__builtins__)) -> возвращает все встроенные имена 

''' Лкальные -> переменная в функциях'''

# def func(test):
#     a = 10 
#     b = 0 
#     print(locals())

# func(6)

# print(locals()) -> когда применяем на глобальном уровне, возвращает все глобальные имена 


# def func1():
#     a = 0
#     b = 9
#     print(a, b)

# func1()

''' Enclosed '''
# возникает только тогда, когда внутри функции обявляется еще функция (вложенности функций)

# def outer_func():
#     outer = 88
#     print(outer)
#     def inner_func():
#         inner = 99
#         print(inner)
    
# outer_func()

# string = 'я глобальная'
# def outer_func():
#     #string = 'не локальная переменная (enclosed)'
#     print(string)
#     def inner_func():
#         #string = 'локальная переменная'
#         print(string)
#         #print(locals())
#     inner_func()
#     #print(locals())
# outer_func()
# # inner_func() -> будет ошибка, так как она в нелокальной области
# # print(outer)


# ''' Порядок поиска переменных '''
# # Local ->Enclosed -> Global -> Builtins

# # import this $ краткий гайд по дзен питону 


# '''global -> позволяет изменить значение глобальной переменной, находясь в локальной области видимости'''


# # x = 10 

# # def func():
# #     global x
# #     x += 20
# #     print(x)

# # func()
# # print(x)


# count = 0

# def couter():
#     global count
#     print(count)
#     count += 1

# couter()
# couter()
# couter()

# '''
# nonlocal -> позволяет изменить значение 
# enclised (не локальная) пнременной в локальной области видимости 
# '''

# def outer():
#     a = 8 
#     def inner():
#         nonlocal a
#         a = 10
#         print('inner a = ', a)
#     inner()
#     print('outer a =', a)
    
# outer()







# x = 'Я глобальная переменная!'
# def my_func():
#     global x
#     print(x)
#     x = 'Я могу изменяться'

# my_func()
# print(x)





# balance = 0
# def get_salary(amount):
#     global balance
#     balance = balance + amount

# def pay_bills(amount, log_name):
#     global balance
#     balance = balance - amount
#     print(f"Вы заплатили {amount} сом за {log_name}")
# def get_balance():
#     global balance
#     print(f'У вас на счету {balance} сом')

# get_salary(1000) 
# get_balance() 
# pay_bills(400, 'кабельное тв') 
# get_balance()


# result = 0
# def pow_first(x,y):
#     global result
#     result = x**y
# def pow_second(z):
#     global result 
#     result %= z
    
# pow_first(2, 3)
# pow_second(3)
# print(result)




var = 'переменная в foo' 
def foo(): 
    global var 
    var = 'переменная foo' 
    print('переменная в foo: ', var) 

def bar(): 
    global var 
    var = 'переменная bar' 
    
    bar() 

foo() 
print('переменная в foo: ', var)