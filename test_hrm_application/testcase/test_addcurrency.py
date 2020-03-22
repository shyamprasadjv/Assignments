import time

from selenium import webdriver

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path=r'C:\Users\shyam raj\test_hrm_application\drivers\chromedriver.exe')
driver.implicitly_wait(10)
url = 'https://opensource-demo.orangehrmlive.com/'
actions = ActionChains(driver)
driver.maximize_window()
def testcaselogin():
        driver.get(url)
        driver.find_element_by_xpath('//input[@name="txtUsername"]').send_keys('Admin')
        driver.find_element_by_xpath('//input[@name="txtPassword"]').send_keys('admin123')
        driver.find_element_by_xpath('//input[@name="Submit"]').click()

        driver.implicitly_wait(10)

def addcurrency():
    admins=driver.find_element_by_xpath('//b[text()="Admin"]')
    users=driver.find_element_by_xpath('//a[text()="User Management"]')
    job=driver.find_element_by_xpath('//a[text()="Job"]')
    paygrades=driver.find_element_by_xpath('//a[text()="Pay Grades"]')
    actions.move_to_element(admins).move_to_element(users).move_to_element(job).move_to_element(paygrades).click().perform()
    driver.find_element_by_xpath('//input[@id="btnAdd"]').click()
    driver.find_element_by_xpath('//input[@id="jobTitle_jobTitle"]').send_keys('Automation Test Engineer')
    driver.find_element_by_xpath('//input[@id="btnSave"]').click()
    driver.implicitly_wait(30)
    time.sleep(23)



testcaselogin()
#addcurrency()

def paygrade():
    driver.implicitly_wait(20)
    admins = driver.find_element_by_xpath('//b[text()="Admin"]')
    users = driver.find_element_by_xpath('//a[text()="User Management"]')
    job = driver.find_element_by_xpath('//a[text()="Job"]')
    paygrades = driver.find_element_by_xpath('//a[text()="Pay Grades"]')
    actions.move_to_element(admins).move_to_element(users).move_to_element(job).move_to_element(paygrades).click().perform()
    time.sleep(20)
    driver.find_element_by_xpath('//input[@name="btnAdd"]').click()
    driver.find_element_by_xpath('//input[@name="payGrade[name]"]').send_keys('Salary Slip')
    driver.find_element_by_xpath('//input[@id="btnSave"]').click()
    time.sleep(4)
paygrade()
def testlogout():
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(10)

    driver.find_element_by_xpath('//a[text()="Welcome Admin"]').click()
    driver.find_element_by_xpath('//a[text()="Logout"]').click()

testlogout()




