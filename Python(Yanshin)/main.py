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

managerOne = int(input('Продажи первого менеджера '))
managerTwo = int(input('Продажи второго менеджера '))
managerThree = int(input('Продажи третьего менеджера '))
cash = 200

if 0 < managerOne < 500:
    a = ((managerOne * 3) // 100) + cash
elif 0 < managerTwo < 500:
    b = ((managerTwo * 3) // 100) + cash
elif 0 < managerThree < 500:
    c = ((managerThree * 3) // 100) + cash
elif 500 == managerOne < 1000:
    e = ((managerOne * 5) // 100) + cash
elif 500 == managerTwo < 1000:
    r = ((managerOne * 5) // 100) + cash
elif 500 == managerTwo < 1000:
    t = ((managerTwo * 5) // 100) + cash
elif 500 == managerThree < 1000:
    y = ((managerThree * 5) // 100) + cash



if 0 < managerOne < 500 or 500 == managerOne < 1000 or managerOne > 1000:
    