from calc_tax import *


def get_income():
    income = input("Введите свой среднемесячный доход: ")
    try:  # если вычисления возможно, вернется валидное значение годового дохода
        income_v = float(income)
        print("Принято")
        return income_v
    except:  # если валидное значение не вернется, то инструкция запустится вновь
        print("Нужно ввести число")
        get_income()


def calc_tax():
    income_year = 12 * get_income()
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


def get_tax_message(tax):
   return f"Сумма налога за год: {round(tax, 2)}$"


class tax():
    def __init__(self):

