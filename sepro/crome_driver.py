from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome(executable_path='./driver/chromedriver 2')
driver.get('https://accounts.google.com/signup')


driver.find_element(By.NAME,"firstName").send_keys("arpita")
driver.find_element(By.NAME,"lastName").send_keys("patel")
driver.find_element(By.ID,"username").send_keys("patelarpita2367")
driver.find_element(By.NAME,"Passwd").send_keys("patelarpita45375")
driver.find_element(By.NAME,"ConfirmPasswd").send_keys("patelarpita45375")
driver.find_element(By.ID,"accountDetailsNext").click()
#driver.find_element(By.ID,"identifierId").send_keys('ap')

#element=driver.find_elements_by_class_name("ng-scope") 
#drp=Select(element)
#drp.select_by_visible_text
#driver.implicitly_wait(4)
#element.click()