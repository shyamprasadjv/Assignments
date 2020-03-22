from selenium import webdriver
import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


driver=webdriver.Chrome(executable_path=r'C:\Users\shyam raj\test_hrm_application\drivers\chromedriver.exe')
actions=ActionChains(driver)
from testcase.test_login11 import testcaselogin,testlogout
wait=WebDriverWait(driver,timeout=8)

driver.implicitly_wait(10)
driver.set_page_load_timeout(30)

def test_pimdatahrm():
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.maximize_window()

    driver.find_element_by_xpath('//input[@name="txtUsername"]').send_keys('Admin')
    driver.find_element_by_xpath('//input[@name="txtPassword"]').send_keys('admin123')
    driver.find_element_by_xpath('//input[@name="Submit"]').click()

    time.sleep(5)
    pims=driver.find_element_by_xpath('//*[@id="menu_pim_viewPimModule"]/b')
    #wait.until(ec.visibility_of_element_located("xpath", pims))

    config=driver.find_element_by_xpath('/html/body/div[1]/div[2]/ul/li[2]/ul/li[1]/a')
    optionalfiled=driver.find_element_by_xpath('/html/body/div[1]/div[2]/ul/li[2]/ul/li[1]/ul/li[1]/a')
    actions.move_to_element(pims).move_to_element(config).move_to_element(optionalfiled).click().perform()
    driver.find_element_by_xpath('(//input[@type="button"])[4]').click()
    driver.find_element_by_xpath('//input[@name="configPim[chkDeprecateFields]"]').click()
    driver.find_element_by_xpath('//input[@name="configPim[chkShowSSN]"]').click()
    time.sleep(6)
    driver.find_element_by_xpath('//input[@name="configPim[chkShowSIN]"]').click()
    driver.find_element_by_xpath('//input[@id="configPim_chkShowTax"]').click()
    driver.find_element_by_xpath('//input[@id="btnSave"]').click()




test_pimdatahrm()
#testlogout()
