#Модуль 1 Введение 2 Задача 1

#numberOne = int(input('Введите число 1 '))
#numberTwo = int(input('Введите число 2 '))
#numberThree = int(input('Введите число 3 '))
#summ = numberOne + numberTwo + numberThree
#print(summ)

#Модуль 1 Введение 2 Задача 2

#salary = int(input('Зарплата за месяц? '))
#credit = int(input('Платеж по кредиту? '))
#utility_bills = int(input('Какая задолжность по комунальнке? '))
#summMoney = ((salary - credit) - utility_bills)
#print("Остаток после всех расходов", summMoney)

#Модуль 1 Введение 2 Задача 3

#diagonalOne = int(input('Введите длинну первой диагонали'))
#diagonalTwo = int(input('Введите длину второй диагонали'))
#s = ((diagonalOne * diagonalTwo) / 2)
#print('Площад ромба равна', s)

#Модуль 1 Введение 2 Задача 4

#print(' To be\n or not\n to be')

#Модуль 1 Введение 2 Задача 5

#print(' "Life is what happens \n        when \n           you are busy making other plans"     \n                                       John Lennon')

#Модуль 1 Введение 3 Задача 1

#num_one = (input('Введите число 1 '))
#num_two = (input('Введите число 2 '))
#num_three = (input('Введите число 3 '))
#summNum = num_one + num_two + num_three
#print('Сформерованное число', summNum)

#Модуль 1 Введение 3 Задача 2

#listNum = int(input('Введите черехзначное число '))
#a = listNum % 10
#b = listNum // 1000
#c = listNum % 100 // 10
#d = listNum // 100 % 10
#sum = b * d * c * a
#print('Результат произведениея равен ', sum)

#Модуль 1 Введение 3 Задача 3

#metrsNumber = int(input("Введите кол-во метров "))
#convertSan = metrsNumber * 100
#convertDcm = metrsNumber * 10
#convertMm = metrsNumber * 1000
#convertMili = metrsNumber * 0.00062137
#print('Из', metrsNumber, 'получиться сантиметров', convertSan, 'децеметров', convertDcm, 'Милиметров', convertMm, 'Милей', convertMili)

#Модуль 1 Введение 3 Задача 4

#base_size = int(input('Введите размер основания треугольника '))
#base_hide = int(input('Введите размер высоты '))
#S = (base_size * base_hide) ** 2
#print('Площадь треугольника равна', S)

#Модуль 1 Введение 3 Задача 5

#listNumber = (input('Введите черехзначное число '))
#ret = (listNumber[::-1])
#print(ret)

#Модуль 1 Практическое задание 1 Задача 1

#print(' Nothing\n will work\n unless you do')

#Модуль 1 Практическое задание 1 Задача 2

#print(' "Anyone who\n   stops\n      learning is old,\n         whether at twenty or eighty"\n                                 Henry Ford')

#Модуль 1 Практическое задание 1 Задача 3

#entNumberOne = int(input('Введите первое число '))
#entNumberTwo = int(input('Введите второе число'))
#summa = entNumberOne + entNumberTwo
#raz = entNumberOne - entNumberTwo
#proiz = entNumberOne * entNumberTwo
#print('Сумма чисел ', summa, 'Разница ', raz, 'Произведение', proiz )

#Модуль 1 Практическое задание 1 Задача 4

#oneNum = int(input('Введите число'))
#twoNum = int(input('Введите % '))
#summ = (oneNum // 100) * twoNum
#print(twoNum, 'Процентов', 'из числа', oneNum, 'получается', summ)

#Модуль 1 Практическое задание 1 Задача 5

#width = int(input('Введите ширену прямоугольника '))
#height = int(input('Введите высоту прямоугольника '))
#S = width * height
#print('Площадь прямоугольника равна', S)


#Модуль 1 часть 3  Задача 1

#num1 = (input('Введите двухзначное число '))
#for n in num1[0:2:1]:
#   print(n)

#Модуль 1 часть 3  Задача 2 

#number1 = input('Введите трехзначное число ')
#c = int(number1) % 10
#d = int(number1) // 100
#e = int(number1) % 100 // 10
#for a in number1[0:3:1]:
#print(a)
#print(d+e+c)

#Модуль 1 часть 3  Задача 3

#num1 = input('Введите первое число ')
#num2 = input('Введите второе число ')
#sum = num1 + num2
#print(sum)

#Модуль 1 часть 3  Задача 4

#tempCel = int(input('Введите градусы по Цельсия '))
#tempFa = tempCel * 9 // 5 + 32
#print('В', tempCel, 'градусов Целься', 'градусов по Фаренгейту', tempFa)


#Д3 2
#Модуль 2 часть 1  Задача 1

#numberA = int(input('Введите число 1 '))
#numberB = int(input('Введите число 2 '))
#numberC = int(input('Введите число 3 '))
#programm = input('Выберите действие + или * ')
#if programm == "+":
# summ = numberA + numberB + numberC
# print('Сумма равна ', summ)
#else:
# proz = numberA * numberB * numberC
#print('Произвеление равно', proz)


#one = int(input('Введите первое число '))
#two = int(input('Введите второе число '))
#three = int(input('Введите третее число '))

#programm = input('Выберете max, min, mid ')

#if programm == "max":
#    if two < one > three:
#       print('Максимальное число', one)
#  elif one < two > three:
#     print('Максимальное число', two)
#else:
#    print('Максимальное число', three)
#elif programm == 'min':
#   if two > one < three:
#     print('Минимальное число', one)
#  elif one > two < three:
#  print('Минимальное число ', two)
#else:
#     print('Минемальное число ', three)
#elif programm == 'mid':
#  midls = ((one + two + three) // 3)
# print('Среднее арефмитическое ', midls)


#Модуль 2 часть 1  Задача 3

#lineMetr = int(input('Введите кол-во метров '))
#program = input('Выберете конвертацию ml, du, ya ')

#if program == 'ml':
#    mili = lineMetr * 0.00062137
#    print(lineMetr, 'метров равняются', mili, 'Миль')
#elif program == 'du':
#    duim = lineMetr * 39.370
#    print(lineMetr, 'метров равняются', duim, 'Дюймам')
#elif program == 'ya':
#    yard = lineMetr * 0,9144
#    print(lineMetr, 'метров равняются ', yard, 'Ярадам')


#Модуль 2 часть 2  Задача 1

#listWeek = input('Введите номер дня в неделе (1-7) ')

#if listWeek == "1":
#   print('Понедельник')
#elif listWeek == '2':
#    print('Вторник')
#elif listWeek == '3':
#   print('Среда')
#elif listWeek == '4':
#    print('Четверг')
#elif listWeek == '5':
#    print('Пятница')
#elif listWeek == '6':
#    print('Суббота')
#elif listWeek == '7':
#    print('Восерсеьне')

#Модуль 2 часть 2  Задача 2

#mouthList = input('Ввежите номер месяца (1 - 12) ')

#if mouthList == '1':
#    print('Январь')
#elif mouthList == '2':
#    print('Февраль')
#elif mouthList == '3':
#    print('Март')
#elif mouthList == '4':
#    print('Апрель')
#elif mouthList == '5':
#    print('Май')
#elif mouthList == '6':
#    print('Июнь')
#elif mouthList == '7':
#    print('Июль')
#elif mouthList == '8':
#    print('Август')
#elif mouthList == '9':
#    print('Сентябрь')
#elif mouthList == '10':
#    print('Октябрь')
#elif mouthList == '11':
#    print('Ноябрь')
#elif mouthList == '12':
#    print('Декабрь')


#Модуль 2 часть 2  Задача 3

#number = int(input('Введите число '))
#if number > 0:
#    print('Number is positive')
#elif number < 0:
#    print('Number is negative,')
#elif number == 0:
#   print('Number is equal to zero')

#Модуль 2 часть 2  Задача 4

#numberOne1 = int(input('Введите число 1 '))
#numberTwo2 = int(input('Введите число 2 '))

#while numberOne1 != numberTwo2:
#    if numberOne1 > numberTwo2:
#       print(numberOne1, numberTwo2)
#  elif numberOne1 < numberTwo2:
#       print(numberTwo2, numberOne1)
#   break
#else:
#    numberOne1 == numberTwo2
#   print('Числа равны')

#Модуль 2 часть 3  Задача 1 ???

#number = int(input('Введите число от 1 до 100 '))

#for number in range (1,100):
#   if number % 3 == 0:
#       print('Fizz')
#    elif number % 5 == 0:
#       print('Buzz')
#   else:
#       print('Ошибка')


#while number < 1 and number > 100:
#print('Ошибка')
#continue
# if number % 3 == 0:
#   print('Fizz')
# elif number % 5 == 0:
#     print('Buzz')
#elif number % 3 != 0 and number % 5 != 0:
#     print('Fizz Buzz')


#Модуль 2 часть 3  Задача 2


#oneNumber = int(input('Введите число '))

#for a in range (0,7):
#   print(oneNumber ** a)

#Модуль 2 часть 3  Задача 3

#abonentCash = int(input('Введите стоимость разговора '))
#operationOne = input('Выберете оператор c которго идет звонок 1, 2, 3 ' )
#operationTwo = input('Выберете оператор принимающий звонок 1, 2, 3 ')

#count = abs(abonentCash)

#a = 2
#b = 3
#c = 5

#if operationOne == '1' and operationTwo == '2':
#    count -= a
#    print ('Стоимость звонка', a, 'руб', 'Остаток', count, 'руб')
#elif operationOne == '2' and operationTwo == '1':
#    count -= b
#    print ('Стоимость звонка', b, 'руб', 'Остаток', count, 'руб')
#elif operationOne == '3' and operationTwo == '1':
#    count -= c
#    print ('Стоимость звонка', c, 'руб', 'Остаток', count, 'руб')


#Модуль 2 часть 3  Задача 4

#managerOne = int(input('Продажи первого менеджера '))
#managerTwo = int(input('Продажи второго менеджера '))
#managerThree = int(input('Продажи третьего менеджера '))
#cash = 200

#if 0 < managerOne < 500:
#    a = ((managerOne * 3) // 100) + cash
#elif 0 < managerTwo < 500:
#    b = ((managerTwo * 3) // 100) + cash
#elif 0 < managerThree < 500:
#    c = ((managerThree * 3) // 100) + cash
#elif 500 == managerOne < 1000:
#    e = ((managerOne * 5) // 100) + cash
#elif 500 == managerTwo < 1000:
#    r = ((managerOne * 5) // 100) + cash
#elif 500 == managerTwo < 1000:
#    t = ((managerTwo * 5) // 100) + cash
#elif 500 == managerThree < 1000:
#    y = ((managerThree * 5) // 100) + cash

#Модуль 3 часть 1  Задача 1


#oneNumber = int(input('Введите число 1 '))
#twoNumber = int(input('Введите число 2 '))

#for num in range(oneNumber, twoNumber):
#   if num % 7 == 0:
#      print('кратные 7-ми', num)


#Модуль 3 часть 1  Задача 2

#numOne = int(input('Введите число 1 ' ))
#numTwo = int(input('Введите число 2 ' ))


#for n in range(numOne,numTwo + 1):
#    print(n)
#for num in range(numTwo, numOne - 1, - 1):
#   print(num)
#for num1 in range(numOne,numTwo +1):
#    if num1 % 7 == 0:
#        print() 
#counter = 0
#for num2 in range(numOne,numTwo + 1):
#    if num2 % 5 == 0:
#       counter += 1
#print(counter)

#Модуль 3 часть 1  Задача 3

#range1 = int(input('введите число 1 '))
#range2 = int(input('введите число 2 '))

#for i in range(range1,range2):
#    if i % 3 == 0:
#        print('Fizz')
#    elif i % 5 == 0:
#        print('Buzz')
#    elif i % 3 == 0 and i % 5 == 0:
#        print('Fizz Buzz')
#    elif i % 3 != 0 and i % 5 != 0:
#        print(i)


#Модуль 3 часть 2  Задача 1


#number1 = int(input('Введите число 1 '))
#number2 = int(input('введите число 2 '))
#counter = 0

#for n in range (number1,number2):
#    if n % 2 == 0:
#       counter += 1
#print(counter)

#for a in range(number1,number2):
#    if a % 2 != 0:
#        counter += 1
#print(counter)

#for c in range(number1,number2):
#    if c % 9 == 0:
#        counter += 1
#print(counter)

#sum = (n + a + c )// 3
#print(sum)

#Модуль 3 часть 2  Задача 2

#dlinna = int(input('Введите длину линии '))
#simbol = input('Выберет симовол ')
#sum = (simbol + "\n") * dlinna
#print(sum)


#Модуль 3 часть 2  Задача 3 

#while True:
#enterNumber = int(input('Введите число '))
#    if enterNumber > 0 and eterNumber != 7:
#        print('«Number is positive»')  
#    elif enterNumber < 0:
#        print('«Number is negative»')     
#    elif enterNumber == 0:
#        print('«Number is equal to zero»')  
#    elif enterNumber == 7:
#        print('Good bye') 
#        break   


#Модуль 3 часть 2  Задача 4 

#sum = 0
#min = None
#max = None

#while True:
#    num = int(input('Введите число '))
#    if num == 7:
#        print('Good bye')
#        break
#    if min==None and max==None:
#        min = num
#        max = num
#    if num > max:
#        max = num
#    if num < min:
#        min = num
#    sum += num
#    print('Сумма ', sum, 'Минимум' ,min,'Максимум', max )

#Модуль 3 часть 3  Задача 1 

#numberX = int(input('Введите число 1 '))
#numberY = int(input('Введите число 2 '))
#summ = numberX ** numberY

#print(summ)


#Модуль 3 часть 3  Задача 2

#counter = 0

#for n in range(100,999 +1):
#    n = str(n)
#    if n[0] == n[1] or n[0] == n[2] or n[1] == n[2]:
#        counter += 1
#print(counter)

#Модуль 3 часть 3  Задача 3

#coont = 0

#for n in range(100,999):
#    n = str(n)
#    if n[0] != n[1] or n[0] != n[2] or n[1] != n[2]:
#        coont += 1
#for n in range(1000, 9999 +1):
#    n = str(n)
#   if n[0] != n[1] or n[0] != n[2] or n[0] != n[3] or n[1] != [2] or n[1] != n[3] or n[2] != n[3]:
#       coont += 1
#print(coont)

#Модуль 3 часть 3  Задача 4

#numOne = int(input('Введите число '))

#tail = ''

#while numOne:
#    if not (numOne%10 == 3 or numOne%10 == 6):
#        tail = str(numOne%10) + tail
#    numOne //= 10
#print(tail)

#Модуль 3 часть 4  Задача 1????


# rangeOne = int(input('Ввеите начало диапозона '))
# rangeTwo = int(input('Ввеите конец диапозона '))


# for num in range(rangeOne,rangeTwo+1):
#     for num2 in range(rangeOne,rangeTwo+1):
#         if num % num2:


#Модуль 3 часть 4  Задача 2


# for n in range(1,10 +1):
#     for j in range(1,10 +1):
#         print(n * j, end='\t')
#     print('\n')


#Модуль 3 часть 4  Задача 3


# rangeOne = int(input('Вверхняя граница диапазона '))
# rangeTwo = int(input('Введите нижнию границу диапазона '))

# for n in range(1, 10 +1):
#     for j in range(rangeOne,rangeTwo +1):
#         print(n * j, end='\t')
#     print('\n')


#Модуль 3 часть 4  Задача 4 ???


# ПЗ Модуль 1 часть 3 Задание 1


# myNum = int(input('Введите 2х значное число '))

# a = myNum % 10
# b = myNum // 10
# print(b,'\n',a)


# ПЗ Модуль 1 часть 3 Задание 2

# myNum = int(input('Введите 3х значное число '))

# a = myNum % 10
# b = myNum % 100 // 10
# c = myNum // 100
# sum = a+b+c
# print('\n',c,'\n',b,'\n',a)
# print(sum)


# ПЗ Модуль 1 часть 3 Задание 3

# myNumber1 = input('введите число 1 ')
# myNumber2 = input('введите число 2 ')

# concr = myNumber1 + myNumber2

# print(concr)

# ПЗ Модуль 1 часть 3 Задание 4


# myCel = int(input('Введите градус цельсия '))

# myFa = ((myCel * 9) % 5) + 32

# print('Граус', myCel, 'Цельсия', 'Равен', myFa, 'Фарингейта')


# ПЗ Модуль 2 часть 1 Задание 1

# myNum = int(input('введите число '))

# if myNum % 2 == 0:
#     print(myNum, 'Even number.')
# else:
#     print(myNum, 'Odd number.')


# ПЗ Модуль 2 часть 1 Задание 2


# myNum = int(input('введите число '))

# if myNum % 7 == 0:
#     print(myNum,'Number is multiple 7')
# else:
#     if myNum % 7 != 0:
#         print(myNum, 'Number is not multiple 7')


# ПЗ Модуль 2 часть 1 Задание 3

# myNumOne = int(input('введите число 1 '))
# myNumTwo = int(input('введите число 2 '))

# if myNumOne > myNumTwo:
#     print('максимум ', myNumOne)
# else:
#     print('максиму', myNumTwo)


# ПЗ Модуль 2 часть 1 Задание 4

# myNumOne = int(input('введите число 1 '))
# myNumTwo = int(input('введите число 2 '))

# if myNumOne < myNumTwo:
#     print('минум ', myNumOne)
# else:
#     print('миниму', myNumTwo)


# ПЗ Модуль 2 часть 1 Задание 5


# myNumOne = int(input('введите число 1 '))
# myNumTwo = int(input('введите число 2 '))
# opiration = input('Выберетие операцию (+, *, -, u) ')


# if opiration == '+':
#     sum = myNumOne + myNumTwo
#     print('сумма равна ', sum)
# elif opiration == '*':
#     proiz = myNumOne * myNumTwo
#     print('произведение ', proiz)
# elif opiration == '-':
#     raz = myNumOne - myNumTwo
#     print('Разность ', raz)
# elif opiration == 'u':
#     aref = (myNumOne + myNumTwo) % 2
#     print('Среднеаремитичесоке ', aref)

# ПЗ Модуль 2 часть 2 Задание 1


# myTime = int(input('Введите время в секундах '))

# opiration = input('Выберете в чем отобразть h,m,s ')

# if opiration == 'h':
#     hours = (86400 - myTime)//3600
#     print('До полуночи останется ', hours, 'часов')
# elif opiration == 'm':
#     min = (86400 - myTime) // 60 
#     print('До полуночи останется ', min, 'минут')
# elif opiration == "s":
#     sec = 86400 - myTime
#     print('До полуночи останется ', sec, 'секунд')


# ПЗ Модуль 2 часть 2 Задание 2


# myD = int(input('ВВедиет диметр окружности '))
# operator = input('Введите операцию s, l ')


# if operator == 's':
#     S = ((myD ** 2)// 4) * 3.14
#     print('Площадь окружности равно ', S)
# elif operator == 'l':
#     L = 3.14 * myD
#     print('Периметр окружности будет равен ', L)


# ПЗ Модуль 2 часть 2 Задание 3


# price = int(input('Введите стоимость приставки '))
# quan = int(input('Введите кол-во приставок '))
# saly = int(input('введите скидку '))

# summ = ((price * quan)* saly) // 100 
# sumSaly = price * quan - summ

# print('Сумма заказа с учетом скидки будет ', sumSaly)


# ПЗ Модуль 2 часть 2 Задание 4 ???

# sizeGB = int(input('Введите размер файла в ГБ '))
# speedNet = int(input('Введите скокрость  байт в секунду '))


# ПЗ Модуль 2 часть 2 Задание 5

# myTime = int(input('Введите колл-во часов '))

# if myTime >0 and myTime < 6:
#     print('Ночь')
# elif myTime >= 6 and myTime < 13:
#     print('Утро')
# elif myTime >= 13 and myTime < 17:
#     print('День')
# else:
#     print('Вечер')


# ДЗ Модуль 4 Часть 1 Задача 1


# myList = input('Введите текст ')


# myList = myList.lower()
# myList = myList.replace(' ', '')

# if myList == myList[::-1]:
#     print('Строка палиндром')
# else:
#     print('Страка не палинром')


# ДЗ Модуль 4 Часть 1 Задача 2

# myText = input('введите текст ')
# myList = input('Введите через пробел зарезервированые слова ').split()

# for word in myList:
#     myText = myText.replace(word,str(word.upper()))
# print(myText)


# ДЗ Модуль 4 Часть 1 Задача 3

# import re

# myText = input('Введите текст ') 

# newlist = re.split(r'[.!?...]+', myText)

# count = 0

# for char in myText:
#     if char in '.!?':
#         count += 1

# print(f'В тексте {count} предложений')


# ДЗ Модуль 4 Часть 2 Задача 1

# import re

# myText = input('Введите вырвжение ')
# operation = input('Выберите операцию +, -, *, / ')

# newList = re.split(r'[\D]', myText)

# if operation == '+':
#     sum = int(newList[0]) + int(newList[1])
#     print(sum)
# elif operation == '-':
#     raz = int(newList[0]) - int(newList[1])
#     print(raz)
# elif operation == '*':
#     proiz = int(newList[0]) * int(newList[1])
#     print(proiz)
# elif operation == '/':
#     deli = int(newList[0]) / int(newList[1])
#     print(deli)


# ДЗ Модуль 4 Часть 2 Задача 2


# my_str = input('Введите числа ').split()

# min(my_str)
# max(my_str)
# coun = 0 
# counz = 0
# counO = 0
# for n in my_str:
#     n = int(n)
#     if n > 0:
#         coun += 1
#     print('Положительных чисел ', coun)
#     if n < 0:
#         counz +=1
#     print('отрицательных чисел ', counz)
#     if n == 0:
#         counO += 1
#     print("Колл-во 0 ", counO )


# Модуль 4 часть 3 задача 1

# my_listOne = input('Введите список чисел ').split()
# my_listTwo = input('Введите список чисел ').split()

# max(my_listOne)
# min(my_listOne)
# max(my_listTwo)
# min(my_listTwo)

# print(my_listOne)
# print(my_listTwo)

# my_listThree = my_listOne + my_listTwo

# print(my_listThree)

# my_listThree = []

# for num in my_listOne:
#     if my_listOne.count(num) == 1:
#         my_listThree.append(num)
# for num2 in my_listTwo:
#     if my_listTwo.count(num2) == 1:
#         my_listThree.append(num2)
# print(my_listThree)


# for num_One in my_listOne:
#     if my_listOne.count(num_One) != 1:
#         my_listThree.append(num_One)
# for num_two in my_listTwo:
#     if my_listTwo.count(num_two) != 1:
#         my_listThree.append(num_two)
# print(my_listThree)


# for nO in my_listOne:
#     for n1 in my_listTwo:
#         if nO == n1:
#             my_listThree.append(nO)
# print(my_listThree)

# for n_one in my_listOne:
#     if n_one == max(my_listOne):
#         my_listThree.append(n_one)
#     elif n_one == min(my_listOne):
#         my_listThree.append(n_one)
# for n_two in my_listTwo:
#     if n_two == max(my_listTwo):
#         my_listThree.append(n_two)
#     elif n_two == min(my_listTwo):
#         my_listThree.append(n_two)
# print(my_listThree)


# ПЗ Модуль 3 часть 1 задача 1

# my_str = input('Введите строку ')

# print(my_str[::-1])


# import re

# my_str = input('Введите строку ')

# word = re.search('[a-z]+', my_str)

# print(word)


# ДЗ Модуль 5 часть 1 задача 1

# def my_txt():
#      print('“Dont compare yourself with anyone in this world… \nif you do so, you are insulting yourself.” \n\t\t\t\t\tBill Gates')
# my_txt()


# ДЗ Модуль 5 часть 1 задача 2
# def my_Fun(a,b):
#     for n in range(a,b):
#         if n % 2 == 0:
#             print(n)
# print(my_Fun(1,10))    

# ДЗ Модуль 5 часть 1 задача 4


# def minNumber(a,b,c,d,e,):
#     min1 = min(a,b)
#     min2 = min(c,d)
#     min3 = min(min1,min2)
#     return min(min3,e)

# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))
# d = int(input('d = '))
# e = int(input('e = '))
# print(minNumber(a,b,c,d,e))

# ДЗ Модуль 5 часть 1 задача 5

# def someFunc(a:int,b:int)-> int:
#     res = 1
#     if a > b:
#         a,b = b,a
#         for n in range(a,b+1):
#             res *= n
#         return res
#     elif a < b:
#         for n in range(a,b+1):
#             res *= n
#         return res
# a = int(input('1 '))
# b = int(input('2 '))
# print(someFunc(a,b))


# ДЗ Модуль 5 часть 1 задача 6

# def lenNumber(a):
#     return len(a)
# a = input("enter number ")
# print(lenNumber(a))

# # ДЗ Модуль 5 часть 1 задача 7

# def my_poli(a:list):
#     if a == a[::-1]:
#         print("Строка полиндром")
#     else:
#         print('Строка не полиндром ')
# print(my_poli(a=input('enter number ')))


# # ДЗ Модуль 5 часть 2 задача 1

# def my_func(a:int):
#     p = 1
#     for i in a:
#         i = int(i)
#         p*=i
#         print(p, type(i), type(a),type(p))
# a = input('enter ').split()
# my_func(a)

    

# ДЗ Модуль 5 часть 2 задача 2

# def min_number(a:int):
#     """Функция выполняет поиск 
#         минимального числа из списка целых
#     """
#     min1 = min(a)
#     print(min1,type(a),type(min1))
# a = input('enter ').split()
# min_number(a)

# ДЗ Модуль 5 часть 2 задача 3

# def int_praim(a:int):
    
#     for i in a:
#         count = 0
#         i = 2
#         i = int(i)
#         if i % i and  i % 1:
#             count+=1
#         print(count,type(i),type(a))
#     else:
#         print('number not praim')
# a = input('enter ').split()
# int_praim(a)



# ДЗ Модуль 5 часть 2 задача 4

# Напишите функцию, удаляющую из списка целых
# некоторое заданное число. Из функции нужно вернуть
# количество удаленных элементов.

# def remove_func(a):
#     count = 0
#     new_List = list(a)
#     for n in a:
#         n = input('delit numb ')
#         new_List.remove(n)
#         count += 1
#     print(count)
        
# a = input('enter list ').split()
# remove_func(a)        
    


# ДЗ Модуль 5 часть 2 задача 5

# def my_sumFunc(a,b):
#     c = a + b
#     return c
# a = input('enter1 ')
# b = input('enter2 ')
# print(my_sumFunc(a,b))


# # ДЗ Модуль 5 часть 2 задача 6

# Напишите функцию, высчитывающую степень каждого
# элемента списка целых. Значение для степени передаётся
# в качестве параметра, список тоже передаётся в качестве
# параметра. Функция возвращает новый список, содержа-
# щий полученные результаты.


# def stepen_el(a,b):
    
#     new_list = []
#     for i in a:
#      new_list.append(int(i) ** b)
#     print(new_list,a)
      
# a = input('enter ').split()
# b = int(input('enter stepen '))
# print(stepen_el(a,b))


# ДЗ Модуль 5 часть 2 задача 5

# Напишите функцию, которая получает два списка в
# качестве параметра и возвращает список, содержащий
# элементы обоих списков.


# def my_dubl_list(a,b):
#     """Данная функция получает 2 списка 
#     и возвращает содержащие элементы обоих списков"""
#     three_list = list(a)+list(b)
#     print(three_list)
# a = input('enter list 1 ').split()
# b = input('enter list 2 ').split()
# my_dubl_list(a,b)

# ДЗ Модуль 5 часть 3 задача 1????

# Написать рекурсивную функцию нахождения наи-
# большего общего делителя двух целых чисел.

# import re

# def re_serch_max():
#     """Данная функция метод рекурсии находит 
#     наибольший общий делитель целых чисел"""

# ДЗ Модуль 7 часть 1 задача 1

# Необходимо отсортировать первые две трети списка
# в порядке возрастания, если среднее арифметическое
# всех элементов больше нуля; иначе — лишь первую треть.
# Остальную часть списка не сортировать, а расположить
# в обратном порядке.

# def sotrt_list(a:list, b:int):
#     """Данная функция спртирует список в порядке 
#     возрвстания, если среднее арефмитическое всех элементов > 0
#     иначе сортирует только первую часть """
#     new_avg = len(a) / float(b)
#     new_list = []
#     last = 0.0

#     while last < len(a):
#         new_list.append(a[int(last): int(last + new_avg)])
#         last += new_avg
#     sum1 = 0
#     sum2 = 0
#     sum3 = 0
#     new_arr = []
#     arr1 = []
#     for i in new_list[0]:
#         arr1.append(i)
#         new_arr.append(i)
#         sum1 += int(i)
#     for i in new_list[1]:
#         new_arr.append(i)
#         sum2 += int(i)
#     for i in new_list[2]:
#         sum3 += int(i)
#     sum_all = sum1+sum2+sum3
#     print(sum1,sum2,sum3, new_arr, arr1, sum_all, a, new_list)

#     if sum_all > 0:
#         new_arr.sort()
#         print(new_arr)
#     else:
#         arr1.sort()
#         print(arr1)
# a = input('enter ').split()
# b = int(input('enter number '))
# sotrt_list(a,b)




# ДЗ Модуль 7 часть 1 задача 2

# Написать программу «успеваемость». Пользователь
# вводит 10 оценок студента. Оценки от 1 до 12 Реализовать
# меню для пользователя:
# ■ Вывод оценок (вывод содержимого списка);
# ■ Пересдача экзамена (пользователь вводит номер эле-
# мента списка и новую оценку);
# ■ Выходит ли стипендия (стипендия выходит, если
# средний бал не ниже 10.7);
# ■ Вывод отсортированного списка оценок: по возрас-
# танию или убыванию.


# def academic_perfomence(a):
#     print(a)

#     total = 0

#     index_list = int(input('enter index '))
#     ball = int(input('enter ball '))
#     a[index_list] = ball
#     print(a)


#     for number in a:
#         total += int(number)
#         total_ball = (total / len(a))
#     if total_ball >= 10.7:
#         print('money is OK ')
#     else:
#         print('no money ')

#     a.sort()
#     print(a[::-1], a)

# a = list(input('enter ball ').split())
# print(academic_perfomence(a))


# ДЗ Модуль 7 часть 1 задача 1

# Необходимо отсортировать первые две трети списка
# в порядке возрастания, если среднее арифметическое
# всех элементов больше нуля; иначе — лишь первую треть.
# Остальную часть списка не сортировать, а расположить
# в обратном порядке.

def sotrt_list(a:list):
    """Данная функция спртирует список в порядке 
    возрвстания, если среднее арефмитическое всех элементов > 0
    иначе сортирует только первую часть """
    sum=0
    for x in a:
      sum+=x
    avg = sum/len(a)
    print(avg)

    limit = 0
    if avg>0:
      limit = 2*int(len(a)/3)
    else:
      limit = int(len(a)/3)
         
    first_arr = a[:limit]
    second = a[limit:]
    first_arr.sort()
    second.reverse()
    return [*first_arr,*second]
    

a = [x for x in range(-100,90,3)]
print(sotrt_list(a))

# ДЗ Модуль 7 часть 2 задача 2

# Есть четыре списка целых. Необходимо объединить
# в пятом списке только те элементы, которые уникальны
# для каждого списка. Полученный результат в зависимости
# от выбора пользователя отсортировать по убыванию или
# возрастанию. Найти значение, введенное пользователем,
# с использованием бинарного поиска.



# a = list(input('enter number1 '))
# b = list(input('enter number2 '))
# c = list(input('enter number3 '))
# d = list(input('enter number4 '))
# req = input('Выбрать сортировку возрастание/убывание 1/0 ')

# e = []

# for x in a:
#     if x not in e:
#         e.append(x)
# for x1 in b:
#     if x1 not in e:
#         e.append(x1)
# for x2 in c:
#     if x2 not in e:
#         e.append(x2)
# for x3 in d:
#     if x3 not in e:
#         e.append(x3)

# if req == 1:
#     e.sort()
#     print(e)
# else:
#     e.sort(reverse=True)
#     print(e)


# Модуль 8 часть 1 задание 1

# Есть три кортежа целых чисел необходимо найти
# элементы, которые есть во всех кортежах.


# cor1 = (1,2,3,4,5)
# cor2 = (1,5,6,1,8)
# cor3 = (1,2,5,1,2)

# serch_elements_tuple = set(cor1).intersection(set(cor2), set(cor3))

# result_tuple = tuple(serch_elements_tuple)

# print('Общие элементы в кортежже: ', result_tuple)


# Модуль 8 часть 1 задание 2

# Есть три кортежа целых чисел необходимо найти
# элементы, которые есть во всех кортежах.

# cor1 = (1,2,3,4,5)
# cor2 = (1,5,6,1,8)
# cor3 = (1,2,5,1,2)

# unicals_element = set(cor1) ^ set(cor2) ^ set(cor3)

# tuple_element_result = tuple(unicals_element)

# print('уникальные элементы в кортеже: ', tuple_element_result)


# Модуль 8 часть 1 задание 3

# Есть три кортежа целых чисел необходимо найти
# элементы, которые уникальны для каждого списка.


# cor1 = (1,2,3,4,5)
# cor2 = (1,5,6,1,8)
# cor3 = (1,2,5,1,2)

# result_tuple = ()

# for i in range(min(len(cor1), len(cor2), len(cor3))):
#     if cor1[i] == cor2[i] == cor3[i]:
#         result_tuple += (cor1[i], )
# print('Элементы уникальные для каждого списка ', result_tuple)



# определение функции декоратора
# def select(input_func):    
#     def output_func():      # определяем функцию, которая будет выполняться вместо оригинальной
#         print("*****************")  # перед выводом оригинальной функции выводим всякую звездочки
#         input_func()                # вызов оригинальной функции
#         print("*****************")  # после вывода оригинальной функции выводим всякую звездочки
#     return output_func     # возвращаем новую функцию
 
# # определение оригинальной функции
# @select         # применение декоратора select
# def hello():
#     print("Hello METANIT.COM")
 
# # вызов оригинальной функции
# hello()



# модуль 8 часть 2 задание 1

# Создайте программу, хранящую информацию о вели-
# ких баскетболистах. Нужно хранить ФИО баскетболиста и
# его рост. Требуется реализовать возможность добавления,
# удаления, поиска, замены данных. Используйте словарь
# для хранения информации.

# players = {}
# def add_players():
#     name = input('Введите ФИО спортсмена ')
#     height = float(input('Введите его рост '))
#     players[name]= height
#     print('Спортмен добавлен ')
#     print(players)
#     # add_players()
    
    

# def del_player():
#     name = input('Введите ФИО что бы удалить игрока ')
#     if name in players:
#         del players[name]
#         print(players)
#     else:
#         print('Игрок не найден')


# def find_player():
#     name = input('Введите ФИО спортсмена для поиска ')
#     if name in players:
#         height  = players[name] 
#         print(f"Рост баскетболиста {name}:{height} см")
#     else:
#         print('Спротсмен не найден')

# def replace_player():
#     name = input('Введите ФИО спортсмена данные которого необходимо заменить ')
#     if name in players:
#         height = float(input('Введите новый рост спортсмена '))
#         players[name] = height
#         print('Данные успешно изменены ')
#         print(players)
#     else:
#         print('спортмен не найден ')

# add_players()
# find_player()
# replace_player()
# del_player()




# модуль 8 часть 2 задание 2

# Создайте программу «Англо-французский словарь».
# Нужно хранить слово на английском языке и его перевод
# на французский. Требуется реализовать возможность до-
# бавления, удаления, поиска, замены данных. Используйте
# словарь для хранения информации.


# english_frach_directori = {}

# def add_word_direct():
#     eng_word = input('Введите слово на Английском ')
#     fr_word = input('Введите перевод на французском ')
#     english_frach_directori[eng_word] = fr_word
#     print('Слово добавленов словарь')

# def del_word_direct():
#     eng_word = input('Введите английское слово для удаления ')
#     if eng_word in english_frach_directori:
#         del english_frach_directori[eng_word]
#     else:
#         print('Слово не найдено ')

# def find_word_direct():
#     eng_word = input('введите английское слово для поиска ')
#     if eng_word in english_frach_directori:
#         fr_word = english_frach_directori[eng_word]
#         print(f'Найдено слово {eng_word}:{fr_word}')
#     else:
#         print('Слово не найдено ')


# def replase_word_direct():
#     eng_word = input('Введите слово, что бы заменить ')
#     if eng_word in english_frach_directori:
#         fr_word = input('Введите новый перевод ')
#         english_frach_directori[eng_word] = fr_word
#         print('Данные успешно изменены ')
#     else:
#         print('Слово не найдено ')


# модуль 8 часть 2 задание 3

# Создайте программу «Фирма». Нужно хранить ин-
# формацию о человеке: ФИО, телефон, рабочий email,
# название должности, номер кабинета, skype. Требуется
# реализовать возможность добавления, удаления, поис-
# ка, замены данных. Используйте словарь для хранения
# информации.

# bisness_firma = {}

# def add_firm_Worker():
# """Эта функция добаляет нового сотрудника"""
#     name = input('Введите ФИО сотрудника')
#     fone = int(input('Укажите телефон сотрудника '))
#     worck_mail = input('Укажите электорнную почту ')
#     job_title = input('Укажите должность сотрудника ')
#     skype_worker = input('Укажите скайп ')
#     bisness_firma[name]=fone,worck_mail,job_title,skype_worker
#     print("Сотрудник добавлен ")

# def del_firm_Worker():
# """Эта функция удаляет сотрудника"""
#     name = input('Введите ФИО сотрудника ')
#     if name in bisness_firma:
#         del bisness_firma[name]
#         print('Сотрудник удален ')
#     else:
#         print('Сотрудник не найден ')

# def find_firm_worker():
# """Эта функция ищет сотрудника """
#     name = input('Введите ФИО сотрудника')
#     if name in bisness_firma:
#         fone = bisness_firma[name]
#         worck_mail = bisness_firma[name]
#         job_title = bisness_firma[name]
#         skype_worker = bisness_firma[name]
#         print(f'Найден сотрудник {name}:{fone},{worck_mail},{job_title},{skype_worker}')
#     else:
#         print('Сотрудник не найден ')

# def replace_firm_worker():
#  '''Эта функция изменяет внутренние данные сотрудника'''
#     name = input('Введите ФИО сотркдника ')
#     if name in bisness_firma:
#         fone = int(input('Укажите телефон сотрудника '))
#         worck_mail = input('Укажите электорнную почту ')
#         job_title = input('Укажите должность сотрудника ')
#         skype_worker = input('Укажите скайп ')
#         bisness_firma[name]=fone,worck_mail,job_title,skype_worker
#         print('Данные успешно обновлены ')
#     else:
#         print('Сотрудник не найден ')


# модуль 8 часть 2 задание 4

# Создайте программу «Книжная коллекция». Нужно
# хранить информацию о книгах: автор, название книги,
# жанр, год выпуска, количество страниц, издательство.
# Требуется реализовать возможность добавления, удале-
# ния, поиска, замены данных. Используйте словарь для
# хранения информации.


# book_colection = {}

# def add_book():
#     author = input('Укажите ФИО автора книги ')
#     name_book = input('Укажите название книги')
#     genre = input('Укажите жарн книги ')
#     year_of_issue = input('Укажите год издания ')
#     number_of_pages = int(input('Ввежите колл-во страниц'))
#     book_colection[author] = name_book,genre,year_of_issue,number_of_pages
#     print('Книга Добавлена ')

# def del_book():
#     author = input('Введите ФИО автора ')
#     if author in book_colection:
#         del book_colection[author]
#         print('Книга удалена ')
#     else:
#         print('Книга не найдена ')

# def find_book():
#     author = input('Введите ФИО автора ')
#     if author in book_colection:
#         name_book = book_colection[author]
#         genre = book_colection[author]
#         year_of_issue = book_colection[author]
#         number_of_pages = book_colection[author]
#         print(f'Найдено по запросу {author}:{name_book},{genre},{year_of_issue},{number_of_pages}')
#     else:
#         print('Книга не найдена ')

# def replace_book():
#     author = input("Введите ФИО автора ")
#     if author in book_colection:
#         name_book = input('Укажите название книги')
#         genre = input('Укажите жарн книги ')
#         year_of_issue = input('Укажите год издания ')
#         number_of_pages = int(input('Ввежите колл-во страниц'))
#         book_colection[author] = name_book,genre,year_of_issue,number_of_pages
#         print('Данные успешно изменены ')
#     else:
#         print('Книга не найдена')




# Открытие потоков:

# encoding - указывает тип кодировки (например UTF-8 при работе с тексовыми файлами)
# file - путь файла который будет связан с потоком 
# mode - задает режим открытия для этого потока (например r - чтение ), w - запись, а - дозапись,
# r+ - чтение и обновление, w+ - запись и обновление 

# Аргументы режима могут быть опущенны, тогда принимаються значение по умолчанию:
# режим открытия - r (чтение )
# encoding  - зависит от используемой платформы

# stream = open(file, mode = 'r', encoding = None)   

# try:
#     file = open('./заметка.txt', 'rt')
#     print(file.read())
#     file.close()


# except Exception as exc:
#     print("Cannot open the file:", exc)


# import sys

# sys.stdin
# ▷ stdin (standard input — стандартный ввод)  - поток stdin обычно связан с  клавиатурой, пред-
# варительно открыт для чтения и рассматривается как основной источник данных для запущенных программ;
# ▷ хорошо известная функция input () по умолчанию читает данные из stdin.
    
# ■ sys.stdout - stdout (standard output — стандартный вывод)поток stdout обычно связан с экраном, предвари-
# тельно открыт для записи и рассматривается как основной объект для вывода данных, запущенных программой;
# ▷ хорошо известная функция print() выводит данные в поток stdout.
    
# ■ sys.stderr
# ▷ stderr (standard error output — стандартный поток ошибок) - поток stderr обычно связан с экраном, предварительно
# открыт для записи и рассматривается как основное место, куда запущенная программа должна отправлять
# информацию об ошибках, возникших при ее работе; мы не представили метода для отправки данных в этот
# поток (но обещаем это сделать в ближайшее время). разделение потоков на stdout (полезные результаты,
# полученные программой) и stderr (сообщения об ошибках, безусловно полезные, но они не выводят
# результаты) дает возможность перенаправить эти два типа информации разным получателям. Более под-
# робное обсуждение этого вопроса выходит за рамки нашего курса. Руководство по операционной системе
# даст вам больше информации по этим вопросам.
    

# from os import strerror

# try:
#     cnt = 0
#     s = open('заметка.txt', 'rt')
#     ch = s.read(1)
#     while ch != '':
#         print(ch, end='')
#         cnt += 1
#         ch = s.read(1)
#     s.close()
#     print("\n\nCharacters in file: ", cnt)

# except IOError as e:
#     print("I/O error occurred: ", strerror(e.errno))

# Программа прочитала заметку и посчитала символы
    


# Упрощенный метод записи 
    

# try:
#     for line in open('./заметка.txt', 'rt'):
#         print(line, end='')
# except Exception as exc:
#     print("Cannot open the file: ", exc)


# Програма дописать в имеющийся текстовый файл и прочитать его 
# try:

#     s = open('заметка.txt', 'at')
#     s.write('new sting\n')
#     s.close()

# except Exception as exc:
#     print("Cannot open the file: ", exc)
        
# try:
#     for line in open('./заметка.txt', 'rt'):
#         print(line, end='')
# except Exception as exc:
#     print("Cannot open the file: ", exc)



# Модуль 9 часть 1 Задание 1

# Дано два текстовых файла. Выяснить, совпадают ли
# их строки. Если нет, то вывести несовпадающую строку
# из каждого файла.

# try:
#     with open('txt1.txt', 'r') as txt1, open('txt2.txt', 'r') as txt2:
#         lines1 = txt1.readlines()
#         lines2 = txt2.readlines()

#         if len(lines1) != len(lines2):
#             print("Количество строк во входных файла не совпадает.")
        

#         for line1, line2 in zip(lines1, lines2):
#             if line1.strip()!= line2.strip():
#                 print(f"Несовпадающие строки:\n{line1.strip()}\n{line2.strip()}")
# except FileNotFoundError:
#     print("Один или оба из входных файла не найдены.")


# Модуль 9 часть 1 Задание 2

# Дан текстовый файл. Необходимо создать новый файл
# и записать в него следующую статистику по исходному
# файлу:
# ■ Количество символов;
# ■ Количество строк;
# ■ Количество гласных букв;
# ■ Количество согласных букв;
# ■ Количество цифр.


# try:
#     with open('txt1.txt', 'r') as txt1_file, open('newfile.txt', 'w') as newfile_file:
#         symbols_count = 0
#         lines_count = 0
#         vowels_count = 0
#         consonants_count = 0
#         digits_count = 0

#         for line in txt1_file:
#             lines_count += 1
#             symbols_count += len(line.strip())

#             for char in line.strip():
#                 if char.isalpha():
#                     if char.lower() in 'аоуэиыеёюя':
#                         vowels_count += 1
#                     else:
#                         consonants_count += 1
#                 elif char.isdigit():
#                     digits_count += 1
        

#         newfile_file.write(f"Количество символов: {symbols_count}\n")
#         newfile_file.write(f"Количество строк: {lines_count}\n")
#         newfile_file.write(f"Количество гласных букв: {vowels_count}\n")
#         newfile_file.write(f"Количество согласных букв: {consonants_count}\n")
#         newfile_file.write(f"Количество цифр: {digits_count}\n")
        

# except Exception as e:
#     print("Ошибка:", e)

# try:
#     with open('newfile.txt', 'r') as newfile_file:
#         print("Статистика из исходного файла:")
#         for line in newfile_file:
#             print(line.strip())
# except Exception as e:
#         print("Ошибка при чтении из нового файла:", e)


# Модуль 9 часть 1 Задание 3

# Дан текстовый файл. Удалить из него последнюю
# строку. Результат записать в другой файл.

# try:
#     with open('txt1.txt', 'r') as txt1_file, open('newfile.txt', 'w') as newfile_file:
#         lines = txt1_file.readlines()
#         newfile_file.writelines(lines[:-1])
# except Exception as e:
#     print("Ошибка:", e)

# try:
#     with open('newfile.txt', 'r') as newfile_file:
#         print("Статистика из исходного файла:")
#         for line in newfile_file:
#             print(line.strip())
# except Exception as e:
#         print("Ошибка при чтении из нового файла:", e)


# Модуль 9 часть 1 Задание 4

# Дан текстовый файл. Найти длину самой длинной
# строки.


# try:
#     with open('txt1.txt', 'r') as txt1_file:
#         max_length = 0
#         for line in txt1_file:
#             length = len(line.strip())
#             if length > max_length:
#                 max_length = length

#     print("Длина самой длинной строки:", max_length)
# except Exception as e:
#     print("Ошибка:", e)


# Модуль 9 часть 1 Задание 5

# Дан текстовый файл. Посчитать сколько раз в нем
# встречается заданное пользователем слово.


# word = input("Введите слово: ")

# try:
#     with open('txt1.txt', 'r') as txt1_file:
#         word_count = 0
#         for line in txt1_file:
#             words = line.strip().split()
#             for w in words:
#                 if w.lower() == word.lower():
#                     word_count += 1
#         print(f"Слово '{word}' встречается {word_count} раз.")
# except Exception as e:
#     print("Ошибка:", e)


# Модуль 9 часть 1 Задание 6

# Дан текстовый файл. Найти и заменить в нем задан-
# ное слово. Что искать и на что заменять определяется
# пользователем.


# word_to_find = input("Введите слово для поиска: ")
# word_to_replace = input("Введите слово для замены: ")


# try:
#     with open('txt1.txt', 'r') as txt1_file, open('newfile.txt', 'w') as newfile_file:
#         for line in txt1_file:
#             newfile_file.write(line.replace(word_to_find, word_to_replace))
#         print("Замены произведены.")
# except Exception as e:
#     print("Ошибка:", e)

# Модуль 9 часть 2 задание 1

# Напишите информационную систему «Сотрудники».
# Программа должна обеспечивать ввод данных, редактирование данных сотрудника, удаление сотрудника, поиск
# сотрудника по фамилии, вывод информации обо всех сотрудниках, указанного возраста, или фамилия которых
# начинается на указанную букву. Организуйте возможность сохранения найденной информации в файл. Также весь
# список сотрудников сохраняется в файл (при выходе из программы — автоматически, в процессе исполнения
# программы — по команде пользователя). При старте программы происходит загрузка списка сотрудников из
# указанного пользователем файла.

# def staff():

#     def create_empty_file():
#         with open('staff_list.txt', 'at') as file:
#             file.write('')
#             print('Пустой файл staff_list.txt создан.')
#     create_empty_file()

#     def add_staff_list():
#         name = input('Введите имя сотрудника: ')
#         surname = input('Введите фамилию сотрудника: ')
#         age = int(input('Введите возраст сотрудника: '))
#         position = input('Введите должность сотрудника: ')
#         with open('staff_list.txt', 'at') as file:
#             file.write(f'{name}, {surname}, {age}, {position}\n')
#             file.close()
#         print('Сотрудник добавлен.')
#         try:
#             with open('staff_list.txt', 'r') as list:
#                 read_list = list.read()
#             print(read_list, 'Список сотрудников загружен.')
#         except Exception as e:
#             print('Ошибка при загрузке списка сотрудников:', e)
#     add_staff_list()


#     def find_and_edit_in_file():
#         search_surname  = input('Введите фамилию для поиска: ')
#         try:
#             with open('staff_list.txt', 'r') as file:
#                 for line in file:
#                     if search_surname  in line:
#                         print(line)
#         except Exception as e:
#             print('Ошибка при поиске:', e)
#         surname  = input('Введите фамилию для замены: ')
#         name = input('Введите имя для замены: ')
#         age = int(input('Введите возраст для замены: '))
#         position = input('Введите должность для замены: ')
#         with open('staff_list.txt', 'r') as file:
#             lines = file.readlines()
#             with open('staff_list.txt', 'w') as file:
#                 for line in lines:
#                     if search_surname  in line:
#                         file.write(f'{name}, {surname}, {age}, {position}\n')
#                     else:
#                         file.write(line)
#                         print('Сотрудник изменен.')
#     find_and_edit_in_file()

#     def dell_staff():
#         surname  = input('Введите фамилию для удаления: ')
#         with open('staff_list.txt', 'r') as file:
#             lines = file.readlines()
#         with open('staff_list.txt', 'w') as file:
#             for line in lines:
#                 if surname not in line:
#                     file.write(line)
#                     print('Сотрудник удален.')
#         try:
#             with open('staff_list.txt', 'r') as list:
#                 read_list = list.read()
#             print(read_list, 'Список сотрудников загружен.')
#         except Exception as e:
#             print('Ошибка при загрузке списка сотрудников:', e)
#     dell_staff()

#     def find_staff():
#         search_surname  = input('Введите фамилию для поиска: ')
#         try:
#             with open('staff_list.txt', 'r') as file:
#                 for line in file:
#                     if search_surname  in line:
#                         print(line)
#         except Exception as e:
#             print('Ошибка при поиске:', e)
#     find_staff()

#     def find_by_surname():
#         surname = input('Введите фамилию: ')
#         try:
#             with open('staff_list.txt', 'r') as file:
#                 for line in file:
#                     if surname in line:
#                         print(line)
#         except Exception as e:
#             print('Ошибка при поиске:', e)
#         print('Найденные сотрудники:')
        
#         def find_by_age():
#             age = int(input('Введите возраст: '))
#             try:
#                 with open('staff_list.txt', 'r') as file:
#                     for line in file:
#                         staff_data = line.strip().split(', ')
#                         if int(staff_data[2]) == age:
#                             print(line)
#             except Exception as e:
#                 print('Ошибка при поиске:', e)
#             print('Найденные сотрудники:')
        

#             def find_by_letter():
#                 letter = input('Введите букву для поиска: ')
#                 try:
#                     with open('staff_list.txt', 'r') as file:
#                         for line in file:
#                             staff_data = line.strip().split(', ')
#                             if staff_data[1].startswith(letter):
#                                 print(line)
#                 except Exception as e:
#                     print('Ошибка при поиске:', e)
#                 print('Найденные сотрудники:')
#             find_by_letter()
#         find_by_age()
#     find_by_surname()


#     def save_to_file():
#         try:
#             with open('staff_list.txt', 'r') as file:
#                 read_list = file.read()
#             with open('saved_staff_list.txt', 'w') as file:
#                 file.write(read_list)
#             print('Список сотрудников сохранен в saved_staff_list.txt.')
#         except Exception as e:
#             print('Ошибка при сохранении списка сотрудников:', e)
#     save_to_file()


#     def load_from_file():
#         try:
#             with open('staff_list.txt', 'r') as file:
#                 read_list = file.read()
#             print('Список сотрудников загружен из staff_list.txt.')
#             return read_list
#         except Exception as e:
#             print('Ошибка при загрузке списка сотрудников:', e)
#             return None

#     def main():
#         loaded_list = load_from_file()
#         while True:
#             print('\nМеню:')
#             print('1. Добавить сотрудника')
#             print('2. Изменить информацию о сотруднике')
#             print('3. Удалить сотрудника')
#             print('4. Найти сотрудника по фамилии')
#             print('5. Сохранить список сотрудников в staff_list.txt')
#             print('6. Загрузить список сотрудников из staff_list.txt')
#             print('7. Выйти')
#             try:
#                 choice = int(input('Выберите задачу: '))
#                 if choice in range(1,8 ):
#                     if choice == 1:
#                         add_staff_list()
#                         loaded_list = load_from_file()
#                         print('Список сотрудников загружен из staff_list.txt.')
#                     elif choice == 2:
#                         find_and_edit_in_file()
#                         loaded_list = load_from_file()
#                         print('Список сотрудников загружен из staff_list.txt.')
#                     elif choice == 3:
#                         dell_staff()
#                         loaded_list = load_from_file()
#                         print('Список сотрудников загружен из staff_list.txt.')
#                         print('Найденные сотрудники:')
#                     elif choice == 4:
#                         find_by_surname()
#                         loaded_list = load_from_file()
#                         print('Список сотрудников загружен из staff_list.txt.')
#                         print('Найденные сотрудники:')
#                     elif choice == 5:
#                         save_to_file()
#                         print('Список сотрудников сохранен в staff_list.txt.')
#                     elif choice == 6:
#                         loaded_list = load_from_file()
#                         print('Список сотрудников загружен из staff_list.txt.')
#                         print('Найденные сотрудники:')
#                     elif choice == 7:
#                         break
#                     else:
#                         print('Неверный ввод. Попробуйте снова.')
#                 if loaded_list is None:
#                     print('Список сотрудников:')
#                     print(loaded_list)
#             except ValueError:
#                 print('Неверный ввод. Попробуйте снова.')
#         print('Программа завершена.')
#     main()
# staff()



