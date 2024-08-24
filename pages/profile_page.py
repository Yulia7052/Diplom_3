import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProfilePage(BasePage):
    URL = 'https://stellarburgers.nomoreparties.site/account/profile'
    HISTORY_ORDERS_BUTTON = [By.XPATH, '//a[@href="/account/order-history"]']
    ACCOUNT_LOGOUT_BUTTON = [By.XPATH, '//button[contains(text(), "Выход")]']
    HISTORY_ORDER_ID = [By.XPATH, '//div[contains(@class, "OrderHistory_textBox")]/p[1]']

    @allure.step('Кликаем на кнопку "История заказов"')
    def click_history_orders_button(self):
        return self.click_button(self.HISTORY_ORDERS_BUTTON)

    @allure.step('Кликаем на кнопку "Выход"')
    def click_logout_button(self):
        return self.click_button(self.ACCOUNT_LOGOUT_BUTTON)

    @allure.step('Получение всех идентификаторов заказов в "Истории заказов"')
    def get_order_ids(self):
        self.wait_until_element_visible(self.HISTORY_ORDER_ID)
        order_ids = self.find_elements(self.HISTORY_ORDER_ID)
        return list(map(lambda element: element.text, order_ids))
