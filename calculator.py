
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

choice = input("Введите номер операции (1/2/3/4): ")

if choice == '1':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif choice == '2':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif choice == '3':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif choice == '4':
    if num2 == 0:
        print("Ошибка! Деление на ноль невозможно.")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")

else:
    print("Некорректный ввод")

