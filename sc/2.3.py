from selenium import webdriver
import time
link="http://suninjuly.github.io/selects1.html"

try:
    browser=webdriver.Chrome()
    browser.get(link)

    x_element=browser.find_element_by_id("num1")
    x=int(x_element.text)
    y_element=browser.find_element_by_id("num2")
    y=int(y_element.text)
    result=x+y
    input1=browser.find_element_by_id("dropdown")
    input1.send_keys(result)

    from selenium.webdriver.support.ui import Select
    select=Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(result))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
       time.sleep(15)
       browser.quit()

