
__author__ = 'Meshcheryakov Alexander'

# Задача-1: Запросите у пользователя ввод произвольного целого числа
# Необходимо вывести поочередно цифры введенного пользователем числа

number = int(input('Привет, назови любое целое число от 1 до 100: ' ))
if number > 100:
    print ('я же сказал до 100')
else : print (number)


# Задача-2: Запросите у пользователя ввод двух чисел и связать значения с соответствующими переменными
# Поменять значения переменных местами. Вывести новые значения на экран.
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

number_a = int(input('назови число A:  ' ))
number_b = int(input('теперь число В:  ' ))

number_a,number_b = number_b,number_a

print (number_a)
print (number_b)


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input ('Назовите свой возраст: '))

if age > 18:
    print ("Доступ разрешен")
else:
    print ('Извините, пользование данным ресурсом только с 18 лет')
