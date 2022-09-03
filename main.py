# from calc_tax import *
from tkinter import *
from tax_class import tax


class terminal():

    def __init__(self):

        self.income_field_label = None
        self.state = None
        self.list_state = None
        self.calc_box_btn = None
        self.root = Tk()  # создание окна
        self.root.title('Fed tax')  # создание титульной надписи
        self.root.minsize(500, 400)  # минимальный размер окна
        self.create_ent()  # создание поля ввода
        self.create_income_field()

        self.income_field_label.pack()
        self.income_field.pack()
        self.income_field_space.pack()
        self.state_label.pack()
        self.variants.pack()

        self.create_calc_box()
        self.root.mainloop()

    def create_ent(self):
        self.state = ['Калифорния', 'Техас', 'Нью Йорк', 'Не указывать штат']
        self.list_state = StringVar()
        self.list_state.set(self.state[0])

        self.state_label = Label(text="Выберите свой штат")
        self.variants = OptionMenu(self.root,
                                   self.list_state,
                                   *self.state,
                                   command=self.variants_event_listener)

    def variants_event_listener(self, value):
        self.list_state.set(value)

    def create_income_field(self):
        self.income_field_label = Label(
            text="Введите свой среднемесячный доход:")
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
            income = float(self.income_field.get())
            state = self.list_state.get()
            messages = tax(income, state).get_message()
            self.place_tax_message_text(messages)
        else:
            self.income_field.config({"background": "red"})

    def validate_income(self):
        income = self.income_field.get()
        try:
            float(income)
            return True
        except:
            return False

    def place_tax_message_text(self, messages):
        empty_label = Label()
        empty_label.pack()
        for message in messages:
            tax_label = Label(text=message)
            tax_label.pack()


terminal()