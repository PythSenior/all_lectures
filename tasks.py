        # task 1

        # task 2

        # task 3

        # task 4

        # task 5

        # task 6

# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# res = []
# for i in nums :
#     if i < 5:
#         res.append(i)
# print(res)

        # task 9

# list_ = [1, 2, 3, 4, 5,]
# new_list = []
# for num in list_:
#     if num %2 == 0:
#         new_list.append('четное')
#     else:
#         new_list.append('нечетное')
        
# print(new_list)

        # task 10

# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# num = list(range(20))
# print(num)

        # task 11

# list_ = list(range(0, 101, 2))
# print(list_)

        # task 12

# list1 = [11, 23, 45, 7, 9] 
# list2 = [21, 4, 16, 8, 10]
# print(sum(list1+list2))

        # task 13

        # 1 option

# list_ = sorted(input().split(','))   
# print(list_)

        # 2 option

# user_number = input()    
# num_list = user_number.split(',')  
# num_list = [int(num) for num in num_list] 
# sorted_nums = sorted(num_list)
# print(sorted_nums)

        # task 14

# list_ = [1,1,3] 
# set_ = set(list_) 
# if len(set_) != len(list_):
#          print('yes') 
# else:
#         print('ERROR')

        # task 15

# list_ = []
# for i in range(54, 9184):
#     if i %5 == 0:
#         list_.append(i)
#         list_.append(i)
#         print(list_)

        # task 16

        # 1 option

# list_ = [20, 10, 20, 1, 100] 
# list_.sort()
# min_number = list_[0] 
# print(min_number)

        # 2 option

# list_ = [20, 10, 20, 1, 100]
# min1=list_[0]
# for i in list_:
#     if i <min1:
#         min1=i
# print(min1)

        #task 17

        #task 18

        #task 19

# list_ = [8, 6, 8, 10, 8, 20, 10, 8, 8] 
# number = 10
# if list_ == number: 
#     print('Oshjeh') 
# else: 
#     print(list_.count(number))

        # task 20

# list_ = [1, 'abcd', 3, '1', 4, 'xyz', 5, 'pqr', 7, 5, 12] 
# count = 0 
# a = '' 
# for i in list_: 
#         if type (i) == int: 
#                 count = i + count 
#         elif type(i) == str:
#                 a = i 
#         if a.isdigit(): 
#                 count = count + int(i) 
# print(count)




# list_ = [1, 'abcd', 3, '1', 4, 'xyz', 5, 'pqr', 7, 5, 12]  
# sum_ = 0 
# res = [int(x) for x in list_ if type(x) == int or x.isdigit()] 
# for i in res: 
#     sum_ += i 
#     print(sum_)




# list_ = [1, 'abcd', 3, '1', 4, 'xyz', 5, 'pqr', 7, 5, 12] 
# total = 0 
# for item in list_: 
#         if isinstance(item, int):     
#                 total += item 
#         elif isinstance(item, str) and item.isdigit():     
#                 total += int(item) 
#                 print(total)



