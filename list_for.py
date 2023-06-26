# '''Тип данных списки (list)'''
# # изменяемый, упорядоченный, индексируемый, итерируемый тип данных
# # [] -> литералы (выражения или константы, которые создают объект)

# list_ = [1, 2, [True, 'hello'], {1: 'one'}, (1, 2, 3)]
# print(list_[0])
# print(list_[2] [0])
# print(list_[-1])
# print(list_[:3])



# '''========= Создание списков ========='''

# #1. list(iterable)
# list_1 = list ('hello world')
# print(list_1)

# #2. []
# a = []
# print(type(a))

# #3. range() -> возвращает последовательность
# list_2 = list(range(10))
# print(list_2)
# # range (start, end, step)
# #start -> с какого числа начать (по умолчанию 0)
# #end -> до какого элемента (не включая последнее)
# #step -> шаг (какие элементы пропускать)



# '''========= Методы списков ========='''

# list.apped('element') #-> добавляет элемент в конце списка

# list_3 = [1, 2, 3, 'hello', 'world']
# list_3.apped(4)
# print(list_3)


# list.extend(['intrable']) #-> расширяет список (добавляет каждый элемент iterable по отдельности, в конец списка)

# list_3 = [1, 2, 3, 'hello', 'world']
# list_3.extend([1, 2, 3])
# print(list_3)


# list.insert('index', 'element') #-> добавляет element по индексно (по указанному индексу)

# list_3 = [1, 2, 3, 'hello', 'world']
# list_3.insert(3, 'makers')
# print(list_3)


# list.index('element', ['start', 'end']) #-> возвращает индекс элеента

# list_3 = [1, 2, 3, 'hello', 'world', 1, 2, 3]
# list_3.index((1))
# print(list_3.index(1))


# list.clear() #-> очищает список

# list_3 = [1, 2, 3, 'hello', 'world', 1, 2, 3]
# list_3.clear()
# print(list_3)


# list.count('eliment') #-> кол-во вхождения элемента в список
 
# list_3 = [1, 2, 3, 'hello', 'world', 1, 2, 3]
# print(list_3.count(1)) 
# print(list_3.count('hello'))


# list.pop(['index']) #-> удаляет элементы поиндексно, возвращает удаленный элемент(по умолчанию удаляет последний элемент)

# list_3 = [1, 2, 3, 'hello', 'world', 1, 2, 3]
# print(list_3.pop(1)) 
# print(list_3.pop('hello')) 


# list.remove('element') #-> удаляет element

# list_3 = [1, 2, 3, 'hello', 'world', 1, 2, 3]
# print(list_3.remove(1)) 
# print(list_3.remove('hello')) 


# list.reverse() #-> полностью разварачивает список

# list_3 = [1, 2, 3, 'hello', 'world', 1, 2, 3]
# list_3.reverse()
# print(list_3)


# list.sort() #-> сортирует список, состоящий из элементов одного типа данных (сортирует в порядке возростания)

# list_3 = [1, 2, 3, 1, 2, 3]
# list_3.sort()
# print(list_3)


# list.copy() #-> поверхностное копирование 

# list_3 = [1, 2, 3, 'hello', 'world', 1, 2, 3]
# list_1 = list_3.copy()
# print(list_1)



# '''========= Цикл for ========='''

# # повтаряющийся блок кода

# lilist_1 = [1, 2, 3, 'hello', 'world', 1, 2, 3]
# for i in list_1: 
#     print(i)


# list_1 = [1, 2, 3, 1, 2, 3]
# for i in list_1: 
#     print(i ** 2)


# lilist_1 = [1, 2, 3, 'hello', 'world', 1, 2, 3]
# for i in list_1: 
#     print(i)


# for i in range(11) : 
#     print(i)


# for i in range(11) : 
#     if i %2:
#         print(i, 'нечетное')
#     else:
#         print(i, 'четное')


# for i in range(1, 5):
#     print()
#     print(i)
#     for b in range(0, 2):
#         print(b)


# list_ = [1, 2, 3, 'hello', 'world', 1, 2, 3, 'world']
# list_index =[]
# for i in list_:
#     if type(i) != int:
#         list_index.append(i)

# for i in list_index:
#     list_.remove(i)

# print(list_) 



# '''========= Typle ========='''

# # кортеж - неизменяемый, индексируемый, упорядоченный, итерируемый тип данных (неизменяемый список)
# # литералы -> (,) 

# '''========= Методы ========='''

# list.count('eliment') #-> кол-во вхождения элемента в список
 
# list_3 = (1, 2, 3, 'hello', 'world', 1, 2, 3)
# print(list_3.count(1)) 
# print(list_3.count('hello')) 


# list.index('element', ['start', 'end']) #-> возвращает индекс элеента

# list_3 = (1, 2, 3, 'hello', 'world', 1, 2, 3) 
# list_3.index((1)) 
# print(list_3.index(1)) 




list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
list1 = [x for x in list_.items if x < 0 = int_list:]
int_list = [] 
print(int_list)