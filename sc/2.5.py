from selenium import webdriver
import time
link="http://suninjuly.github.io/file_input.html"
try:
    browser=webdriver.Chrome()
    browser.get(link)
    input1=browser.find_element_by_name("firstname")
    input1.send_keys("Test")
    input2=browser.find_element_by_name("lastname")
    input2.send_keys("Testov")
    input3=browser.find_element_by_name("email")
    input3.send_keys("123@123.ru")
    import os
    current_dir=os.path.abspath(os.path.dirname('_file_'))
    file_path=os.path.join(current_dir,'file.txt')
    element=browser.find_element_by_id("file")
    element.send_keys(file_path)
    button=browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(15)
    browser.quit()
