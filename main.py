from naturals import *
from integer import *
from rational import *
from polynome import *
from tkinter import *
from idlelib.tooltip import Hovertip


class Main(Frame):
    modes = [('Натуральные', 'Natural'), ('Целые', 'Integer'), ('Рациональные', 'Rational'), ('Многочлены', 'Polynome')]
    mode_buttons = []
    enter_button = []
    instruction = []
    argument = 0
    entry = []
    var = 0
    all_buttons = []
    buttons = {
        'Natural': [
            ('COM_NN_D', 'Сравнение натуральных чисел: 2 - если первое больше второго, 0, если равно, 1 иначе.'),
            ('NZER_N_B', 'Проверка на ноль: если число не равно нулю, то «да» иначе «нет»'),
            ('ADD_1N_N', 'Добавление 1 к натуральному числу'),
            ('ADD_NN_N', 'Сложение натуральных чисел'),
            ('SUB_NN_N', 'Вычитание из первого большего натурального числа второго меньшего или равного'),
            ('MUL_ND_N', 'Умножение натурального числа на цифру'), ('MUL_Nk_N', 'Умножение натурального числа на 10^k'),
            ('MUL_NN_N', 'Умножение натуральных чисел'),
            ('SUB_NDN_N', 'Вычитание из натурального другого натурального, умноженного на цифру для случая с неотрицательным результатом'),
            ('DIV_NN_Dk', 'Вычисление первой цифры деления большего натурального на меньшее, домноженное на 10^k,где k - номер позиции этой цифры (номер считается с нуля)'),
            ('DIV_NN_N', 'Частное от деления большего натурального числа на меньшее или равное натуральное с остатком(делитель отличен от нуля)'),
            ('MOD_NN_N', 'Остаток от деления большего натурального числа на меньшее или равное натуральное с остатком(делитель отличен от нуля)'),
            ('GCF_NN_N', 'НОД натуральных чисел'),
            ('LCM_NN_N', 'НОК натуральных чисел')],
        'Integer': [
            ('ABS_Z_N', ' Абсолютная величина числа, результат - натуральное'),
            ('POZ_Z_D', ' Определение положительности числа (2 - положительное, 0 — равное нулю, 1 - отрицательное)'),
            ('MUL_ZM_Z', ' Умножение целого на (-1)'),
            ('TRANS_N_Z', ' Преобразование натурального в целое'),
            ('TRANS_Z_N', ' Преобразование целого неотрицательного в натуральное'),
            ('ADD_ZZ_Z', ' Сложение целых чисел'),
            ('SUB_ZZ_Z', ' Вычитание целых чисел'),
            ('MUL_ZZ_Z', ' Умножение целых чисел'),
            ('DIV_ZZ_Z', ' Частное от деления целого на целое (делитель отличен от нуля)'),
            ('MOD_ZZ_Z', ' Остаток от деления целого на целое(делитель отличен от нуля)')],
        'Rational': [
            ('RED_Q_Q', ' Сокращение дроби'),
            ('INT_Q_B', ' Проверка на целое, если рациональное число является целым, то «да», иначе «нет»'),
            ('TRANS_Z_Q', ' Преобразование целого в дробное'),
            ('TRANS_Q_Z', ' Преобразование дробного в целое (если знаменатель равен 1)'),
            ('ADD_QQ_Q', ' Сложение дробей'),
            ('SUB_QQ_Q', ' Вычитание дробей'),
            ('MUL_QQ_Q', ' Умножение дробей'),
            ('DIV_QQ_Q', ' Деление дробей (делитель отличен от нуля)')],
        'Polynome': [
            ('ADD_PP_P', ' Сложение многочленов'),
            ('SUB_PP_P', ' Вычитание многочленов'),
            ('MUL_PQ_P', ' Умножение многочлена на рациональное число'),
            ('MUL_Pxk_P', ' Умножение многочлена на x^k'),
            ('LED_P_Q', ' Старший коэффициент многочлена'),
            ('DEG_P_N', ' Степень многочлена'),
            ('FAC_P_Q', ' Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей'),
            ('MUL_PP_P', ' Умножение многочленов'),
            ('DIV_PP_P', ' Частное от деления многочлена на многочлен при делении с остатком'),
            ('MOD_PP_P', ' Остаток от деления многочлена на многочлен при делении с остатком'),
            ('GCF_PP_P', ' НОД многочленов'),
            ('DER_P_P', ' Производная многочлена'),
            ('NMR_P_P', ' Преобразование многочлена — кратные корни в простые')]}

    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build("Natural")

    def build(self, mode):
        for i in range(len(self.modes)):
            com = lambda x=self.modes[i][1]: self.create_buttons(x)
            button = Button(text=self.modes[i][0], command=com, font=("Roboto", 14), width=12)
            self.mode_buttons.append(button)
            button.grid(row=0, column=i, padx=(5, 5), pady=(5, 5))

        label = Label(text='Поле ввода', font=("Roboto", 14))
        label.grid(row=1, column=0, columnspan=3, padx=(5, 5), pady=(5, 5))
        self.instruction = label

        self.var = IntVar()
        enter = Button(text='Ввод', font=("Roboto", 14), width=12, command=lambda: self.var.set(1))
        enter.grid(row=2, column=3, padx=(5, 5), pady=(5, 5))
        self.enter_button = enter

        message = StringVar()
        entry = Entry(textvariable=message, font=("Roboto", 14), width=45)
        entry.grid(row=2, column=0, columnspan=3, padx=(5, 5), pady=(5, 5))
        self.entry = entry
        self.create_buttons(mode)
        self.mainloop()

    def create_buttons(self, operation):
        buttons = self.buttons[operation]
        for button in self.mode_buttons:
            button["state"] = "normal"
        i = 0
        while self.modes[i][1] != operation:
            i += 1
        self.mode_buttons[i]["state"] = "disable"
        for button in self.all_buttons:
            button.destroy()
        self.all_buttons = []
        for i in range(len(buttons)):
            com = lambda x=buttons[i][0]: self.calculate(x)
            button = Button(text=buttons[i][0], command=com, font=("Roboto", 14), width=12)
            button.grid(row=3 + i // 4, column=i % 4, padx=(5, 5), pady=(5, 5))

            self.all_buttons.append(button)
            Hovertip(button, buttons[i][1], hover_delay=100)

    def is_natural(self, n):
        if n.isdigit():
            if int(n) >= 0:
                return True
        return False


    def get_natural(self):
        self.instruction.config(text='Введите натуральное число')
        self.enter_button.wait_variable(self.var)
        s = self.entry.get()
        while not self.is_natural(s):
            self.instruction.config(text='Неправильный формат, попробуйте ещё раз')
            self.enter_button.wait_variable(self.var)
            s = self.entry.get()
        return Natural(s)


    def calculate(self, name):
        f = eval(name)
        for button in self.all_buttons:
            button["state"] = "disable"
        for button in self.mode_buttons:
            button["state"] = "disable"
        arguments = []
        for i in name.split('_')[1]:
            if i == 'N':
                arguments.append(self.get_natural())

        self.instruction.config(text=f(*arguments))


if __name__ == '__main__':
    root = Tk()
    root.title("Pon")
    root.resizable(False, False)
    app = Main(root)
    root.mainloop()
