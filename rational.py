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


def DIV_QQ_Q(a1, b1):
    """деление дробей. Снятков Илья"""
    a = Rational(str(a1))
    b = Rational(str(b1))
    b.denom = TRANS_N_Z(b.denom)
    if POZ_Z_D(b.numer) == 2:
        b.numer = TRANS_Z_N(b.numer)
    elif POZ_Z_D(b.numer) == 1:
        b.numer = MUL_ZM_Z(b.numer)
        b.numer = TRANS_Z_N(b.numer)
        a.numer = MUL_ZM_Z(a.numer)
    else:
        print("moron")
    a.numer = MUL_ZZ_Z(a.numer, b.denom)
    a.denom = MUL_NN_N(a.denom, b.numer)
    return a


def RED_Q_Q(a1):
    """Сокращение дроби.Ташимбетов Тимур"""
    Q = Rational(str(a1))
    r = Rational("")
    q1 = Q.numer
    q2 = Q.denom
    qN = ABS_Z_N(q1)
    n = GCF_NN_N(qN, q2)
    q11 = DIV_ZZ_Z(q1, n)
    q12 = DIV_ZZ_Z(q2, n)
    r.numer = q11
    r.denom = q12
    return r


def ADD_QQ_Q(a1, b1):
    """Сложение дробей. Абдулаев Алексей"""
    a = Rational(str(a1))
    b = Rational(str(b1))
    LCdenom = LCM_NN_N(a.denom, b.denom)  # Общий знаменатель

    # Числители чисел после приведение к общему знаменателю
    new_a = MUL_ZZ_Z(TRANS_N_Z(DIV_NN_N(LCdenom, a.denom)), a.numer)
    new_b = MUL_ZZ_Z(TRANS_N_Z(DIV_NN_N(LCdenom, b.denom)), b.numer)

    a.numer = ADD_ZZ_Z(new_a, new_b)
    a.denom = LCdenom
    return a


def SUB_QQ_Q(a1, b1):
    """Вычитание дробей. Абдулаев Алексей"""
    a = Rational(str(a1))
    b = Rational(str(b1))
    LCdenom = LCM_NN_N(a.denom, b.denom)  # Общий знаменатель

    # Числители чисел после приведение к общему знаменателю
    new_a = MUL_ZZ_Z(TRANS_N_Z(DIV_NN_N(LCdenom, a.denom)), a.numer)
    new_b = MUL_ZZ_Z(TRANS_N_Z(DIV_NN_N(LCdenom, b.denom)), b.numer)

    a.numer = SUB_ZZ_Z(new_a, new_b)
    a.denom = LCdenom
    return a


def MUL_QQ_Q(a1, b1):
    """Умножение дробей. Абдулаев Алексей"""
    a = Rational(str(a1))
    b = Rational(str(b1))
    num1 = MUL_ZZ_Z(a.numer, b.numer)
    num2 = MUL_NN_N(a.denom, b.denom)
    a.numer = num1
    a.denom = num2
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
