from selenium import webdriver
import time
link="http://suninjuly.github.io/alert_accept.html"
try:
    browser=webdriver.Chrome()
    browser.get(link)
    button=browser.find_element_by_css_selector("button.btn")
    button.click()
    confirm=browser.switch_to.alert
    confirm.accept()
    import math
    def calk(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    x_element=browser.find_element_by_id("input_value")
    x=x_element.text
    y=calk(x)
    input1=browser.find_element_by_id("answer")
    input1.send_keys(y)
    button=browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(20)
    browser.quit()



