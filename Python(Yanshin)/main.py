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