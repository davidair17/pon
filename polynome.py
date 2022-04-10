from rational import *


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
    poly1 = Polynome(str(poly))
    poly1.m = poly1.m + k
    for i in range(k):
        poly1.C.append(Rational("0/1"))
    return poly1


def DER_P_P(poly1):
    """Производная многочлена. Николаев Клим."""
    if poly1.m == 0:
        poly1.C[0] = 0
    elif poly1.m > 0:
        poly1.m = poly1.m - 1
        poly1.C.pop(len(poly1.C) - 1)
        t = poly1.m + 1
        for i in range(len(poly1.C)):
            poly1.C[i] = MUL_QQ_Q(poly1.C[i], Rational(str(t)))
            t -= 1
    return poly1


def ADD_PP_P(p1, p2):
    """Сложение многочленов. Малых Андрей"""
    poly1 = Polynome(str(p1))
    poly2 = Polynome(str(p2))

    if DEG_P_N(poly1) < DEG_P_N(poly2):
        poly1, poly2 = poly2, poly1

    deg_delta = DEG_P_N(poly1) - DEG_P_N(poly2)
    for i in range(DEG_P_N(poly2) + 1):
        poly1.C[i + deg_delta] = ADD_QQ_Q(poly1.C[i + deg_delta], poly2.C[i])
    poly1.frontZerosDel()
    poly1.redCoeff()
    return poly1


def SUB_PP_P(p1, p2):
    """Вычитание многочленов. Малых Андрей"""
    poly1 = Polynome(str(p1))
    poly2 = Polynome(str(p2))

    if DEG_P_N(poly1) < DEG_P_N(poly2):
        poly1, poly2 = poly2, poly1
        poly1 = MUL_PQ_P(poly1, "-1")
        poly2 = MUL_PQ_P(poly2, "-1")

    deg_delta = DEG_P_N(poly1) - DEG_P_N(poly2)
    for i in range(DEG_P_N(poly2) + 1):
        poly1.C[i + deg_delta] = SUB_QQ_Q(poly1.C[i + deg_delta], poly2.C[i])
    poly1.frontZerosDel()
    poly1.redCoeff()
    return poly1


def MUL_PQ_P(polynome1, num1):
    """Умножение многочлена на число. Малых Андрей"""
    polynome = Polynome(str(polynome1))
    num = Rational(str(num1))
    for i in range(DEG_P_N(polynome) + 1):
        polynome.C[i] = MUL_QQ_Q(polynome.C[i], num)
    polynome.frontZerosDel()
    return polynome


def FAC_P_Q(a):
    """Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей.Максимов Матвей"""
    a = [ABS_Z_N(i.numer) for i in a.C if str(i.numer) != '0']
    if len(a) < 2:
        return a[0]
    elif len(a) == 2:
        return GCF_NN_N(a[0], a[1])
    nod = GCF_NN_N(a[0], a[1])
    for i in range(3, len(a)):
        nod = GCF_NN_N(nod, a[i])
    b = [ABS_Z_N(j.denom) for j in a.C if str(j.denom) != '0']
    if len(b) < 2:
        return b[0]
    elif len(b) == 2:
        return LCM_NN_N(b[0], b[1])
    nok = LCM_NN_N(b[0], b[1])
    for j in range(3, len(a)):
        nok = LCM_NN_N(nok, b[i])
    q = Rational(str(Rational(str(nod))) + '/' + str(Natural(str(nok))))
    return q


def GCF_PP_P(a, b):
    """Нод многочленов. Снятков Илья"""
    a1 = Polynome(str(a))
    b1 = Polynome(str(b))
    while DEG_P_N(b1) != 0:
        temp = b1
        b1 = MOD_PP_P(a1, b1)
        a1 = temp
    return a1


def NMR_P_P(poly1):
    """Преобразование многочлена — кратные корни в простые.Николаев Клим"""
    # Производная многочлена
    temp = DER_P_P(poly1)
    # НОД многочлена и его производной
    gcf = GCF_PP_P(poly1, temp)
    fac = FAC_P_Q(gcf)
    # Делим многочлен на значеие НОД и возвращаем результат
    res = DIV_PP_P(poly1, gcf)
    res = MUL_PQ_P(res, fac)
    return Polynome(res)


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
    r = Polynome(str(poly1))
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
            divider = Polynome(str(poly2))
            r = SUB_PP_P(r, MUL_PQ_P(MUL_Pxk_P(divider, n - m - i), temp))
    return q


def MOD_PP_P(poly1, divider):
    """Остаток от деления полинома на полином. Глушков Арсений"""

    if DEG_P_N(poly1) >= DEG_P_N(divider):
        sf = Polynome(str(poly1))
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
