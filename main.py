import re
from naturals import *
from integer import *
from rational import *
from polynome import *
from tkinter import *
from idlelib.tooltip import Hovertip
from buttons import buttons


class Main(Frame):
    modes = [('Натуральные', 'Natural'), ('Целые', 'Integer'),
             ('Рациональные', 'Rational'), ('Многочлены', 'Polynome')]
    mode_buttons = []
    enter_button = []
    instruction = []
    argument = 0
    entry = []
    var = 0
    all_buttons = []
    buttons = buttons

    def __init__(self, root):
        """Инициализация приложения. Смирнов Иван"""
        super(Main, self).__init__(root)
        self.build("Natural")

    def build(self, mode):
        """Заполнение окна. Смирнов Иван"""
        for i in range(len(self.modes)):
            com = lambda x=self.modes[i][1]: self.create_buttons(x)
            button = Button(text=self.modes[i][0], command=com, font=(
                "Roboto", 14), width=12)
            self.mode_buttons.append(button)
            button.grid(row=0, column=i, padx=(5, 5), pady=(5, 5))

        label = Label(text='Поле ввода', font=("Roboto", 14))
        label.grid(row=1, column=0, columnspan=4, padx=(5, 5), pady=(5, 5))
        self.instruction = label

        self.var = IntVar()
        enter = Button(text='Ввод', font=("Roboto", 14), width=12, command=lambda: self.var.set(1))
        enter.grid(row=2, column=3, padx=(5, 5), pady=(5, 5))
        self.enter_button = enter
        self.enter_button["state"] = 'disable'

        message = StringVar()
        entry = Entry(textvariable=message, font=("Roboto", 14), width=45)
        entry.grid(row=2, column=0, columnspan=3, padx=(5, 5), pady=(5, 5))
        self.entry = entry
        self.create_buttons(mode)
        label = Label(text='Чтобы узнать, что делает функция, наведите курсор мыши на неё.\n'
                           'Примеры ввода чисел:\n'
                           'Натуральные: 0; 13; 230032; 12; 23; 7645\n'
                           'Целые: 34; 364; 8231; -3423; -938; -38; 81\n'
                           'Рациональные: 3/4; -3/8; -1; 13; 0; -12/21\n'
                           'Полиномы: 3/4x^5-3423x; 9x^3+x^2-4/10', font=("Roboto", 12), justify="left")
        label.grid(row=7, column=0, columnspan=4, padx=(5, 5), pady=(5, 5))
        self.mainloop()

    def create_buttons(self, operation):
        """Создание набора кнопок для вызова группы функций. Смирнов Иван"""
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
            button = Button(text=buttons[i][0], command=com, font=(
                "Roboto", 14), width=12)
            button.grid(row=3 + i // 4, column=i % 4, padx=(5, 5), pady=(5, 5))

            self.all_buttons.append(button)
            Hovertip(button, buttons[i][1], hover_delay=100)

    def is_natural(self, n):
        """Проверка строки на натуральное. Смирнов Иван"""
        if n.isdigit():
            if int(n) >= 0:
                return True
        return False

    def get_natural(self):
        """Ввод натурального. Смирнов Иван"""
        self.instruction.config(text='Введите натуральное число или ноль')
        self.enter_button.wait_variable(self.var)
        s = self.entry.get()
        while not self.is_natural(s):
            self.instruction.config(
                text='Неправильный формат, попробуйте ещё раз')
            self.enter_button.wait_variable(self.var)
            s = self.entry.get()
        return Natural(s)

    def is_integer(self, n):
        """Проверка строки на целое. Смирнов Иван"""
        return n.isdigit() or n[1:].isdigit and n[0] == '-'

    def get_integer(self):
        """Ввод целого. Смирнов Иван"""
        self.instruction.config(text='Введите целое число')
        self.enter_button.wait_variable(self.var)
        s = self.entry.get()
        while not self.is_integer(s):
            self.instruction.config(
                text='Неправильный формат, попробуйте ещё раз')
            self.enter_button.wait_variable(self.var)
            s = self.entry.get()
        return Integer(s)

    def is_rational(self, n):
        """Проверка строки на рациональное. Смирнов Иван"""
        if '/' in n:
            return self.is_integer(n.split('/')[0]) and self.is_natural(n.split('/')[1]) and n.split('/')[1] != '0'
        return self.is_integer(n)

    def get_rational(self):
        """Ввод рационального. Смирнов Иван"""
        self.instruction.config(text='Введите рациональное число (дробь)')
        self.enter_button.wait_variable(self.var)
        s = self.entry.get()
        while not self.is_rational(s):
            self.instruction.config(
                text='Неправильный формат, попробуйте ещё раз')
            self.enter_button.wait_variable(self.var)
            s = self.entry.get()
        return Rational(s)

    def is_polynome(self, n):
        """Проверка на полином. Малых Андрей"""
        if not re.search(r'\w+\s+\w+', n):
            n = n.replace(' ', '')
            n = n.replace('-', '+-').split('+')
            n = [i for i in n if i]
            pattern = re.compile(
                r'^-?(((\d*|(\d+/[1-9]+))((x\^\d+$)|(x$)))|(((\d+)|(\d+/[1-9]+))$))')
            if n:
                degs = []
                for i in n:
                    res = re.fullmatch(pattern, i)
                    if not (res and n):
                        return False
                    f = i.split('x')
                    if len(f) != 2:
                        f.append(0)
                    elif not f[1]:
                        f[1] = 1
                    else:
                        f[1] = int(f[1][1:].strip())
                    degs.append(f[1])

                # Проверка, что степени в строгом монотонно убывающем порядке
                for i in range(len(degs) - 1):
                    if degs[i] <= degs[i + 1]:
                        return False
                return True
        return False

    def get_polynome(self):
        """Ввод полинома. Смирнов Иван"""
        self.instruction.config(text='Введите полином')
        self.enter_button.wait_variable(self.var)
        s = self.entry.get()
        while not self.is_polynome(s):
            self.instruction.config(
                text='Неправильный формат, попробуйте ещё раз')
            self.enter_button.wait_variable(self.var)
            s = self.entry.get()
        return Polynome(s)

    def is_digital(self, n):
        """Проверка на цифру. Смирнов Иван"""
        return len(n) == 1 and n.isdigit()

    def get_digital(self):
        """Ввод цифры. Смирнов Иван"""
        self.instruction.config(text='Введите цифру')
        self.enter_button.wait_variable(self.var)
        s = self.entry.get()
        while not self.is_digital(s):
            self.instruction.config(text='Неправильный формат, попробуйте ещё раз')
            self.enter_button.wait_variable(self.var)
            s = self.entry.get()
        return int(s)

    def calculate(self, name):
        """Вычисление результат выбранной функции. Смирнов Иван"""
        f = eval(name)
        for button in self.all_buttons:
            button["state"] = "disable"
        for button in self.mode_buttons:
            button["state"] = "disable"
        self.enter_button["state"] = 'normal'
        arguments = []
        for i in name.split('_')[1]:
            if i == 'N':
                arguments.append(self.get_natural())
            elif i == 'Z':
                arguments.append(self.get_integer())
            elif i == 'Q':
                arguments.append(self.get_rational())
            elif i == 'P':
                arguments.append(self.get_polynome())
            elif i == 'D':
                arguments.append(self.get_digital())
            elif i == 'k':
                arguments.append(int(str(self.get_natural())))
            self.entry.delete(0, END)
        for button in self.mode_buttons:
            button["state"] = "normal"
        for button in self.all_buttons:
            button["state"] = "normal"
        if name in ('SUB_NN_N', 'DIV_NN_Dk', 'DIV_NN_N', 'MOD_NN_N') and int(str(arguments[0])) < int(str(arguments[1])):
            self.instruction.config(text='Первое число должно быть >= второго, операция отменена')
        elif name == 'TRANS_Z_N' and int(str(arguments[0])) < 0:
            self.instruction.config(text='Число должно быть отрицательным, операция отменена')
        elif name in ('DIV_ZZ_Z', 'MOD_ZZ_Z', 'DIV_QQ_Q') and str(arguments[1]) == '0':
            self.instruction.config(text='Делить должен быть отличен от нуля, операция отменена')
        elif name == 'TRANS_Q_Z' and int(str(arguments[0].denom)) != 1:
            self.instruction.config(text='Знаменатель должен быть равен 1, операция отменена')
        else:
            result = str(f(*arguments))
            arguments = [str(i) for i in arguments]
            self.instruction.config(
                text=name + '(' + ', '.join(arguments) + ') = ' + result, wraplength=600)
        self.enter_button["state"] = 'disable'


if __name__ == '__main__':
    root = Tk()
    root.title("Pon")
    root.resizable(False, False)
    app = Main(root)
    root.mainloop()
