import time

from selenium import webdriver
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

    driver.implicitly_wait(10)
def employeelistedit():
    pims=driver.find_element_by_xpath('//b[text()="PIM"]')
    empl=driver.find_element_by_xpath('//a[text()="Employee List"]')
    actions.move_to_element(pims).move_to_element(empl).click().perform()
    driver.find_element_by_xpath('//a[text()="Russel"]').click()
    driver.implicitly_wait(4)
    time.sleep(8)
    driver.find_element_by_xpath('(//input[@type="button"])[4]').click()
    driver.find_element_by_xpath('//input[@class="calendar editable calendar hasDatepicker"]').clear()
    driver.find_element_by_xpath('//input[@class="calendar editable calendar hasDatepicker"]').send_keys('2020-03-25',Keys.ENTER)
    #obj=driver.find_element_by_xpath('//select[@name="personal[cmbMarital]"]')
    #time.sleep(9)
    #s=Select(obj)
    #s.select_by_value('Indian')


    obj1=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div[2]/form/fieldset/ol[3]/li[2]/select')
    s=Select(obj1)
    s.select_by_visible_text('Married')
    #driver.find_element_by_xpath('//input[@name="personal[txtEmpNickName]"]').send_keys('Nick Jonas')
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div/div/a/img').click()
    driver.find_element_by_xpath('//input[@id="photofile"]').send_keys(r'C:\Users\shyam raj\Downloads\d15306aed51db2d3344a3c94ce396483.jpg')
    driver.find_element_by_xpath('//input[@id="btnSave"]').click()
    #driver.find_element_by_xpath('(//input[@type="button"])[5]').click()
    #driver.find_element_by_xpath('//input[@class="formInputText editable"]').send_keys('1234567890')
testcaselogin()
employeelistedit()







