from rational import *
from copy import copy


class Polynome:
    def __init__(self, polynome="0"):
        """Принимает строку с записью многочлена от переменной x
           в каноническом виде, возвращает экземпляр класса. Малых Андрей"""

        # Разбиение многочлена на список отдельных членов
        polynome = polynome.replace('-', '+-').split('+')
        polynome = [i.replace(' ', '') for i in polynome if i]

        koeffs = []  # Список коэффициентов, записанных в строке polynome
        degs = []  # Список степеней x, записанных в строке polynome

        for i in polynome:
            f = i.split('x')
            if len(f) != 2:
                f.append(int('0'))
            elif not f[1]:
                f[1] = int('1')
            else:
                f[1] = int(f[1][1:].strip())

            if not f[0]:
                f[0] = '1'
            elif f[0] == '-':
                f[0] = '-1'

            koeffs.append(f[0])
            degs.append(f[1])

        self.m = max(degs)  # Степень многочлена
        self.C = [Rational('0')] * (self.m + 1)  # Список коэффициентов
        j = 0
        for i in range(self.m + 1, -1, -1):
            if i in degs:
                self.C[self.m - i] = Rational(koeffs[j])
                j += 1

    def __copy__(self):
        a = type(self)()
        a.C = self.C.copy()
        a.m = self.m
        return a

    def frontZerosDel(self):
        """Удаление нулевых коэффициентов перед старшим членом. Малых Андрей"""
        while self.C[0].numer.A == [0] and len(self.C) > 1:
            self.C.pop(0)
        self.m = len(self.C) - 1

    def redCoeff(self):
        """Сокращение коэффициентов многочлена. Малых Андрей"""
        self.C = [RED_Q_Q(i) for i in self.C]

    def __str__(self):
        """Возвращает строковое представление многочлена. Малых Андрей."""

        def sign(num):
            """Определяет, какой знак выводить перед членом. Малых Андрей"""
            if num:
                if num == '-':
                    return ''
                else:
                    return '' if num.numer.b else '+'
            return '+'

        def deg(i):
            """Принимает степень икса, возвращает строковое представление x^i. Малых Андрей"""
            if i > 1:
                return f'x^{i}'
            elif i == 1:
                return 'x'
            return ''

        res = ''

        for i in range(self.m, -1, -1):
            j = self.m - i  # Номер коэффициента
            coeff = self.C[j]  # Вид коэффициента при выводе

            if coeff.numer.A == [1] and coeff.denom.A == [1] and i != 0:
                coeff = '-' if coeff.numer.b else ''

            if self.C[j].numer.A != [0]:
                res += sign(coeff) + f'{coeff}{deg(i)}'

        if not res:
            return '0'
        elif res[0] == '+':
            res = res[1:]
        return res


def LED_P_Q(polynome):
    """Старший коэффициент многочлена. Таланков Влад."""
    return polynome.C[0]


def DEG_P_N(polynome):
    """Степень многочлена. Таланков Влад."""
    return polynome.m


def MUL_Pxk_P(poly, k):
    """Умножение полинома на x^k. Угрюмов Михаил."""
    poly1 = copy(poly) #Cоздание копии полинома
    poly1.m = poly1.m + k #Максимальную степень полинома увеличиваем на k
    for i in range(k):
        poly1.C.append(Rational("0/1")) #Добавляем незначимые коэффициенты перед степенями х которых после умножения уже нет ((2x^2 + x) * x^2 = 2x^4 + x^3 + 0/1x^2 + 0/1x^1 + 0/1x^0)
    return poly1 # возвращаем массив коэффициентов нового многочлена


def DER_P_P(poly2):
    """Производная многочлена. Николаев Клим."""
    # на вход поступает многочлен - массив его коэффициентов
    polynome = copy(poly2)
    # если степень многочлена 0(то есть максимальная степень равна 0 - например 5*x^0)
    if polynome.m == 0:
        # Возвращаем многочлен с единственым элементом 0
        polynome.C[0] = 0
    # если степень многочлена больше 0
    elif polynome.m > 0:
        # уменьшаем степен многочлена на единицу
        polynome.m = polynome.m - 1
        # уменьшаем массив коэффициентов на единицу
        polynome.C.pop(len(polynome.C) - 1)
        # t - показатель степени при старшем члене
        t = polynome.m + 1
        # идем по всем коэффициентам многочлена
        for i in range(len(polynome.C)):
            # умножаем коэффициент на показатель степени
            polynome.C[i] = MUL_QQ_Q(polynome.C[i], Rational(str(t)))
            # уменьшаем показатель степени на 1
            t -= 1
    # возвращаем массив коэффициентов производной исходного многочлена
    return polynome


def ADD_PP_P(p1, p2):
    """Сложение многочленов. Малых Андрей"""
    poly1 = copy(p1)
    poly2 = copy(p2)

    # Многочлен poly1 должен иметь степень >= степени poly2
    # Если степень poly2 > степени poly1, то меняем их местами
    if DEG_P_N(poly1) < DEG_P_N(poly2):
        poly1, poly2 = poly2, poly1

    # Находим разницу между степенями многочленов
    deg_delta = DEG_P_N(poly1) - DEG_P_N(poly2)

    # Вычитаем из коэффициентов poly1 коэффициенты poly2 при тех же степенях
    for i in range(DEG_P_N(poly2) + 1):
        poly1.C[i + deg_delta] = ADD_QQ_Q(poly1.C[i + deg_delta], poly2.C[i])

    # Удаляем нулевые коэффициенты, стоящие перед старшим коэффициентом
    poly1.frontZerosDel()

    # Сокращаем коэффициенты
    poly1.redCoeff()
    return poly1


def SUB_PP_P(p1, p2):
    """Вычитание многочленов. Малых Андрей"""
    poly1 = copy(p1)
    poly2 = copy(p2)

    # Многочлен poly1 должен иметь степень >= степени poly2
    # Если степень poly2 > степени poly1, то меняем их
    # местами и умножаем на -1 для правильного результата вычитания
    if DEG_P_N(poly1) < DEG_P_N(poly2):
        poly1, poly2 = poly2, poly1
        poly1 = MUL_PQ_P(poly1, "-1")
        poly2 = MUL_PQ_P(poly2, "-1")

    # Находим разницу между степенями многочленов
    deg_delta = DEG_P_N(poly1) - DEG_P_N(poly2)

    # Вычитаем из коэффициентов poly1 коэффициенты при тех же степенях poly2
    for i in range(DEG_P_N(poly2) + 1):
        poly1.C[i + deg_delta] = SUB_QQ_Q(poly1.C[i + deg_delta], poly2.C[i])

    # Удаляем нулевые коэффициенты, стоящие перед старшим коэффициентом
    poly1.frontZerosDel()

    # Сокращаем коэффициенты
    poly1.redCoeff()
    return poly1


def MUL_PQ_P(polynome1, num1):
    """Умножение многочлена на число. Малых Андрей"""
    polynome = copy(polynome1)
    num = Rational(str(num1))

    # Умножаем все коэффициенты на заданное число
    for i in range(DEG_P_N(polynome) + 1):
        polynome.C[i] = MUL_QQ_Q(polynome.C[i], num)

    # Удаляем нулевые коэффициенты, стоящие перед старшим коэффициентом
    polynome.frontZerosDel()
    return polynome


def FAC_P_Q(a):
    """Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей. Максимов Матвей"""
    pol = a
    a = [ABS_Z_N(i.numer) for i in pol.C if str(i.numer) != '0']
    if len(a) < 2:
        return a[0]
    elif len(a) == 2:
        return (GCF_NN_N(a[0], a[1]))
    nod = GCF_NN_N(a[0], a[1])
    for i in range(2, len(a)):
        nod = GCF_NN_N(nod, a[i])
    b = [ABS_Z_N(j.denom) for j in pol.C if str(j.denom) != '0']
    if len(b) < 2:
        return b[0]
    elif len(b) == 2:
        return (LCM_NN_N(b[0], b[1]))
    nok = LCM_NN_N(b[0], b[1])
    for i in range(2, len(a)):
        nok = LCM_NN_N(nok, b[i])
    q = Rational(str(Rational(str(nod))) + '/' + str(Natural(str(nok))))
    return q


def GCF_PP_P(a, b):
    """Нод многочленов. Снятков Илья"""
    a1 = copy(a)
    b1 = copy(b)
    while DEG_P_N(b1) != 0:
        temp = b1
        b1 = MOD_PP_P(a1, b1)
        a1 = temp
    return a1


def NMR_P_P(poly1):
    """Преобразование многочлена — кратные корни в простые.Николаев Клим"""
    # На вход поступает многочлен
    # берем производную исходного многочлена
    temp = DER_P_P(poly1)
    # находим НОД исходного многочлена и его производной
    gcf = GCF_PP_P(poly1, temp)
    # находим НОК знаменателей коэффициентов и НОД числителей
    fac = FAC_P_Q(gcf)
    # делим исходный многочлен на значение НОД(gcf)
    res = DIV_PP_P(poly1, gcf)
    # умножаем res на fac
    res = MUL_PQ_P(res, fac)
    # возвращаем результат
    return res


def MUL_PP_P(poly1, poly2):
    """Умножение полинома на полином. Глушков Арсений"""
    n = DEG_P_N(poly1) + 1
    m = DEG_P_N(poly2) + 1
    if n < m:
        poly1, poly2 = poly2, poly1
        n, m = m, n

    # Формирование нового полинома
    res_poly = Polynome('0')
    res_poly = MUL_Pxk_P(res_poly, n + m - 2)

    # Заполнение нового полинома
    for k in range(m):
        for i in range(k + 1):
            res_poly.C[k] = ADD_QQ_Q(
                res_poly.C[k], MUL_QQ_Q(poly1.C[i], poly2.C[k - i]))
    for k in range(m, n):
        for i in range(k - m + 1, k + 1):
            res_poly.C[k] = ADD_QQ_Q(
                res_poly.C[k], MUL_QQ_Q(poly1.C[i], poly2.C[k - i]))
    for k in range(n, m + n):
        for i in range(k - m + 1, n):
            res_poly.C[k] = ADD_QQ_Q(
                res_poly.C[k], MUL_QQ_Q(poly1.C[i], poly2.C[k - i]))

    return res_poly


def DIV_PP_P(poly1, poly2):
    """Частное от деления полинома на полином. Глушков Арсений"""
    r = copy(poly1)
    n = DEG_P_N(poly1)
    m = DEG_P_N(poly2)
    if n < m:
        q = Polynome("1")
    else:
        q = Polynome("0")
        q = MUL_Pxk_P(q, n - m)
        cde = LED_P_Q(poly2)
        for i in range(DEG_P_N(poly1) - DEG_P_N(poly2) + 1):
            temp = DIV_QQ_Q(LED_P_Q(r), cde)
            q.C[i] = temp
            divider = copy(poly2)
            r = SUB_PP_P(r, MUL_PQ_P(MUL_Pxk_P(divider, n - m - i), temp))
    return q


def MOD_PP_P(poly1, divider):
    """Остаток от деления полинома на полином. Глушков Арсений"""

    if DEG_P_N(poly1) >= DEG_P_N(divider):
        sf = copy(poly1)
        res_poly = SUB_PP_P(sf, MUL_PP_P(DIV_PP_P(poly1, divider), divider))
    else:
        res_poly = Polynome(str(poly1))
    return res_poly


if __name__ == '__main__':
    a = Polynome("9x^4 + 15x^3-12x^2-8x + 1")
    b = Polynome("3x^2 -13x -5")
    # k = int(input())
    print(a)
    print(b)
    print(MUL_PP_P(a, b))
    print(DIV_PP_P(a, b))
    print(MOD_PP_P(a, b))
