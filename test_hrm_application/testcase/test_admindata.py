from selenium import webdriver

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains


driver=webdriver.Chrome(executable_path=r'C:\Users\shyam raj\test_hrm_application\drivers\chromedriver.exe')
actions=ActionChains(driver)
from testcase.test_login11 import testcaselogin
testcaselogin()



def testadmindata():
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(10)
    admin=driver.find_element_by_xpath('//*[@id="menu_admin_viewAdminModule"]/b')
    usermanagement=driver.find_element_by_xpath('//*[@id="menu_admin_UserManagement"]')
    user=driver.find_element_by_xpath('//*[@id="menu_admin_viewSystemUsers"]')
    actions.move_to_element(admin).move_to_element(usermanagement).move_to_element(user).click().perform()
    driver.find_element_by_xpath('//input[@id="btnAdd"]').click()
    dropdown=driver.find_element_by_xpath('//select[@class="formSelect valid"]')
    s=Select(dropdown)
    s.select_by_index(0)
testadmindata()









