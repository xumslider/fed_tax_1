from calc_tax import *


class tax():

    def __init__(self, income, state):
        self.rate_by_state = {
            "Техас": 0.087,
            "Калифорния": 0.093,
            "Нью Йорк": 0.0882
        }
        self.income_year = 12 * income
        self.tax = self.calc_tax(self.income_year)
        self.state = state

    def calc_tax(self, income_year):
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

    def get_calc_state_tax(self):
        rate = self.rate_by_state.get(self.state, None)
        if rate:
            return round(rate * self.income_year, 2)
        else:
            return None

    def get_state_tax_message(self):
        state_tax = self.get_calc_state_tax()
        state = self.state
        if state_tax:
            return f"Сумма налога штата {state}: {state_tax}"
        else:
            return "Налог штата не рассчитан"

    def get_message(self):
        tax = self.tax
        message_tax = f"Сумма федерального налога за год: {round(tax, 2)}$"
        message_state_tax = self.get_state_tax_message()
        return (message_tax, message_state_tax)

