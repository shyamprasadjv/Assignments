from selenium import webdriver
import time

from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path=r'C:\Users\shyam raj\test_hrm_application\drivers\chromedriver.exe')
driver.implicitly_wait(10)
url = 'https://opensource-demo.orangehrmlive.com/'
actions = ActionChains(driver)
driver.maximize_window()
def recruitment():
    driver.get(url)
    driver.find_element_by_xpath('//input[@name="txtUsername"]').send_keys('Admin')
    driver.find_element_by_xpath('//input[@name="txtPassword"]').send_keys('admin123')
    driver.find_element_by_xpath('//input[@name="Submit"]').click()


    driver.set_page_load_timeout(3)
    rec=driver.find_element_by_xpath('//b[text()="Recruitment"]')
    canc=driver.find_element_by_xpath('//a[text()="Candidates"]')
    actions.move_to_element(rec).move_to_element(canc).click().perform()
    driver.find_element_by_xpath('//input[@id="btnAdd"]').click()
    driver.find_element_by_xpath('//input[@name="addCandidate[firstName]"]').send_keys('shyam')
    driver.find_element_by_xpath('//input[@name="addCandidate[lastName]"]').send_keys('prasad')
    driver.find_element_by_xpath('//input[@name="addCandidate[email]"]').send_keys('shyamprasadjv@gmail.com')
    driver.implicitly_wait(10)
    time.sleep(3)
    driver.find_element_by_xpath('//input[@name="addCandidate[contactNo]"]').send_keys('9966886477')
    driver.find_element_by_xpath('//input[@name="addCandidate[resume]"]').send_keys(r'C:\Users\shyam raj\Downloads\_shyamresume.pdf')
    driver.find_element_by_xpath('(//input[@type="text"])[6]').send_keys('hrm project')
    driver.find_element_by_xpath('//input[@id="addCandidate_appliedDate"]').clear()
    driver.implicitly_wait(9)
    time.sleep(4)
    driver.find_element_by_xpath('//input[@id="addCandidate_appliedDate"]').send_keys('2020-03-20',Keys.ENTER)
    driver.find_element_by_xpath('//input[@type="checkbox"]').click()
    driver.find_element_by_xpath('//input[@id="btnSave"]').click()
recruitment()


