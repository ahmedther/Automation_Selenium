from selenium import webdriver
import os


class automate(webdriver.Ie):
    def __init__(self, driverpath = r'C:\Users\\6enurse\Downloads\All Portables\WPy32-31010b4\scripts',):
        self.driverpath = driverpath
        os.environ ['PATH'] = self.driverpath
        super(automate,self).__init__()
        self.implicitly_wait(5)
        

    def __exit__(self, exc_type, exc_val,exc_):
        self.quit

    def land_first_page(self):
        self.get("http://em.kdahit.com/HIS/eSM/jsp/login.jsp")

    def enter_login_bhavya(self):
        login_page = self.find_element_by_xpath('(//input[@class="inputH"])[1]')
        login_page.send_keys('KH51001021')

        login_password = self.find_element_by_xpath('(//input[@class="inputH"])[2]')
        login_password.send_keys("satish")

        login_button = self.find_element_by_id('loginID')
        login_button.click()
    
    def enter_login_neeta(self):
        login_page = self.find_element_by_xpath('(//input[@class="inputH"])[1]')
        login_page.send_keys('KH51001261')

        login_password = self.find_element_by_xpath('(//input[@class="inputH"])[2]')
        login_password.send_keys("trayati23")

        login_button = self.find_element_by_id('loginID')
        login_button.click()

        login_button = self.find_element_by_id('loginID')
        login_button.click()

    def test(self):
        id = self.find_element_by_name('pat_id1')
        id.send_keys('KH51001261')

      
    def handel_info(self):
        handel1_info = self.current_window_handle
        print(handel1_info)
        

    def hand_switch(self):
        handel1_info = self.current_window_handle
        hand_list =  self.window_handles
        for handle in hand_list:
            print(f"All Handle = {handle}")
            if handle not in handel1_info:
                self.switch_to.window(handle)
                print(f"Switched to window: : {handle}")


    def rech_to_visit(self):
        op_desk = self.find_element_by_id('jd167')
        op_desk.click()
