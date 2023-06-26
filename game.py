# import random

# nums=[1,2,3,4,5,6,7,8,9,10]
# comp = random.choice(nums)
# inp1 = input('Введите свое имя: ')

# inp2 = input(f' {inp1} Вы хотите сыграть в игру? Да или Нет: ')
# while True:
#     if inp2 == 'Да' or 'да':
        
#         inp3 = int(input('Выберите и введите число от 1 до 10: ')) 

#     elif inp2 == 'Нет' or 'нет':
        
#         print('До свидания!')

    

#     if inp3 != comp:

#         print('Вы не угадали, число было ->', comp, )
        
#     elif inp3 == comp:
#         print(f' {inp1}Вы угадали, сыграем еще? Да или нет: ')
#     if inp3 == 'Да' or 'да':
#         print(inp3 = int(input('Выберите и введите число от 1 до 10: ')))
#     elif inp3 == 'Нет'or 'нет':
#         print('До свидания ')
#         break






import random

numbers = [1,2,3,4,5,6,7,8,9,10]
comp = random.choice(numbers)
name = input('Как вас зовут?')
print(f'Здравствуйте {name}, хотите ли вы сыграть в игру?')

while True:
    wish = input('(Да или Нет)')
    if wish == 'да':
        print('Вы должны угадать число')
        num = int(input('Выберите и введите число от 1 до 10: '))
        trying = 0
        while num != comp:
            print('Попробуйте еще!')
            num = int(input('Выберите и введите число от 1 до 10: '))
            trying += 1
        print(f'Вы угадали!!! загаданное число было {comp}! вы угадали загаданное число с {trying}-ой попытки \n хотите ли вы сыграть еще раз?')

    elif wish != 'нет' and 'да':
        print('Выберите только да или нет!')
    elif wish =='нет':
        print('Спасибо за игру, до свидания!')
        break
