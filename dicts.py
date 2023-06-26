# """Словари (dict)"""
# изменяемый, неиндексируемый, упорядоченный , итерируемый тип данных
# {ключ: значение}

# # {}
# """ Способы создания словарей"""
# dict_ = {}
# print(type(dict_))

# dict_1 = dict(a = "Hello")
# print(type(dict_1))

# dict_ = dict(([]"key, 'value"], ['o', "v"]))
# dict_ = dict(['ad', 'cd', 'ef'])
# print(dict_)
# key, value = [1, 2]
# print(key, value)


# # ключи должны быть неизменяемым типом данных 

# {[]: 1} -> TypeError: unhashable type: "list"
# # ключи -> должны быть уникальными

# a = {1: "hello", 1: 'world', 1: 1}
# print (a) #{1: 1}

# Значения -> могут относиться к любому типа данных

# dict_ = {
#     "name": "Aiana",
#     "last_name": None,
#     "email": True,
#     "info": [1, 2, 3, 4]
# }
# print(dict_['info'])

# dict_["email"] = "test@gmail.com" # изменение значени по ключу
# print(dict_)
# dict_{"emaill"} #KeyError: "emaill"
# dict_["emaill"] = 12 # добавляет новую пару в словарь {...., "emaill": 12}
# print(dict_)

""" Методы словарей """
# print(dir(dict))

# dict.items() -> возращает все пары в словаре, в виде списка с кортежами
# print(dict_.items()) #dict_items ([('name'), 'Aiana',]) ......

# for key, value in dict_.items():
    # print(i)
    # print (key, "--->>" , value)

# a, b, c, = (1, 2, 3)
# print(a, "--->>", b, "--->>>", c, "--->>>")

# dict.values() -> для получения всех значений в словаре

# print(dict_.values())

# for i in dict_.values():
#     print(i)

# dict.keys() -->> для получения всех ключей словаря
#
# print(dict_.keys())
# for i in dict_.keys():
#     print(i)

# dict.clear() -> очищает словарь
# dict_.clear()
# print(dict_)

# del dict_   -> удаляет объекты
# print(dict_)

# dict.copy() -> возвращает копию словаря 
# dict_copy = dict_.copy() 
# print(dict_copy)


# dict.fromkeys(seq, [default]) -> создает словарь с ключами из последовательности и значением default(None)

# list_ = ["name", "hello", 'test']
# dict_ = dict.fromkeys(list_, 1)
# print(dict_)

# dct = dict.fromkeys('as')
# print(dct)

# dict.get(key, [default]) -> возвращает значение по ключу, если такого ключа нет, не бросает иключение, а возвращает default, если default не указан, возвращает None

# dict[key] -> бросает исключение, если такого ключа нет (вызывает ошибку)

# dict_ = {1: "one", 2: "two"}
# print(dict_.get(1, "no such key")) # one 
# print(dict_.get(3, "no such key")) # "no such key"
# print(dict_.get(3)) # None
# print(dict_[3]) # KeyError
# dict_ = {1: "one", 2: "two"}
# # dict.update(new_dict) -> добавляет new_dict в наш словарь
# # dict_[5] = "five" # добавляет только одну пару
# dict_.update({3: "three", 4: "four" })
# new_dict = (5: "five", 6: "six")
# dict_.update(new_dict)
# print(dict_)


# dict.setdefault(key, [default_value])  ->
# 1. Работает как get
# 2. Если ключа нет, создает новую пару key: default_value, если не указать default_value -> None


#1
# dict_ = {1: "one", 2: "two"}
# print(dict_.setdefault(1)) #one

# #2
# print(dict_.setdefault(3, 'three')) # three
# print(dict_.setdefault(4)) # None
# print(dict_)

# """ Удаление эл-ов словаря"""
# # dict_pop(key, [message]) -> удаляет пару ключ, значение и возвращает значение , если ключа нет выводит message (по умолчанию бросает исключение)

# dict_ = {1: 'a', 2: 'b', 3: 'c'}
# deleted = dict_.pop("a")
# print(dict_,deleted)
# print(dict_.pop("d")) # KeyError: 4 
# print(dict_.pop("d", 'no such key')) # no such key 
# print(dict_.deleted)

# dict.popitem() -> удаляет последнюю пару ключ и значение и значение и возвращает ключ и значение 
# # lifo fifo
# print(dict_.popitem()) # ('c', "three")
# print(dict_)

"""Поменять местами ключи и значение"""

# new_dict = {}
# for key, value in dict.items():
#     new_dict.update({value: key})
#     # new  dict[value] - key
# print(new_dict)