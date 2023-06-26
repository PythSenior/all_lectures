'''======= Comprehensions ======='''
#генерация последовательности в одну строку используя цикл for (синтаксический сахар)

# for переменная in диапозон:
#     тело


'''Синтаксис'''

# 1 результат for элемент in итерируемый объект 

# 2 результат for элемент in итерируемый объект if фильтрация 

'''=========== List compehension ==========='''

# упрощение процесса создания списков 

# list_ = []
# for i in 'hello':
#     list_.append(i)

#     print(list_)




# list_0 = list([i for i in 'hello'])
# print(list_0)

# list_ = [i for i in 'hello']
# print(list_)


# import time
# start_time = time.time()
# list_ = []
# for i in range(1,1000000):
#     list_.append(i)
# print(time.time() - start_time)



# import time
# start_time = time.time()
# list_num = [number for number in range(1,1000000)]
# print(time.time() - start_time)


'''создать список четных чисел от 1 до 10'''

# list_1 = [i for i in range(11) if i % 2 == 0]
# print(list_1)


# [элемент if условие else элемент 2 for i in итерируемый объект]

# a = [
#     'четное' 
#     if i % 2 == 0 
#     else 'не четное' 
#     for i in range(1, 11)
#     ]
# print(a)


# list_str = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         list_str .append('четное ')
#     else:
#         list_str.append('нечетное')

'''========== Set comprehension =========='''

# list_ = {1,1,2,3,4,5,3,2,1,6,6,7,8}
# set_l = [i for i in list_]
# print(set_l)

# set_ = set()
# for i in list_:
#     set_.add(i)
# print(set_)

# dict_ = {i: i[i] ** 2 for i in range(1, 11)}
# print(dict_)

# employees = {
#     'id1': {
#         'first name': 'Александр',
#         'last name' : 'Иванов',
#         'age': 30,
#         'job':'программист'
#             },
#     'id2': {
#         'first name': 'Ольга',
#         'last name' : 'Петрова',
#         'age': 35,
#         'job':'ML-engineer'
#             }
# }

# # dct={key:value for key,value in employees.items()}
# # print(dct)

# dct = {
#     key: 
#     {k: float(v) 
#     if k == 'age' else v 
#     for k, v in value.items()
#     }
#     for key, value in 
#     employees.items()
#     }

# print(dct)


# for info in employees.values():
#     for k, v in info.items():
#         if k == 'age':
#             info[k] = float(v)

# print(employees)