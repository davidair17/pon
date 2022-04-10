from naturals import *
from integer import *
from rational import *
from polynome import *
from tkinter import *
from idlelib.tooltip import Hovertip
from buttons import buttons


class Main(Frame):
    modes = [('Натуральные', 'Natural'), ('Целые', 'Integer'), ('Рациональные', 'Rational'), ('Многочлены', 'Polynome')]
    mode_buttons = []
    enter_button = []
    instruction = []
    argument = 0
    entry = []
    var = 0
    all_buttons = []
    buttons = buttons

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
        label.grid(row=1, column=0, columnspan=4, padx=(5, 5), pady=(5, 5))
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
        self.instruction.config(text='Введите натуральное число или ноль')
        self.enter_button.wait_variable(self.var)
        s = self.entry.get()
        while not self.is_natural(s):
            self.instruction.config(text='Неправильный формат, попробуйте ещё раз')
            self.enter_button.wait_variable(self.var)
            s = self.entry.get()
        return Natural(s)

    def is_integer(self, n):
        return n.isdigit() or n[1:].isdigit and n[0] == '-'

    def get_integer(self):
        self.instruction.config(text='Введите целое число')
        self.enter_button.wait_variable(self.var)
        s = self.entry.get()
        while not self.is_integer(s):
            self.instruction.config(text='Неправильный формат, попробуйте ещё раз')
            self.enter_button.wait_variable(self.var)
            s = self.entry.get()
        return Integer(s)

    def is_rational(self, n):
        if '/' in n:
            return self.is_integer(n.split('/')[0]) and self.is_natural(n.split('/')[1])
        return self.is_integer(n)

    def get_rational(self):
        self.instruction.config(text='Введите рациональное число (дробь)')
        self.enter_button.wait_variable(self.var)
        s = self.entry.get()
        while not self.is_rational(s):
            self.instruction.config(text='Неправильный формат, попробуйте ещё раз')
            self.enter_button.wait_variable(self.var)
            s = self.entry.get()
        return Rational(s)

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
            elif i == 'Z':
                arguments.append(self.get_integer())
            elif i == 'Q':
                arguments.append(self.get_rational())
        for button in self.mode_buttons:
            button["state"] = "normal"
        for button in self.all_buttons:
            button["state"] = "normal"
        result = str(f(*arguments))
        arguments = [str(i) for i in arguments]
        self.instruction.config(text=name + '(' + ', '.join(arguments) + ') = ' + result, wraplength=600)


if __name__ == '__main__':
    root = Tk()
    root.title("Pon")
    root.resizable(False, False)
    app = Main(root)
    root.mainloop()
