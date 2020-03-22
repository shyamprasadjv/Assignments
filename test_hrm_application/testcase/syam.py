from selenium import webdriver
import time

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
def testcaselogin():
    driver.get(url)
    driver.find_element_by_xpath('//input[@name="txtUsername"]').send_keys('Admin')
    driver.find_element_by_xpath('//input[@name="txtPassword"]').send_keys('admin123')
    driver.find_element_by_xpath('//input[@name="Submit"]').click()
    driver.get('https://opensource-demo.orangehrmlive.com/index.php/leave/assignLeave')
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[1]/input[1]').send_keys('Robert Craig')
    leave = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[2]/select')
    s = Select(leave)
    s.select_by_index(2)
    driver.find_element_by_xpath('//input[@id="assignleave_txtFromDate"]').clear()
    driver.find_element_by_xpath('//input[@id="assignleave_txtFromDate"]').send_keys('2020-03-15')
    driver.find_element_by_xpath('//input[@id="assignleave_txtToDate"]').clear()
    driver.find_element_by_xpath('//input[@id="assignleave_txtToDate"]').send_keys('2020-03-16',Keys.ENTER)
    time.sleep(5)
    driver.implicitly_wait(4)

    partialdays = driver.find_element_by_xpath('//select[@id="assignleave_partialDays"]')
    s = Select(partialdays)
    s.select_by_index(1)
    day = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[8]/select')
    s = Select(day)
    s.select_by_index(0)
    shift = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[8]/span[1]/select')
    s = Select(shift)
    s.select_by_index(0)
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[10]/textarea').send_keys('Thanks For giving leave')
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/p/input').click()
testcaselogin()