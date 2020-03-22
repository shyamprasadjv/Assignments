
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

def testadmindata():
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(10)
    admin=driver.find_element_by_xpath('//*[@id="menu_admin_viewAdminModule"]/b')
    usermanagement=driver.find_element_by_xpath('//*[@id="menu_admin_UserManagement"]')
    user=driver.find_element_by_xpath('//*[@id="menu_admin_viewSystemUsers"]')
    actions.move_to_element(admin).move_to_element(usermanagement).move_to_element(user).click().perform()
    driver.find_element_by_xpath('//input[@id="btnAdd"]').click()
    dropdown=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[1]/select')
    s=Select(dropdown)
    s.select_by_index(0)
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[2]/input[1]').send_keys('shyam prasad')
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[3]/input').send_keys('shyamprasad9966')
    dropdown2=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[4]/select')
    s=Select(dropdown2)
    s.select_by_index(0)
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[6]/input').send_keys('Shyam@9966')
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[7]/input[1]').send_keys('Shyam@9966')
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/form/fieldset/p/input[1]').click()

def testlogout():
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(10)

    driver.find_element_by_xpath('//a[text()="Welcome Admin"]').click()
    driver.find_element_by_xpath('//a[text()="Logout"]').click()
testcaselogin()
testadmindata()


testlogout()

















