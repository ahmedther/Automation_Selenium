from automate import automate
from autopy import autmation


with automate() as bot:

    bot.land_first_page()

    bot.handel_info()

    bot.enter_login_bhavya()

    bot.hand_switch()

# Had to switch to pyautogui as Selenium IE webdriver did not Support Hospital API

autmation.bhavya_op_desk()

autmation.register_visit() # to get add visit window

autmation.add_visit_details()

autmation.muone_order() # for seleting multi order

autmation.apply_without_fiancial_details()

autmation.order_release()


# Change to 2 Tier

autmation.change_to_tier_two()

autmation.details_in_bill_cum()

autmation.settle_page()

autmation.settelment_details_in_cash()

#KH1000763563
