#from calc_tax import *
from tkinter import *


class terminal():
    def __init__(self):

        self.income_field_label = None
        self.state = None
        self.list_state = None
        self.calc_box_btn = None
        self.root = Tk()    #создание окна
        self.root.title('Fed tax')  #создание титульной надписи
        self.root.minsize(500, 400)  #минимальный размер окна
        self.create_ent()   #создание поля ввода
        self.create_income_field()

        self.income_field_label.pack()
        self.income_field.pack()
        self.income_field_space.pack()
        self.state_label.pack()
        self.variants.pack()

        self.create_calc_box()
        self.root.mainloop()

    def create_ent(self):
        self.state = ['California', 'Texas', 'New York', 'Не указывать штат']
        self.list_state = StringVar()
        self.list_state.set(self.state[0])

        self.state_label = Label(text="Выберите свой штат")
        self.variants = OptionMenu(
            self.root, self.list_state, *self.state,
            command = self.variants_event_listener)

    def variants_event_listener(self, value):
        self.list_state.set(value)

    def create_income_field(self):
        self.income_field_label = Label(text="Введите свой среднемесячный доход:")
        self.income_field = Entry()
        self.income_field_space = Label()

    def create_calc_box(self):
        self.calc_box = Label()
        self.calc_box_btn = Button(text="Рассчитать налог")
        self.calc_box_btn.bind('<Button>', self.calculate)
        self.calc_box.pack()
        self.calc_box_btn.pack()

    def calculate(self, event):
        is_valid = self.validate_income()
        if is_valid:
            self.income_field.config({"background": "green"})
        else:
            self.income_field.config({"background": "red"})

    def validate_income(self):
        income = self.income_field.get()
        try:
            float(income)
            return True
        except:
            return False






terminal()


def calc_tax(self):
    income_year = 12 * float(income)
    if lim_1 >= income_year:
        return calc_lim_1_tax(income_year)
    if lim_1 < income_year <= lim_2:
        return calc_lim_2_tax(income_year)
    if lim_2 < income_year <= lim_3:
        return calc_lim_3_tax(income_year)
    if lim_3 < income_year <= lim_4:
        return calc_lim_4_tax(income_year)
    if lim_4 < income_year <= lim_5:
        return calc_lim_5_tax(income_year)
    if lim_5 < income_year <= lim_6:
        return calc_lim_6_tax(income_year)
    if lim_6 < income_year:
        return calc_lim_7_tax(income_year)



def print_tax(self):
            if self.countries_state[0]:
                print("\nСумма федерального налога за год: " + f'{round(calc_tax(), 2)}' + "$")

            if self.countries_state[1]:
                print("\nСумма федерального налога за год: " + f'{round(calc_tax(), 2)}' + "$")

            if self.countries_state[2]:
                print("\nСумма федерального налога за год: " + f'{round(calc_tax(), 2)}' + "$")

