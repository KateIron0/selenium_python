from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.implicitly_wait(12)
browser.get("http://suninjuly.github.io/explicit_wait2.html")
try:
    y=WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID,"price"),"100"))
    button = browser.find_element_by_id("book")
    button.click()
    import math
    def calk(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element_by_id("input_value")
    x=x_element.text
    z=calk(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(z)
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "solve")))
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(15)
    browser.quit()
