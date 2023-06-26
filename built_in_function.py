'''Встроенные функции'''

'''Общеизвестные '''
print 
len
sum
min
max
input
int
str
list
id
dir
sorted
divmod
type

'''lambda -> анонимная функция (та же самая функция, только без имени)'''

# def <имя>(параметры):
#     тело

# lambda параметры:  что функция возвращает 

# def add_nums(x, y): return x + y
# print(add_nums(5,6))
# print(b)


# list_ = ['1', '2', '3']
# list_nums = []

# for i  in list_:
#     list_nums.append(int(i))

# print(list_nums)


# list_ = [3, 56, 2, 4]
# list_s = list(map(lambda x: x ** 2, list_))
# print(list_s)


# def filter_nums(number: int) -> bool:
#     if number % 2 == 0

# print((lambda x, y: x + y ) (4, 7))

# lambda_fun = lambda x, y: x + y
# print(lambda_fun(7, 9))
    
# a = lambda a, b, c: (a, b, c)

# print(a(3,4,5))


# dict_ = {1: 'a', 2: 'b', 3: 'c'}

# dict_keys = lambda x: x.keys()
# print(dict_keys(dict_))
# def func(dict_):

# ls = [1 ,2, 3, 4, 5, 6, 7, 8]
# ls_= lambda x: x[-1]
# print(ls_(ls))

# num =lambda z: z ** 2
# print(num(5))

# num =lambda x:len(x)
# print(num('hello')) 

'''
map(func, iterable) -> она применяет func 
для каждого элемента итерируемого объекта 
'''
 
# list_ = ['1', '2','3']
# # print(map(int, list_))
# for i in map(int, list_):
#     print(i)

# nums = input('Ведите два числа через пробел')
# a, b = map(int, nums.split())
# print(a)
# print(b)


# list_ = ['1', '2', '3']
# list_nums = []

# for i  in list_:
#     list_nums.append(int(i))

# print(list_nums)


# list_ = [3, 56, 2, 4]
# list_s = list(map(lambda x: x ** 2, list_))
# print(list_s)


# def filter_nums(number: int) -> bool:
#     if number % 2 == 0
#         return True
#     return False

# list_ = [2, 6, 4, 9, 7, 55, 33]
# result = 
# def filter_nums(number: int) -> bool:
#     if number % 2 == 0
#         return True
#     return False

# list_ = [2, 6, 4, 9, 7, 55, 33]
# result =list(filter(filter_nums, list_))
# print(result)

# list_ = ['Тима', 'Макс', 'Эртай', 'Алина', 'Эркаим', 'Алекс']

# def startswitch_vowels(name):
#     vowels = 'АОГШАОКООШАОК'
#     print(tuple(vowels))
#     return name.upper().startswitch(tuple(vowels))


# result = list(filter(startswitch_vowels, list_))
# print(result)


'''======= filter на цикле for ======='''

# list_1 = []
# for name in list_:
#     if startswitch_vowels(name):
#         list_1.append(name)

# print(list_)


'''
reduce(func, iterable) -> нужно импортировать с functools
возвращает один результат 

reduce заменили -> sum, min, max
'''

'''
сумма всех элементов списка
'''


# from functools import reduce

# list_ = [5,2,9,6,4,3]
# result = reduce(lambda x, y: x + y, list_)
# print(result)



'''Произведение всех элементов списка'''

# result = reduce(lambda x ,y: x + y, list_)
# print(result)

'''reduce на цикле for'''
# x = list_[0]
# for y  in list_[1:]:
#     result = (lambda x, y: x * y) (result, y) 
# print(result)

'''enumerate(iterable, [start]) -> нумерует элементы
 последовательности (по умолчанию начинаетсяс 0)
'''

# list_ = ['hello', 'test', 'john', 'world', 'py30', 'питхаб']

# print(list(enumerate(list_, 5)))



# for i in enumerate(list_):
#     print(list_)



# изменить тип данных значений с помощью функций


# dict_ = {1: 2, 3: 4, 5: 6}

# new_dict = dict(map(lambda item: (item[0], str(item[1])), dict_.items()))

# print(new_dict)


'''задача при помощи map() заменить значение чисел словами четное не четное '''



# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = list(map(lambda x: "четное" if x % 2 == 0 else "не четное", list_))
# print(result)


'''
all()

Встроенная функция all() проверяет все элементы 
последовательности на определенное условие и возвращает 
результат в виде булевого значения - True либо False
'''