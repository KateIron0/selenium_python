import unittest
from selenium import webdriver

class test_class_name(unittest.TestCase):
    def test_lesson1(self):
        self.assertEqual(
            link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector("input[required].first")
        input1.send_keys("Test")
        input2 = browser.find_element_by_css_selector("input[required].second")
        input2.send_keys("Testov")
        input3 = browser.find_element_by_css_selector("input[required].third")
        input3.send_keys("123@123.ru")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text, "Congratulations! You have successfully registered!"
        browser.quit())
if __name__ == "__main__":
    unittest.main()
