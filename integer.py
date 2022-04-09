from naturals import *


class Integer:
    def __init__(self, number=""):
        """Принимает строку, выдает целое число. Малых Андрей"""
        self.b = 0
        if len(number) > 0:
            if number[0] == '-':
                self.b = 1
                number = number[1:]
        self.A = [int(i) for i in number]
        self.n = len(number)

    def __str__(self):
        """Возвращает строковое представление числа. Малых Андрей"""
        return ('-' if self.b else '') + "".join(map(str, self.A))


def ABS_Z_N(z):
    """Возвращает абсолютное значение числа(модуль). Максимов Матвей"""
    nat = Natural("")
    nat.A = z.A
    return nat


def MUL_ZM_Z(z_in):
    """Возвращает число с противоположным знаком(т.е умноженное на (-1). Максимов Матвей"""
    z = Integer(str(z_in))
    if z.b == 1:
        z.b = 0
    else:
        z.b = 1
    return z


def TRANS_N_Z(nat):
    """Преобразует натуральное число в целое. Максимов Матвей"""
    z = Integer("")
    z.b = 0
    z.A = nat.A
    z.n = nat.n
    return z


def TRANS_Z_N(z):
    """Преобразует целое число в натуральное. Максимов Матвей"""
    nat = Natural("")
    nat.b = 0
    nat.A = z.A
    nat.n = z.n
    return nat


def POZ_Z_D(z):
    """Определение положительности числа (2 - положительное, 0 — равное нулю, 1 - отрицательное) Багмутов Всеволод"""
    if z.A[0] == 0 and z.n == 1:
        return 0
    elif z.b == 0:
        return 2
    elif z.b == 1:
        return 1


def DIV_ZZ_Z(a1, b1):
    """Частное от деления целого на целое (делитель отличен от нуля).Ташимбетов Тимур"""
    a = Natural(str(a1))
    b = Natural(str(b1))
    if (POZ_Z_D(a) == 2) and (POZ_Z_D(b) == 2):  # если оба числа положительные
        if a > b:
            c = DIV_NN_N(a, b)
        if a < b:
            c = 0
        if a == b:
            c = 1
    if (POZ_Z_D(a) == 2) and (POZ_Z_D(b) == 1):  # если первое число положительное, а второе отрицательное
        am = ABS_Z_N(a)
        bm = ABS_Z_N(b)
        if am < bm:
            c = 0
        if am == bm:
            c = 1
        if am > bm:
            cp = DIV_NN_N(a, b)
            if MUL_ZZ_Z(cp, bm) == am:
                c = cp
            c = MUL_ZZ_Z(c, -1)
    if (POZ_Z_D(a) == 1) and (POZ_Z_D(b) == 2):  # если первое отрицательное, а второе положительное
        am = ABS_Z_N(a)
        bm = ABS_Z_N(b)
        if am < bm:
            c = 0
        if am == bm:
            c = 1
        if am > bm:
            cp = DIV_NN_N(a, b)
            if MUL_ZZ_Z(cp, bm) == am:
                c = cp
            c = ADD_1N_N(c)
            c = MUL_ZZ_Z(c, -1)
    if (POZ_Z_D(a) == 1) and (POZ_Z_D(b) == 1):  # если оба числа отрицательные
        am = ABS_Z_N(a)
        bm = ABS_Z_N(b)
        if am < bm:
            c = 0
        if am == bm:
            c = 1
        if am > bm:
            cp = DIV_NN_N(a, b)
            if MUL_ZZ_Z(cp, bm) == am:
                c = cp
            c = ADD_1N_N(c)
    if (POZ_Z_D(a) == 0) and (POZ_Z_D(b) == 1) or (POZ_Z_D(b) == 2):  # если первое число 0
        c = 0
    return c


def ADD_ZZ_Z(a, b):
    """Сложение целых чисел. Дитятьев Иван"""

    if COM_NN_D(Natural(str(ABS_Z_N(a))), Natural(str(ABS_Z_N(b)))) == 2:

        x = a
        y = b
    else:
        x = b
        y = a

    if x.b == 0 and y.b == 0:
        return Integer(str(ADD_NN_N(Natural(str(x)), Natural(str(y)))))
    elif x.b == 1 and y.b == 1:
        return MUL_ZM_Z(Integer(str(ADD_NN_N(Natural(str(x)[1:]), Natural(str(y)[1:])))))
    else:
        if x.b == 0:
            return Integer(str(SUB_NN_N(Natural(str(x)), Natural(str(y)[1:]))))
        else:
            return MUL_ZM_Z(Integer(str(SUB_NN_N(Natural(str(x)[1:]), Natural(str(y))))))


def SUB_ZZ_Z(a, b):
    """Разность целых чисел(a - b). Дитятьев Иван"""
    if COM_NN_D(Natural(str(ABS_Z_N(a))), Natural(str(ABS_Z_N(b)))) == 2:
        x = a
        y = b
        o = 1
    else:
        x = b
        y = a
        o = 0

    if x.b == 1 and y.b == 1:
        if o:
            return MUL_ZM_Z(Integer(str(SUB_NN_N(Natural(str(x)[1:]), Natural(str(y)[1:])))))
        else:
            return Integer(str(SUB_NN_N(Natural(str(x)[1:]), Natural(str(y)[1:]))))

    elif x.b == 0 and y.b == 0:
        if str(x) == str(y):
            return Integer('0')
        if o:
            return Integer(str(SUB_NN_N(Natural(str(x)), Natural(str(y)))))
        else:
            return MUL_ZM_Z(Integer(str(SUB_NN_N(Natural(str(x)), Natural(str(y))))))
    elif x.b == 0:
        if o:
            return Integer(str(ADD_NN_N(Natural(str(x)), Natural(str(y)[1:]))))
        else:
            return MUL_ZM_Z(Integer(str(ADD_NN_N(Natural(str(x)), Natural(str(y)[1:])))))
    else:
        if o:
            return MUL_ZM_Z(Integer(str(ADD_NN_N(Natural(str(x)[1:]), Natural(str(y))))))
        else:
            return Integer(str(ADD_NN_N(Natural(str(x)[1:]), Natural(str(y)))))


def MUL_ZZ_Z(a, b):
    """Произведение целых чисел. Дитятьев Иван"""
    x = a
    y = b
    if (a.b and b.b) or (not a.b and not b.b):
        return Integer(str(MUL_NN_N(Natural(str(ABS_Z_N(x))), Natural(str(ABS_Z_N(y))))))
    else:
        return MUL_ZM_Z(Integer(str(MUL_NN_N(Natural(str(ABS_Z_N(x))), Natural(str(ABS_Z_N(y)))))))


def MOD_ZZ_Z(a, b):
    """остаток, a - делимое, b - делитель. Снятков Илья"""
    if POZ_Z_D(b) == 0:
        print("moron")
    else:
        c = DIV_ZZ_Z(a, b)
        d = MUL_ZZ_Z(b, c)
        if (POZ_Z_D(a) == 2 and POZ_Z_D(b) == 2) or (POZ_Z_D(a) == 2 and POZ_Z_D(b) == 1):
            r = SUB_ZZ_Z(a, d)
        elif (POZ_Z_D(a) == 1 and POZ_Z_D(b) == 1) or (POZ_Z_D(a) == 1 and POZ_Z_D(b) == 2):
            r = MUL_ZM_Z(SUB_ZZ_Z(a, d))
    return r


if __name__ == '__main__':
    z = Integer("-4")
    nat = Natural("6")
    print(z, nat)
    print(z)
    print(POZ_Z_D(z))
    print(ABS_Z_N(z))
    print(MUL_ZM_Z(z))
    print(TRANS_N_Z(nat))
    print(str(TRANS_N_Z(z)))
    print(z, nat)
