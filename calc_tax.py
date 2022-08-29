from rate_tax import *
from income_lim import *


def calc_lim_1_tax(income_year):
    return income_year * rate_10


def calc_lim_2_tax(income_year):
    return lim_1 * rate_10 + (income_year - lim_1) * rate_15


def calc_lim_3_tax(income_year):
    return lim_1 * rate_10 + (lim_2 - lim_1) * rate_15 + (income_year - lim_2) * rate_25


def calc_lim_4_tax(income_year):
    return lim_1 * rate_10 + (lim_2 - lim_1) * rate_15 + (lim_3 - lim_2) * rate_25 + (income_year - lim_3) * rate_28


def calc_lim_5_tax(income_year):
    return lim_1 * rate_10 + (lim_2 - lim_1) * rate_15 + (lim_3 - lim_2) * rate_25 + (lim_4 - lim_3) * rate_28 + \
           (income_year - lim_4) * rate_33


def calc_lim_6_tax(income_year):
    return lim_1 * rate_10 + (lim_2 - lim_1) * rate_15 + (lim_3 - lim_2) * rate_25 + (lim_4 - lim_3) * rate_28 + \
           (lim_5 - lim_4) * rate_33 + (income_year - lim_5) * rate_35


def calc_lim_7_tax(income_year):
    return lim_1 * rate_10 + (lim_2 - lim_1) * rate_15 + (lim_3 - lim_2) * rate_25 + (lim_4 - lim_3) * rate_28 + \
           (lim_5 - lim_4) * rate_33 + (lim_6 - lim_5) * rate_35 + (income_year - lim_6) * rate_39
