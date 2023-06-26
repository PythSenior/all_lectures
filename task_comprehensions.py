        #task 1

# list_ = [(i) for i in range(1, 101)]
# print(list_)

        #task 2

# list_ = [x for x in range(1, 50) if x %2 != 0]
# print(list_)

        #task 3

# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4] 
# int_list = [x for x in list_ if x % 2 == 0 and x > 0] 
# print(int_list)

        #task 4

# list_ = [i ** 2  for i in range(1, 26) ]
# print(list_)

        #task 5

# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# int_list = [int(x) for x in str_list]
# print(int_list)

        #task 6 

# list_ = [x**2 if x % 2==0 else x for x in range(1,11)]
# print(list_)

        #task 7

# list_ = [x == False if x % 2 != 0 else True for x in range(1, 11)] 
# print(list_)

        #task 8 

# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# new_list = ['shorter' if len(x) <= 4 else 'longer' for x in list_name] 
# print(new_list)

        #task 9

# dict_ = {x : x ** 2 for x in range (1, 11)} 
# print(dict_)

        #task 10

# n = int(input()) 
# dict_ = {x : x**2 for x in range (1, 501) if x % n == 0} 
# print(dict_)

        #task 11

# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3} 
# dict_ = {k:list(range(v+1))[1:] for k,v in a.items()} 
# print(dict_)

        #task 12

# dict_ = {'first': 1, 'second': 2, 'third': 3} 
# a = {k: 'odd' if v % 2 != 0 else 'even' for k, v in dict_.items()} 
# print(a)

        #task 13

# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending' 
# list1 = list(string_.split()) 
# list_ = [x for x in list1 if x.isdigit()] 
# print(list_)

        #task 14

# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91}, 'Olga': {'history': 92, 'math': 96, 'literature': 81}, 'Nik': {'history': 84, 'math': 85, 'literature': 87}} 
# new_dict={x:max(y,key=lambda x:y.get(x)) for x,y in dict_.items()} 
# print(new_dict)

        #task 15

# my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
# dict_ = {k:y for k,v in my_dict.items() for x,y in v.items()} 
# print(dict_)



