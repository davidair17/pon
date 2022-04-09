from integer import *


class Rational:
    def __init__(self, number=""):
        """Принимает строку, в которой записана дробь
           в виде a/b, выдает рациональное число. Малых Андрей."""
        number = number.strip().split('/')
        number.append('')
        self.numer = Integer(number[0])  # Числитель
        self.denom = Natural(number[1])  # Знаменатель
        if number[1] == '':
            self.denom = Natural('1')

    def __str__(self):
        """Возвращает строковое представление числа. Малых Андрей."""
        if self.denom.A == [1] or self.numer.A == [0] or not self.denom.A:
            return str(self.numer)
        return f'{self.numer}/{self.denom}'


def INT_Q_B(a1):
    """Проверка на целое. Если рациональное число является целым, то True, иначе False. Щелочкова Екатерина."""
    a = RED_Q_Q(a1)
    if a.denom.A[0] == 1 and a.denom.n == 1:
        return True
    return False


def TRANS_Q_Z(a):
    """Преобразование дробного в целое(если знаменатель равен 1). Щелочкова Екатерина."""
    if a.denom.A[0] == 1 and a.denom.n == 1:
        return a.numer


def TRANS_Z_Q(с):
    """Преобразование целого в дробное. Щелочкова Екатерина."""
    a = Rational("1/1")
    a.numer = с
    return a


def DIV_QQ_Q(a, b):
    """деление дробей. Снятков Илья"""
    b.denom = TRANS_N_Z(b.denom)
    if POZ_Z_D(b.number) == 2:
        b.number = TRANS_Z_N(b.number)
    elif POZ_Z_D(b.number) == 1:
        b.number = MUL_ZM_Z(b.number)
        b.number = TRANS_Z_N(b.number)
        a.number = MUL_ZM_Z(a.number)
    else:
        print("moron")
    a.number = MUL_ZZ_Z(a.number, b.denom)
    a.denom = MUL_NN_N(a.denom, b.number)
    return a


def MOD_ZZ_Z(a, b):
    """остаток, a - делимое, b - делитель. Снятков Илья"""
    if POZ_Z_D(b) == 0:
        print("moron")
    else:
        c = DIV_ZZ_Z(a, b)
        d = MUL_ZZ_Z(b, c)
        if (POZ_Z_D(a) == 2 and POZ_Z_D(b) == 2) or (POZ_Z_D(a) == 2 and POZ_Z_D(b) == 1):
            r = SUB_ZZ_Z(a, d)
        elif POZ_Z_D(a) == 1 and POZ_Z_D(b) == 1:
            r = MUL_ZM_Z(SUB_ZZ_Z(a, d))
    return r


def RED_Q_Q(a1):
    """Сокращение дроби.Ташимбетов Тимур"""
    Q = Rational(str(a1))
    r = Rational("")
    q1 = Q.numer
    q2 = Q.denom
    qN = ABS_Z_N(q1)
    n = GCF_NN_N(qN, q2)
    q11 = DIV_ZZ_Z(q1, TRANS_N_Z(n))
    q12 = DIV_ZZ_Z(q2, TRANS_N_Z(n))
    q12 = TRANS_Z_N(q12)
    r.numer = q11
    r.denom = q12
    return r


def ADD_QQ_Q(self, other):
    """Сложение дробей. Абдулаев Алексей"""
    a = Rational(str(self))
    b = Rational(str(other))
    lcm_den = LCM_NN_N(a, b)
    a_floor = DIV_NN_N(lcm_den, SUB_NN_N(lcm_den, MOD_NN_N(lcm_den, a.denom)))
    b_floor = DIV_NN_N(lcm_den, SUB_NN_N(lcm_den, MOD_NN_N(lcm_den, b.denom)))
    numerator = ADD_ZZ_Z(MUL_ZZ_Z(b.numer, Integer(a_floor)), MUL_ZZ_Z(b.numer, Integer(b_floor)))
    a.denom = lcm_den
    a.numer = numerator
    return a


def SUB_QQ_Q(self, other):
    """Вычитание дробей. Абдулаев Алексей"""
    a = Rational(str(self))
    b = Rational(str(other))
    lcm_den = LCM_NN_N(a, b)
    a_floor = DIV_NN_N(lcm_den, SUB_NN_N(lcm_den, MOD_NN_N(lcm_den, a.denom)))
    b_floor = DIV_NN_N(lcm_den, SUB_NN_N(lcm_den, MOD_NN_N(lcm_den, b.denom)))
    numerator = SUB_ZZ_Z(MUL_ZZ_Z(b.numer, Integer(a_floor)), MUL_ZZ_Z(b.numer, Integer(b_floor)))
    a.denom = lcm_den
    a.numer = numerator
    return a


def MUL_QQ_Q(self, other):
    """Умножение дробей. Абдулаев Алексей"""
    a = Rational(str(self))
    b = Rational(str(other))
    num1 = MUL_ZZ_Z(self.numer, other.numer)
    num2 = MUL_NN_N(self.denom, other.denom)
    a.numer = num1
    b.numer = num2
    return a


if __name__ == '__main__':
    # Создание чисел:
    a = Rational("-65/32")
    b = Rational("0/53")
    c = Rational("63/1")
    d = Integer("54")
    print(a, b, c, d)
    print(INT_Q_B(a))
    print(TRANS_Q_Z(c))
    print(TRANS_Z_Q(d))
    print(a, b, c, d)
