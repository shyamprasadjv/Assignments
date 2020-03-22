from selenium import webdriver

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains


driver=webdriver.Chrome(executable_path=r'C:\Users\shyam raj\test_hrm_application\drivers\chromedriver.exe')
actions=ActionChains(driver)
from testcase.test_login11 import testcaselogin
testcaselogin()
#driver.set_page_load_timeout(30)
driver.implicitly_wait(10)
driver.get('https://opensource-demo.orangehrmlive.com/index.php/leave/assignLeave')

def leavedata():
    #driver.find_element_by_xpath('(//span[text()="Assign Leave"]//..//..)[3]').click()
    #driver.set_page_load_timeout(10)
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[1]/input[1]').send_keys('Robert Craig')
    leave=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[2]/select')
    s=Select(leave)
    s.select_by_index(2)
    driver.find_element_by_xpath('//input[@id="assignleave_txtFromDate"]').send_keys('2020-03-15')
    driver.find_element_by_xpath('//input[@id="assignleave_txtToDate"]').send_keys('2020-03-16')
    partialdays=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[7]/select')
    s=Select(partialdays)
    s.select_by_index(1)
    day=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[8]/select')
    s=Select(day)
    s.select_by_index(0)
    shift=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[8]/span[1]/select')
    s=Select(shift)
    s.select_by_index(0)
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[10]/textarea').send_keys('Thanks For giving leave')
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/p/input').click()
leavedata()





