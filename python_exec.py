# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import unittest, time, re

class PythonExec(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.tescoviews.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_python_exec(self):
        driver = self.driver
        driver.get("https://www.tescoviews.com")
        driver.find_element_by_id("promptInput_175080").clear()
        driver.find_element_by_id("promptInput_175080").send_keys("3486")
        driver.find_element_by_xpath(".//*[@id='nextPageLink']").click()
        driver.find_element_by_xpath("//div[@id='prompt_260074']/div[2]/div/div/div[2]/span").click()
        driver.find_element_by_id("option_546860_260074").click()
        driver.find_element_by_xpath(".//*[@id='nextPageLink']").click()
        time.sleep(5)
        driver.find_element_by_xpath(".//*[@id='nextPageLink']").click()
        driver.find_element_by_xpath(".//*[@id='promptInput_174686']").send_keys("26/06/2016")
        driver.find_element_by_xpath(".//*[@id='nextPageLink']").click()
        #this is the place of time 5pm - 7pm
        driver.find_element_by_xpath("//div[@id='prompt_174687']/div[2]/div/div/div[7]/span").click()
        driver.find_element_by_xpath(".//*[@id='nextPageLink']").click()


        driver.find_element_by_id("option_506920_238214").click()
        driver.find_element_by_xpath(".//*[@id='nextPageLink']").click()

        time.sleep(5)

        driver.find_element_by_xpath(".//*[@id = 'prompt_174691']/label/span").click()
        driver.find_element_by_xpath(".//*[@id='nextPageLink']").click()
        driver.find_element_by_xpath(".//*[@id = 'prompt_241867']/label/span").click()
        driver.find_element_by_xpath(".//*[@id='nextPageLink']").click()
        driver.find_element_by_xpath(".//*[@id = 'prompt_241886']/div[2]/div/div[1]/div/div/div[1]/label/div/div").click()
        driver.find_element_by_xpath(".//*[@id='nextPageLink']").click()

        driver.find_element_by_xpath(".//*[@id='prompt_242526']/div[2]/div/div[1]/div[1]/span").click()
        driver.find_element_by_xpath(".//*[@id='prompt_243223']/div[2]/div/div[1]/div[1]/span").click()
        driver.find_element_by_xpath(".//*[@id='nextPageLink']").click()

        driver.find_element_by_xpath(".//*[@id = 'prompt_243151']/div[2]/div/div[1]/div[1]/span").click()
        driver.find_element_by_xpath(".//*[@id = 'prompt_174889']/div[2]/div/div[1]/div[1]/span").click()
        driver.find_element_by_xpath(".//*[@id='nextPageLink']").click()

        driver.find_element_by_xpath(".//*[@id = 'prompt_174892']/div[2]/div/div[1]/div/div/div[1]/label/div/div").click()
        driver.find_element_by_xpath(".//*[@id='nextPageLink']").click()

        driver.find_element_by_xpath(".//*[@id = 'prompt_174901']/div[2]/div/div[1]/div[1]/span").click()
        driver.find_element_by_xpath(".//*[@id = 'prompt_174900']/div[2]/div/div[1]/div[1]/span").click()
        driver.find_element_by_xpath(".//*[@id='nextPageLink']").click()

        driver.find_element_by_xpath(".//*[@id = 'prompt_174898']/div[2]/div/div[1]/div[1]/span").click()
        driver.find_element_by_xpath(".//*[@id='nextPageLink']").click()

        driver.find_element_by_xpath(".//*[@id='prompt_174905']/div[2]/div/div[1]/div/div/div[1]/label/div/div").click()
        driver.find_element_by_xpath(".//*[@id='prompt_174907']/div[2]/div/div[1]/div/div/div[1]/label/div/div").click()
        driver.find_element_by_xpath(".//*[@id='prompt_223245']/div[2]/div/div[1]/div/div/div[1]/label/div/div").click()
        driver.find_element_by_xpath(".//*[@id='prompt_174909']/div[2]/div/div[1]/div/div/div[1]/label/div/div").click()
        driver.find_element_by_xpath(".//*[@id='prompt_174912']/div[2]/div/div[1]/div/div/div[1]/label/div/div").click()
        driver.find_element_by_xpath(".//*[@id='nextPageLink']").click()

        driver.find_element_by_xpath(".//*[@id='prompt_242531']/div[2]/div/div[1]/div/div/div[1]/label/div/div").click()
        driver.find_element_by_xpath(".//*[@id='nextPageLink']").click()

        driver.find_element_by_xpath(".//*[@id='prompt_174945']/div[2]/div/div[1]/div[3]/span").click()
        driver.find_element_by_xpath(".//*[@id='nextPageLink']").click()

        driver.find_element_by_xpath(".//*[@id='prompt_174949']/div[2]/div/div[1]/div[1]/span").click()
        driver.find_element_by_xpath(".//*[@id='prompt_174948']/div[2]/div/div[1]/div[1]/span").click()
        driver.find_element_by_xpath(".//*[@id='nextPageLink']").click()

        driver.find_element_by_xpath(".//*[@id='prompt_174976']/div[2]/div/div[1]/div[2]/span").click()
        driver.find_element_by_xpath(".//*[@id='nextPageLink']").click()

        driver.find_element_by_xpath(".//*[@id='prompt_174990']/div[2]/div/div[1]/div[1]/span").click()
        driver.find_element_by_xpath(".//*[@id='prompt_242545']/div[2]/div/div[1]/div/div/div[1]/label/div/div").click()
        driver.find_element_by_xpath(".//*[@id='nextPageLink']").click()


        driver.find_element_by_xpath(".//*[@id='prompt_210746']/div[2]/div/div[1]/div[1]/span").click()
        driver.find_element_by_xpath(".//*[@id='nextPageLink']").click()

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        driver.find_element_by_xpath(".//*[@id='prompt_242547']/div[2]/div/div[1]/div[10]/span").click()
        driver.find_element_by_xpath(".//*[@id='nextPageLink']").click()

        driver.find_element_by_xpath(".//*[@id='prompt_174706']/div[2]/div/div[1]/div/div/div[1]/label/div/div").click()
        driver.find_element_by_xpath(".//*[@id='prompt_174707']/div[2]/div/div[1]/div/div/div[1]/label/div/div").click()
        driver.find_element_by_xpath(".//*[@id='prompt_176616']/div[2]/div/div[1]/div/div/div[1]/label/div/div").click()
        driver.find_element_by_xpath(".//*[@id='prompt_176618']/div[2]/div/div[1]/div/div/div[1]/label/div/div").click()
        driver.find_element_by_xpath(".//*[@id='nextPageLink']").click()

        driver.find_element_by_xpath(".//*[@id='prompt_176383']/div[2]/div/div[1]/div[3]/span").click()
        driver.find_element_by_xpath(".//*[@id='prompt_176382']/div[2]/div/div[1]/div[1]/span").click()
        driver.find_element_by_xpath(".//*[@id='prompt_223373']/label/span").click()
        driver.find_element_by_xpath(".//*[@id='nextPageLink']").click()

        driver.find_element_by_xpath(".//*[@id='prompt_223371']/div[2]/div/div[1]/div[7]/span").click()
        driver.find_element_by_xpath(".//*[@id='nextPageLink']").click()

        driver.find_element_by_xpath(".//*[@id='promptInput_261489']").clear()
        driver.find_element_by_xpath(".//*[@id='promptInput_261489']").send_keys("firstname")
        driver.find_element_by_xpath(".//*[@id='promptInput_261490']").clear()
        driver.find_element_by_xpath(".//*[@id='promptInput_261490']").send_keys("lastname")
        driver.find_element_by_xpath(".//*[@id='promptInput_261495']").clear()
        driver.find_element_by_xpath(".//*[@id='promptInput_261495']").send_keys("phonenum")
        driver.find_element_by_xpath(".//*[@id='promptInput_176377']").clear()
        driver.find_element_by_xpath(".//*[@id='promptInput_176377']").send_keys("emailid")
        driver.find_element_by_xpath(".//*[@id='promptInput_229325']").clear()
        driver.find_element_by_xpath(".//*[@id='promptInput_229325']").send_keys("123456789") //club card number
        driver.find_element_by_xpath(".//*[@id='nextPageLink']").click()

    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
