from automate import automate
from autopy import autmation as bot1

with automate() as bot:
    bot.land_first_page()

    bot.handel_info()

    bot.enter_login_bhavya()

    bot.hand_switch()

#Had to switch to pyautogui as Selenium IE webdriver did not Support Hospital API

bot1()

#enter patient name, lastname, and prefix Mr. Master or Mrs
bot1.register_patient_via_add_visit_metropolis(" A.R"," Maharugde","31","Mr") # Will work with Bhavya Setup

bot1.add_visit_details("Diag","Exter","First Vis")

bot1.one_order("Methemoglo")

bot1.mod_financial_details("Metropolis")

bot1.billing_group("Ins")

bot1.insurance("Metropolis Healthcare Ltd","1")

bot1.apply_without_fiancial_details()

bot1.order_release()

bot1.change_to_tier_two()

bot1.details_in_bill_cum_insurance()







