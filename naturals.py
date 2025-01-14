class Natural:
    def __init__(self, number):
        """Принимает строку, выдает натуральное число, Смирнов Иван"""
        self.A = list(int(i) for i in number)
        self.n = len(self.A)

    def __str__(self):
        """Возвращает строковое представление числа. Малых Андрей"""
        return "".join(map(str, self.A))


def COM_NN_D(a, b):
    """Сравнение натуральных чисел: 2 - если первое больше второго, 0, если равно, 1 иначе. Виноградов Андрей"""
    if a.n == b.n:
        #Сравнение длин чисел, случай если длины равны
        for i in range(a.n):
            #Считывание и проверка каждой цифры
            if a.A[i] > b.A[i]:
                #Если цифра 1-ого числа больше цифры 2-ого числа
                return 2
            elif a.A[i] < b.A[i]:
                #Если цифра 2-ого числа больше цифры 1-ого числа
                return 1
        return 0
    elif a.n > b.n:
        #Длина 1-ого больше длины второго
        return 2
    else:
        #Длина 2-ого больше длины первого
        return 1


def MUL_ND_N(a1, x):
    """Умножение натурального числа на цифру. Дитятьев Иван"""
    a = Natural(str(a1))
    if x != 0:
        a.A.reverse()
        ost = 0
        for i in range(a.n):
            e = a.A[i]
            a.A[i] = (((e * x) + ost) % 10)
            ost = (((e * x) + ost) // 10)
        if i == a.n - 1 and ost > 0:
            a.A.append(ost)
        o = ""
        a.A.reverse()
        for i in a.A:
            o = o + str(i)
        return Natural(o)
    else:
        return Natural('0')


def SUB_NN_N(a1, b1):
    """Вычитание из первого большего натурального числа второго меньшего или равного. Виноградов Андрей"""
    a = Natural(str(a1))
    b = Natural(str(b1))
    #a, b - переменные - копии, чтобы не менялись изначальные данные.
    Ifer = COM_NN_D(a, b)
    #Ifer - получает цифру - какое число больше.
    D = Natural("")
    #D - Число на выход (результат).
    a.A.reverse()
    b.A.reverse()
    #Переворачиваем числа для удобной работы.
    if Ifer == 2:
        #Если 1-ое число больше второго.
        c = [0] * a.n
        #Массив цифр длинной 1-ого числа (для записи разности).
        last = (b.n) - 1
        #Переменная last - если цифры разной длины, контролирует когда у меньшего числа заканчиваются разряды.
        for i in range(a.n):
            #Считывание и проверка каждой цифры
            k = i + 1
            #k - переменная проверки является ли следующие число 0.
            if i > last:
                #Если у меньшей цифры закончились разряды
                c[i] = a.A[i]
                #Просто переносим цифры из большего числа в массив результата.
            else:
                #Если есть еще разряды
                if a.A[i] >= b.A[i]:
                    #Если уменьшаемого цифра больше вычитаемого
                    c[i] = a.A[i] - b.A[i]
                    #В массив результата вписываем их разность

                else:
                    #Если цифра уменьшаемого меньше цифры вычитаемого
                    while a.A[k] == 0:
                        #Пока цифра следующего разряда равна 0
                        a.A[k] = 9
                        #0 заменяется на 9
                        k += 1
                        #К следующему разряду
                    a.A[k] -= 1
                    #Нашелся ненулевой разряд - уменьшаем на 1
                    c[i] = 10 + a.A[i] - b.A[i]
                    #В результат пишем уменьшаемое + 10 отнять вычитаемое
        c.reverse()
        #Перевернем массив результата
        k = 0
        j = 0
        #Занулим для дальнейшей работы
        while c[k] == 0:
            #Цикл подсчета кол-ва 0 (для того чтобы убрать запись типа 000001234)
            k += 1
        ans = [0] * (a.n - k)
        #Длина новго массива результата - длина большего числа отнять кол-во нулей
        for i in range(k, a.n):
            #Заносим в результат начиная с k-ого элемента (т.е не с нуля)
            ans[j] = c[i]
            j += 1
        D.A = ans
        D.n = a.n - k
        #Вывод результата и получение его длины
        #!!!Важно дальше идет зеркальная работа, меняется только 1-ое и 2-ое число
    elif Ifer == 1:
        c = [0] * b.n
        last = (a.n) - 1
        for i in range(b.n):
            k = i + 1
            if i > last:
                c[i] = b.A[i]
            else:
                if b.A[i] >= a.A[i]:
                    c[i] = b.A[i] - a.A[i]

                else:
                    while b.A[k] == 0:
                        b.A[k] = 9
                        k += 1
                    b.A[k] -= 1
                    c[i] = 10 + b.A[i] - a.A[i]
        c.reverse()
        k = 0
        j = 0
        while c[k] == 0:
            k += 1
        ans = [0] * (b.n - k)
        for i in range(k, b.n):
            ans[j] = c[i]
            j += 1
        D.A = ans
        D.n = b.n - k
    else:
        #Случай если цифры равны просто возвращаем 0
        D.A = [0]
        D.n = 1
    return D


def MUL_Nk_N(a, k):
    """Умножение натурального числа на 10^k. Ташимбетов Тимур"""
    c = a.A.copy()
    D = Natural("")
    for i in range(k):
        c.append(0)
    D.A = c
    D.n = len(c)
    return D


def ADD_NN_N(a1, b1):
    """Сложение натуральных чисел. Виноградов Андрей"""
    a = Natural(str(a1))
    b = Natural(str(b1))
    #a, b - переменные - копии, чтобы не менялись изначальные данные.
    if COM_NN_D(a, b) != 2:
        #Меняем местами переменные если 2-ое число больше или равно 1-ому
        tmp = b
        b = a
        a = tmp
    a.A.reverse()
    b.A.reverse()
    #Переворачиваем числа для удобной работы
    for i in range(a.n - b.n):
        #Заполняем нулями разряды у меньшего числа< начиная с конца его длины.
        b.A.append(0)
    for i in range(a.n):
        e = a.A[i]
        f = b.A[i]
        #e, f - переменные принимающие цифры числа.
        a.A[i] = (e + f) % 10
        #Сумма чисел
        if (e + f) >= 10:
            #Если сумма больше 10
            if i == a.n - 1:
                #Если это последний разряд
                a.A.append(1)
                b.A.append(0)
                #Дописываем единицу
            b.A[i + 1] += 1
    a.A.reverse()
    #Перевочариваем число
    ans = ""
    #для записи ответа
    for x in a.A:
        ans += str(x)
        #ans получает число.
    return Natural(ans)


def NZER_N_B(a):
    """Проверка на ноль: если число не равно нулю, то 'да' иначе 'нет'. Айрапетов Давид"""
    if a.A[0] == 0 and a.n == 1:
        return False
    else:
        return True


def ADD_1N_N(a1):
    """Добавление 1 к натуральному числу. Айрапетов Давид"""
    a = Natural(str(a1))
    i = 0
    a.A.reverse()
    while a.A[i] == 9 and i + 1 < a.n:
        a.A[i] = 0
        i += 1
    if i == a.n:
        a.A.append(1)
        a.n += 1
    else:
        a.A[i] = a.A[i] + 1
    a.A.reverse()
    return a


def MUL_NN_N(a1, b1):
    """Умножение натуральных чисел. Таланков Влад"""
    a = Natural(str(a1))
    b = Natural(str(b1))
    if str(a) != '0' and str(b) != '0':
        a.A.reverse()
        res = Natural('0')  # Переменная хранящая результат умножения
        tens = 0
        for j in range(a.n):
            # Каждую ЦИФРУ числа a умножаем на ЧИСЛО b (начинаем с последней цифры числа
            if a.A[j] == 0:
                tens += 1  # Итерация прошла, однако цифра равна нулю
            else:
                multiplier = a.A[j]
                b_copy = Natural(str(b))
                temp1 = MUL_ND_N(b_copy, multiplier)  # Произведение цифры на число
                temp2 = MUL_Nk_N(temp1, tens)
                # Каждое произведение умножается на 10 в степени кол-во итераций до этого (переменная tens)

                res = ADD_NN_N(temp2, res)  # Добавление умножения в общий результат
                tens += 1  # Кол-во умножений (итераций)
        a.A.reverse()
        return res
    else:
        return Natural('0')


def SUB_NDN_N(a1, D, b1):
    """Вычитание из натурального другого натурального, умноженного на цифру для случая с неотрицательным результатом. Айрапетов Давид"""
    a = Natural(str(a1))
    b = Natural(str(b1))
    com = COM_NN_D(a, b)
    if com == 2 or com == 0:
        b = MUL_ND_N(b, D)
        d = SUB_NN_N(a, b)
    elif com == 1:
        a = MUL_ND_N(a, D)
        d = SUB_NN_N(a, b)
    return d


def MOD_NN_N(a1, b1):
    """Остаток от деления большего натурального числа на меньшее или равное натуральное с остатком(делитель отличен от нуля). Виноградов Андрей"""
    a = Natural(str(a1))
    b = Natural(str(b1))
    D = Natural('0')
    Ifer = COM_NN_D(a, b)
    # Функция ищет остаток при помощи вычитания делимого на делитель умноженного на частное
    if Ifer == 2:
        Div = DIV_NN_N(a, b)
        Del = MUL_NN_N(Div, b)
        D = SUB_NN_N(Del, a)
    if Ifer == 1:
        Div = DIV_NN_N(b, a)
        Del = MUL_NN_N(Div, a)
        D = SUB_NN_N(Del, b)
    return D


def GCF_NN_N(a1, b1):
    """НОД натуральных чисел. Алгоритм Евклида делением. Багмутов Всеволод"""
    a = Natural(str(a1))
    b = Natural(str(b1))
    while NZER_N_B(Natural(str(a))) == True and NZER_N_B(Natural(str(b))) == True:
        if COM_NN_D(a, b) == 2:
            a = MOD_NN_N(a, b)
        else:
            b = MOD_NN_N(a, b)
    return ADD_NN_N(a, b)


def LCM_NN_N(a1, b1):
    """НОК натуральных чисел. Багмутов Всеволод"""
    a = Natural(str(a1))
    b = Natural(str(b1))
    if COM_NN_D(a, b) == 2:
        greatest = a
    else:
        greatest = b
    mult = MUL_NN_N(a, b)
    gcf = GCF_NN_N(a, b)
    i = Natural('0')
    while True:
        if str(MUL_NN_N(i, gcf)) == str(mult):
            break
        else:
            i = ADD_NN_N(i, greatest)
    return i


def DIV_NN_Dk(a1, b1):
    """Вычисление первой цифры деления большего натурального на меньшее, домноженное на 10^k,где k - номер позиции этой цифры. Угрюмов Михаил"""
    # В целом алгоритм описывает деление в столбик до первой цифра, а как результат выдает эту цифру умноженную на 10^k, где к это позиция этой цифры в делении!!!!!!!
    a = Natural(str(a1)) #Cоздание копии натурального
    b = Natural(str(b1)) #Cоздание копии натурального
    arr = Natural('') #Новый массив цифр натурального
    count = Natural(str(0)) #Cоздание счетчки как натурального
    k = a.n - 1 #Сохранение степени 10 для незначимых нулей при делении, k - позиция первой цифры деления
    for i in range(b.n): #Идем по длине делителя и записываем по одной цифре делимого в пустой массив натурального уменьшая при этом k
        arr.A.append(a.A[i])
        k = k - 1
    arr.n = len(arr.A) #Обновление длины массива
    if COM_NN_D(arr, b) == 1: #Если натуральное в новом массиве меньше чем делитель, то добавить еще одну цифру
        arr.A.append(a.A[b.n])
        arr.n = len(arr.A) #Обновление длины массива
    while COM_NN_D(arr, b) != 1:#Пока натуральное в новом массиве больше или равно чем делитель
        count = ADD_1N_N(count) #Счетчик увеличиваем на 1, это и будет частное
        arr = SUB_NN_N(arr, b)# А из массива вычитаем делитель, то есть реализуем деление через вычитание
    res = MUL_Nk_N(count, k) #Как результат умножаем наше частное на 10^k где К опять же номер позиции частного при делении
    return res #Возвращаем результат


def DIV_NN_N(a1, b1):
    """Частное от деления большего натурального числа на меньшее или равное натуральное с остатком. Угрюмов Михаил"""
    # В целом алгоритм описывает полное деление в столбик !!!!!!!
    a = Natural(str(a1)) #Cоздание копии натурального
    b = Natural(str(b1)) #Cоздание копии натурального
    n = Natural(str(0)) #Cоздание копии натурального от нуля
    if COM_NN_D(a, b) == 2: #Если делимое больше делителя
        temp = Natural(str(a)) #Cохранение копии делимого
        n = Natural(str(0)) #Cоздание копии натурального от нуля
        while COM_NN_D(temp, b) != 1: #Пока делимое в новом массиве больше или равно чем делитель
            temp2 = DIV_NN_Dk(temp, b) #Cохраняем первое деление - то  есть первую цифру частного уможенную на 10^k
            n = ADD_NN_N(n, temp2) #Сохраняем цифру частного и с каждым шагом цикла записываем за ней остальный цифры
            temp3 = MUL_NN_N(temp2, b) #Cохраняем деление умноженное на делитель
            temp = SUB_NN_N(temp, temp3) #Вычитаем из делимого сохраненное деление, получая при этом новую часть делителя
    elif COM_NN_D(a, b) == 0: #Если же изначальное натуральное делимое и делитель равный то просто вернуть частное от их деления то есть 1.
        n = ADD_1N_N(n)
    return n #Как результат частное от деления двух натуральных


if __name__ == '__main__':
    a = Natural('1048576')
    b = Natural('1024')
    # Если вам нужно число без цифр длиной ноль, передайте пустую строку
    c = Natural('')
    print(DIV_NN_Dk(a, b))
    print(DIV_NN_N(a, b))
