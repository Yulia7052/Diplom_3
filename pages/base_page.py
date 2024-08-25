from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

import test_data


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def to_main_page(self):
        self.driver.get(test_data.main_url)

    def check_element_exists(self, element):
        try:
            self.driver.find_element(*element)
        except NoSuchElementException:
            return False
        return True

    def find_element(self, element):
        return self.driver.find_element(*element)

    def find_elements(self, element):
        return self.driver.find_elements(*element)

    def wait_until_page_loaded(self, title):
        WebDriverWait(self.driver, 4).until(expected_conditions.title_is(title))

    def wait_until_url_change(self, url):
        WebDriverWait(self.driver, 4).until(expected_conditions.url_changes(url))

    def wait_until_element_visible(self, element):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((element[0], element[1])))

    def wait_until_element_invisible(self, element):
        WebDriverWait(self.driver, 3).until(expected_conditions.invisibility_of_element_located((element[0], element[1])))

    def wait_until_text_in_element(self, element, text):
        WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element((element[0], element[1]), text))

    def click_button(self, button):
        self.wait_until_element_visible(button)
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((button[0], button[1])))
        self.find_element(button).click()

    def get_text(self, element):
        self.wait_until_element_visible(element)
        return self.find_element(element).text

    def set_input_value(self, input, value):
        self.wait_until_element_visible(input)
        self.find_element(input).send_keys(value)

    def set_select_value(self, select, value):
        self.click_button(select)
        self.click_button(value)

    def set_date_value(self, datepicker, day):
        self.click_button(datepicker)
        self.click_button(day)

    def set_dropdown_value(self, dropdown, value):
        self.click_button(dropdown)
        self.click_button(value)

    def get_attribute(self, element, attribute):
        el = self.find_element(element)
        return el.get_attribute(attribute)

    def get_current_page(self):
        return self.driver.current_url

    def full_screen(self):
        return self.driver.fullscreen_window()
    
    def drag_and_drop(self, source_el, dest_el):
        ActionChains(self.driver).drag_and_drop(source_el, dest_el).perform()
