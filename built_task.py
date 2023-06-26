    # task 1

# from functools import reduce

# list_ = [1, 2, 3, 4]  
# result = reduce(lambda x, y: x + y, list_)
# print(result)

    # task 2

# list_ = [5, 8, 4, 6, 7]
# result = all(map(lambda x : x > 3, list_))
# print(result)


    # task 3

# list_ = [5, 8, 4, 6, 7]
# result = any(map(lambda x :x<0, list_))
# print(result)

    # task 4

# list_ = [1, 2, 3, 4]  
# result = map(lambda x :x**2, list_)
# print(result)

    # task 5
        
# list_ = [1, 2, 3, 4] 
# result = list(filter(lambda x :x %2 == 0, list_))
# print(result)

    # task 6

# list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni',] 
# result = list(filter(lambda x :len(x)>7, list_))
# print(result)

    # task 7

# from functools import reduce

# list_ = [5, 6, 7, 8] 
# result = reduce(lambda x ,y: x*y, list_)
# print(result)

    # task 8

# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 = len(list(filter(lambda x: x % 2 == 0, list_)))
# list3 = len(list(filter(lambda x: x % 2 != 0, list_)))
# result = f"even: {list2}, odd: {list3}"
# print(result)

    # task 9

# list_ = [-1, 2, 3, 5, -3, 7] 
# result = list(map(lambda x :x > 0,list_))
# print(result)

    # task 10

# from functools import reduce

# list_ = ['Paul', 'George', 'Ringo', 'John'] 
# result = reduce(lambda x,y :x if len(x)>len(y) else y, list_)
# print(result)

    # task 11

# result = list(map(lambda x :'Fizz' if x%3==0 else 'Buzz', range(1,50)))
# print(result)

    # task 12

# from functools import reduce

# list_ = [1,2,3,4,5,6]
# result = reduce(lambda x,y: x if x > y else y, list_)
# print(result)

    # task 13

# from functools import reduce

# list_ = [1,2,3,4,5,6]
# result = reduce(lambda x,y: x if x < y else y, list_)
# print(result)


    # task 14

# string = 'hello'
# result = tuple(enumerate(string ))
# print(result)

    # task 15

# list_ = [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]
# result = list(map(lambda x :abs(x),list_))
# print(result)

    # task 16

# list_ = ['hello', 123]
# result = list(map(lambda x :type(x), list_))
# print(result)

    # task 17

# names = ['rauchel','john','peter','jessica','steven123','dandy34','kamest','potter']
# result = list(map(lambda x :x + ' Python' if len(x)>5 else x+' JavaScript', names))
# print(result)

    # task 18

# list_ = ['123hello@gmail.com', '123', 'hello']
# result = list(map(lambda x : x if x.endswith('@gmail.com') else 'Not valid email' ,list_))
# print(result)

    # task 19

# string = 'hello'
# result = tuple(enumerate(string, 1))
# print(result)

    # task 20

# list1 = ['M', 'A', 'K', 'E', 'R', 'S'] 
# list2 = [236, 54, 33, 21, 89, 1]
# result = list(zip(list1,list2))
# print(result)

    # task 21

# list_ = [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56] 
# list1=list(filter(lambda x:x>0,list_)) 
# list2=list(filter(lambda x:x<=0,list_)) 
# res=list(zip(list1,list2)) 
# print(res)

    # task 22

# list_ = [0.334, 23.3443, 43.4, -13.44, 22.03, -11.033, 267.993, -3.24]
# result = list(map(lambda x :round(x**2,3), list_))
# print(result)

    # task 23

# list_ = ['a', 'n', 'n', 'a']
# result = list(map(lambda x:'YES' if list_ == list_[::-1] else 'NO', list_ ))
# print(result[0])




# dict_ = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# dict_ = {k:v for k,v in list(dict_.items())}
# if v !=None:
#     dict_.pop(k)
# print(dict_)





