import unittest

from selenium import webdriver
from selenium.webdriver.support.select import Select


import sys
sys.path.append(r'C:\Users\shyam raj\test_hrm_application\pageobjects')
from pageobjects.test_loginpage import Loginpage

class Logintests(unittest.TestCase):
    url=r'https://opensource-demo.orangehrmlive.com/'
    username='Admin'
    password='admin123'
    driver=webdriver.Chrome(executable_path=r'C:\Users\shyam raj\test_hrm_application\drivers\chromedriver.exe')

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
    def test_log(self):
        lp=Loginpage(self.driver)
        lp.setusername(self.username)
        lp.setpassword(self.password)
        lp.clicklogin()
    def tearDown(self):
        self.driver.quit()







