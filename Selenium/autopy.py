import pyautogui
import time
          

class autmation():
    def __init__(self):
        print("pyatuogui started")
        print(pyautogui.size())
    
    def bhavya_op_desk():
        time.sleep(1.5)
        pyautogui.click(67,465) # Click on OP Desk CCO
        time.sleep(1)
        pyautogui.click(92,496) # Click on Register Visit
        time.sleep(1)

    def neeta_op_desk():
        time.sleep(1.5)
        pyautogui.click(45,284) # Click on OP Desk CCO
        time.sleep(1)
        pyautogui.click(60,318) # Click on Register Visit
        time.sleep(1)

    def register_visit():
        pyautogui.click(153,169)
        time.sleep(1)
        pyautogui.click(153,169)
        time.sleep(1)
        pyautogui.click(153,169)
        time.sleep(1)
        pyautogui.click(519,276)
        time.sleep(1)
        pyautogui.hotkey("ctrl","v")
        time.sleep(1)
        pyautogui.hotkey("tab")
        time.sleep(1)
        time.sleep(1.5)
        pyautogui.hotkey("space")
        time.sleep(2)
        pyautogui.click(973,557) # Click on Dialong pop up
        

    def add_visit_details(diagnos,drname,visit_type):
        time.sleep(2)
        pyautogui.click(475,547)
        time.sleep(1)
        pyautogui.typewrite("Clini")
        pyautogui.hotkey("tab")
        time.sleep(1)
        pyautogui.typewrite(diagnos)
        time.sleep(0.5)
        pyautogui.click(391,640)
        time.sleep(2)
        pyautogui.click(391,640)
        time.sleep(1)
        pyautogui.typewrite(drname)
        time.sleep(1)
        pyautogui.hotkey("tab")
        time.sleep(2)
        pyautogui.click(397,606) # Click on Visit Type
        time.sleep(1)
        pyautogui.typewrite(visit_type)
        time.sleep(0.5)
        pyautogui.hotkey("tab")
        time.sleep(1)

    def one_order(order1): # select Order

        time.sleep(0.5)
        pyautogui.doubleClick(431 ,667)# clinck on order catalog
        time.sleep(1)
        pyautogui.typewrite(order1)
        time.sleep(0.5)
        pyautogui.hotkey("tab")
        time.sleep(2)
        tab = 11
        while tab > 0:
            pyautogui.hotkey("tab")
            time.sleep(0.1)
            tab -= 1
        time.sleep(1)
        pyautogui.hotkey("space") # selecting the first check box
        time.sleep(0.5)
        pyautogui.hotkey("tab") # Hover on ok Button
        time.sleep(0.5)
        pyautogui.hotkey("space") # Cick on ok Button



    def mod_financial_details(remark):

        time.sleep(0.5)
        pyautogui.click(120 ,441) # Click on Financial Details
        time.sleep(3)
        pyautogui.click(1374 ,128) # Click on Modify Button
        time.sleep(1)
        pyautogui.typewrite("KH51003720") # User Id Section
        time.sleep(0.5)
        pyautogui.hotkey("tab")
        time.sleep(0.5)
        pyautogui.typewrite(".") # Pin Section
        time.sleep(0.5)
        pyautogui.hotkey("tab")
        time.sleep(0.5)
        pyautogui.typewrite(remark) # Remartk Section
        time.sleep(0.5)
        pyautogui.hotkey("tab")
        time.sleep(0.5)
        pyautogui.hotkey("space")

    def billing_group(insurance_group):
        time.sleep(1.5)
        pyautogui.click(860 ,128) # Click on Billing Group Space
        time.sleep(0.5)
        pyautogui.click(901 ,130) # Click on Cross/ Clear button
        time.sleep(0.5)
        pyautogui.typewrite(insurance_group)
        time.sleep(0.5)
        pyautogui.hotkey("tab")
        time.sleep(2)
  


    def insurance(corpname,policy_number):
        time.sleep(0.5)
        pyautogui.click(758 ,620) # Cick on Non Insurance Billing Group
        time.sleep(0.5)
        pyautogui.click(758 ,620)# Cick on Non Insurance Billing Group
        time.sleep(0.5)
        pyautogui.typewrite("Cas")
        time.sleep(0.5)
        pyautogui.hotkey("tab")
        time.sleep(1.5)
        pyautogui.click(887 ,602) # Add More Payers
        time.sleep(1)
        pyautogui.click(799 ,259) # Cick on Payer Group
        time.sleep(0.5)
        pyautogui.typewrite("Corporate")
        time.sleep(0.5)
        pyautogui.hotkey("tab")
        time.sleep(1)
        pyautogui.click(825 ,287) # Click on Payer
        time.sleep(0.5)
        pyautogui.typewrite(corpname)
        time.sleep(0.5)
        pyautogui.hotkey("tab")
        time.sleep(1)
        pyautogui.click(805 ,318) # Click on Policy
        time.sleep(0.5)
        pyautogui.typewrite("Corporate")
        time.sleep(0.5)
        pyautogui.hotkey("tab")
        time.sleep(1)
        pyautogui.click(1212, 288) # Priority
        time.sleep(0.5)
        pyautogui.typewrite("1")
        time.sleep(0.5)
        pyautogui.click(1238, 317) # Policy Number
        time.sleep(0.5)
        pyautogui.typewrite(policy_number)
        time.sleep(0.5)
        pyautogui.hotkey("tab")
        time.sleep(0.5)
        pyautogui.click(1216 ,572) # Click on Accept
        time.sleep(0.5)
        pyautogui.click(1447 ,131) # Click on Close
        time.sleep(0.5)
        pyautogui.click(970 ,600) # Click on OK
        time.sleep(0.5)
        pyautogui.click(1022 ,329) # Click on Continue

    def apply_without_fiancial_details():
        time.sleep(0.5)
        pyautogui.click(31 ,139) # Click on Apply Button
        time.sleep(1)
        pyautogui.click(1447 ,131) # Click on Close
        time.sleep(0.5)
        pyautogui.click(970 ,600) # Click on OK
        time.sleep(0.5)
        pyautogui.click(1022 ,329) # Click on Continue
        time.sleep(0.5)
        pyautogui.click(1109 ,599) # Click on Continue
        time.sleep(3)
    
    def order_release():
        time.sleep(1.5)
        pyautogui.click(1407 ,795) # Release of order
        time.sleep(0.5)
        pyautogui.hotkey("space")
        time.sleep(2)
        pyautogui.click(1086 ,602) # ok button of Release
        time.sleep(0.5)
        pyautogui.click(992 ,308) #  Ok Button
        time.sleep(0.5)

    def change_to_tier_two():
        pyautogui.hotkey("win","d")
        time.sleep(1)
        pyautogui.click(508 ,1065) #   Click on 2 Tiier when pinned to first space on the task bar
        time.sleep(1)
    
    def details_in_bill_cum():
        pyautogui.click(591 ,303) # Click on UHID Section
        time.sleep(1)
        pyautogui.hotkey("ctrl","v") # Paste UHID Previously Copied
        time.sleep(0.5)
        pyautogui.hotkey("tab")
        time.sleep(1.5)
        pyautogui.hotkey("f10") # Save
        time.sleep(2)

    def details_in_bill_cum_insurance():
        pyautogui.click(591 ,303) # Click on UHID Section
        time.sleep(1)
        pyautogui.hotkey("ctrl","v") # Paste UHID Previously Copied
        time.sleep(0.5)
        pyautogui.hotkey("tab")
        time.sleep(3)
        pyautogui.hotkey("f10") # Save
        time.sleep(3)
        pyautogui.hotkey("tab") # Move to Id Section
        time.sleep(1)
        pyautogui.hotkey("ctrl","v")
        time.sleep(1)
        pyautogui.hotkey("alt","c")
        time.sleep(1)
        pyautogui.hotkey("enter")


    def settle_page(): # Next page after bill cum
        pyautogui.click(1268 ,327) # Click on small button
        time.sleep(0.5)
        pyautogui.hotkey("tab")
        time.sleep(0.5)
        pyautogui.click(793 ,252) # Switch to Settelment Details
        time.sleep(1)

    def settelment_details_in_cash(): # Final Page
        pyautogui.click(740 ,338)
        time.sleep(0.5)
        pyautogui.doubleClick()
        time.sleep(0.5)
        pyautogui.hotkey("ctrl","c")
        time.sleep(0.5)
        pyautogui.hotkey("tab")
        time.sleep(0.5)
        pyautogui.hotkey("tab")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl","v")

    def register_patient_via_add_visit_metropolis(name,lastname,age,prefix): # Bhavya Cordianates
        time.sleep(1.5)
        pyautogui.click(67,465) # Click on Op Desk CCO
        time.sleep(1)
        pyautogui.click(92,496) # Click on Register Visit
        time.sleep(1)
        pyautogui.click(153,169) # Click on Add Visit 
        time.sleep(1)
        pyautogui.click(153,169)# Click on Add Visit 
        time.sleep(1)
        pyautogui.click(153,169)# Click on Add Visit    
        time.sleep(1)
        pyautogui.click(519,276)# Space for UHID
        time.sleep(1)
        pyautogui.hotkey("tab")# Mark goes to Question Mark / Search
        time.sleep(1)
        pyautogui.hotkey("space") # works as enter
        time.sleep(3)
        pyautogui.click(728,220) # Click on First Name Box 
        time.sleep(0.5)
        pyautogui.typewrite(name) # Enter Random Name
        time.sleep(0.5)
        pyautogui.hotkey("tab") # Move to middle Name
        time.sleep(0.5)
        pyautogui.hotkey("tab") # Move to Sir Name
        time.sleep(0.5)
        pyautogui.typewrite(lastname)  #Enter Random Name
        time.sleep(1)   
        pyautogui.click(1456,403) # Click on Search Button
        time.sleep(4)
        pyautogui.hotkey("space") # Click on pop up saying no records found
        time.sleep(1)
        pyautogui.click(1366,401) # Click on Register Patient
        time.sleep(1)
        pyautogui.click(691,148) # Click on Populate From
        time.sleep(2)
        pyautogui.typewrite("patien") # From the dropdown select populate information
        time.sleep(1)
        pyautogui.hotkey("tab") # Move to sencond tab of Populate From
        time.sleep(1)
        pyautogui.click(726,147) # Click on Populate From
        time.sleep(1)
        pyautogui.typewrite("KH1000756312") # Input UHID Of Metropolis
        time.sleep(2)
        pyautogui.hotkey("tab") # Works as Search
        time.sleep(4)  
        #prefix 1 M = Master, 2 M = Mr., 3 M = Mrs., 4 M = Ms
        pyautogui.click(490,402) # Click on Prefix
        time.sleep(1)
        pyautogui.typewrite(prefix)
        time.sleep(1)
        #pyautogui.typewrite(prefix)
        time.sleep(0.5)
        pyautogui.hotkey("tab")
        time.sleep(1)
        pyautogui.click(1093,428) # Age group, Year selection
        time.sleep(1)
        pyautogui.typewrite(age) # Input
        time.sleep(1)
        pyautogui.click(647,195) # Contact Address Tab
        time.sleep(1)
        pyautogui.click(1088,521) # Click on Mobile Number Input
        time.sleep(1)
        pyautogui.typewrite("9821373916") 
        time.sleep(1)
        pyautogui.hotkey("tab") # Land on Email ID
        time.sleep(1)
        pyautogui.typewrite("bcr.mum@metropolisindia.com")
        time.sleep(1)
        pyautogui.click(772,194) # Click on Related Contacts
        time.sleep(1)
        pyautogui.click(694,237) # Click on Name
        time.sleep(1)
        pyautogui.typewrite("Rahul") # Input Name
        time.sleep(1)
        pyautogui.click(1041,193) # Click on Fiancial Detials in Registration
        time.sleep(2)
        pyautogui.click(807,129) # Click on Primary Billing Group
        time.sleep(1)
        pyautogui.typewrite("Cash") # Input Financial Detials in Cash
        time.sleep(1)
        pyautogui.hotkey("tab") # Land on Email ID
        time.sleep(1)
        pyautogui.click(1248,130) # Click on Close
        time.sleep(1)
        pyautogui.click(580,111) # Click on Apply
        time.sleep(3)
        pyautogui.doubleClick(537,276) # To copy Patient ID 
        time.sleep(1)
        pyautogui.hotkey("ctrl", "c")
        time.sleep(1)
        

        


