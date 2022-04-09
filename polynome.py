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
            koeff = self.C[j]   # Вид коэффициента при выводе

            if koeff.numer.A == [1] and koeff.denom.A == [1] and i != 0:
                koeff = '-' if koeff.numer.b else ''

            if self.C[j].numer.A != [0]:
                res += sign(koeff) + f'{koeff}{deg(i)}'

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


def MUL_Pxk_P(a, k):
    """Умножение полинома на x^k. Угрюмов Михаил."""
    a.m = a.m + k
    for i in range(k):
        a.C.append(Rational("0/1"))
    return a


def DER_P_P(a):
    """Производная многочлена. Николаев Клим."""
    if a.m == 0:
        a.C[0] = 0
    else:
        a.m = a.m - 1
        a.C.pop(len(a.C) - 1)
        t = a.m
        for i in range(len(a.C)):
            a.C[i] = a.C[i] * Rational(str(t))
            t -= 1
    return a


def ADD_PP_P(poly1, poly2):
    """Сложение многочленов. Малых Андрей"""
    if DEG_P_N(poly1) < DEG_P_N(poly2):
        poly1, poly2 = poly2, poly1
    for i in range(DEG_P_N(poly2) + 1):
        poly1.C[i] = ADD_QQ_Q(poly1.C[i], poly2.C[i])
    poly1.frontZerosDel()
    return poly1


def SUB_PP_P(poly1, poly2):
    """Вычитание многочленов. Малых Андрей"""
    if DEG_P_N(poly1) < DEG_P_N(poly2):
        poly1, poly2 = poly2, poly1
    for i in range(DEG_P_N(poly2) + 1):
        poly1.C[i] = SUB_QQ_Q(poly1.C[i], poly2.C[i])
    poly1.frontZerosDel()
    return poly1


def MUL_PQ_P(polynome, num):
    """Умножение многочлена на число. Малых Андрей"""
    for i in range(DEG_P_N(polynome) + 1):
        polynome.C[i] = MUL_QQ_Q(polynome.C[i], num)
    polynome.frontZerosDel()
    return polynome


def FAC_P_Q(a):
    """Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей.Максимов Матвей"""
    a = [ABS_Z_N(i.numer) for i in a.C if str(i.numer) != '0']
    if len(a)<2:
        return a[0]
    elif len(a)==2:
       return (GCF_NN_N(a[0],a[1]))
    nod = GCF_NN_N(a[0], a[1]) 
    for i in range(3,len(a)):
        nod= GCF_NN_N(nod,a[i])
    b = [ABS_Z_N(j.denom) for j in b.C if str(j.denom) != '0']
    if len(b)<2:
        return b[0]
    elif len(b)==2:
       return (LCM_NN_N(b[0],b[1]))
    nok=LCM_NN_N(b[0],b[1])
    for j in range(3,len(a)):
        nok=LCM_NN_N(nok,b[i])
    q = Rational(str(Rational(str(nod)))+'/'+str(Natural(str(nok))))
    return q


if __name__ == '__main__':
    a = Polynome("-4/3x^4 + 7/5x^3-13/2x-5/4")
    b = Polynome("3/2 -13/7 -5/2")
    k = int(input())
    print(a)
    print(LED_P_Q(a))
    print(DEG_P_N(a))
    print(MUL_Pxk_P(a, k))
    print(DER_P_P(a))
