from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time
import allure


class OrderFeedPage(BasePage):
    URL = 'https://stellarburgers.nomoreparties.site/feed'
    CONSTRUCTOR_BUTTON = [By.XPATH, '//a[@href="/"]']
    ORDER_CONTAINER = [By.XPATH, '//a[contains(@href, "/feed/")]']
    MODAL_SECTION = [By.XPATH, '//section[contains(@class, "Modal_modal_opened")]']
    ORDER_ID = [By.XPATH, '//div[contains(@class, "OrderHistory_textBox")]/p[1]']
    COMPLETE_NUMBERS = [By.XPATH, '//p[contains(@class, "OrderFeed_number")]']
    ORDERS_IN_PROGRESS = [By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li']

    @allure.step('Кликаем на кнопку "Конструктор"')
    def click_constructor_button(self):
        return self.click_button(self.CONSTRUCTOR_BUTTON)

    @allure.step('Кликаем на заказ')
    def click_order_container(self):
        return self.click_button(self.ORDER_CONTAINER)

    @allure.step('Получение всех идентификаторов заказов в "Ленте заказов"')
    def get_order_ids(self):     
        self.wait_until_element_visible(self.ORDER_ID)
        order_ids = self.find_elements(self.ORDER_ID)
        return list(map(lambda element: element.text, order_ids))

    @allure.step('Получение значения "Выполнено за все время"')
    def get_compete_all_time(self):     
        self.wait_until_element_visible(self.COMPLETE_NUMBERS)
        numbers = self.find_elements(self.COMPLETE_NUMBERS)
        return numbers[0].text

    @allure.step('Получение значения "Выполнено за сегодня"')
    def get_compete_today(self):     
        self.wait_until_element_visible(self.COMPLETE_NUMBERS)
        numbers = self.find_elements(self.COMPLETE_NUMBERS)
        return numbers[1].text

    @allure.step('Получение заказов в работе')
    def get_orders_in_progress(self):     
        time.sleep(5)
        self.wait_until_element_visible(self.ORDERS_IN_PROGRESS)
        orders = self.find_elements(self.ORDERS_IN_PROGRESS)
        return list(map(lambda element: element.text, orders))

