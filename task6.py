# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

num = int(input("Введите число дня недели от 1 до 7: "))

if 1<=num<=5 :
    print("Нет")
else:
    print("Да")