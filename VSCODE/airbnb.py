#aller sur Airbnb; regarder le premier prix d'un séjour de 3 jours à Paris de dimanche à mardi (1 adulte)

import string
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, re


binary = f"C:\Drivers\geckodriver.exe"
browser = webdriver.Firefox(executable_path=binary)

class PrixAirbnbParis1Adulte(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=binary)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_prix_airbnb_paris1_adulte(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.airbnb.fr/")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Expériences en ligne'])[1]/following::div[7]").click()
        driver.find_element_by_id("bigsearch-query-detached-query").clear()
        driver.find_element_by_id("bigsearch-query-detached-query").send_keys("Paris")
        driver.find_element_by_xpath(u"//div[contains(text(),'Arrivée')]").click()
        driver.find_element_by_xpath("//div[@id='panel--tabs--0']/div/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[3]/td[7]/div/div/div").click()
        driver.find_element_by_xpath("//div[@id='panel--tabs--0']/div/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[4]/td[2]/div/div/div").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Voyageurs'])[1]/following::div[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Adultes'])[1]/following::*[name()='svg'][2]").click()
        driver.find_element_by_xpath("//span/span").click()
        Prix = driver.find_element_by_xpath("//span[contains(text(), 'au total')]").text
        print(Prix)
        print ("Le prix est de : " +Prix)
        element = driver.find_element_by_xpath("//span[contains(text(), 'Sweet & Cosy')]")
        driver.execute_script("arguments[0].click();", element)
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
        driver.find_element_by_xpath("//div[3]/form/button/span/span").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Continuer avec Apple'])[1]/following::div[5]").click()
        
    
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



    
    
