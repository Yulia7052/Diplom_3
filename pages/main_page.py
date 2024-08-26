import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    LOGIN_BUTTON = [By.XPATH, '//button[contains(text(), "Войти в аккаунт")]']
    HEADER_PROFILE_BUTTON = [By.XPATH, '//a[@href="/account"]']
    CONSTRUCTOR_BUTTON = [By.XPATH, '//a[@href="/"]']
    ORDER_FEED_BUTTON = [By.XPATH, '//a[@href="/feed"]']
    INGRIDIENT_CONTAINER = [By.XPATH, '//a[contains(@href, "/ingredient/")]']
    INGRIDIENT_COUNTER = [By.XPATH, '//a[contains(@href, "/ingredient/")]/div[1]/p']
    CONSTRUCTOR_ELEMENT_TOP = [By.CLASS_NAME, 'constructor-element_pos_top']
    MODAL_SECTION = [By.XPATH, '//section[contains(@class, "Modal_modal_opened")]']
    MODAL_LOADER = [By.XPATH, '//div[contains(@class, "Modal_modal_opened")]']
    MODAL_CLOSE_BUTTON = [By.XPATH, '//button[contains(@class, "Modal_modal__close")]']
    MODAL_TITLE = [By.XPATH, '//h2[contains(@class, "Modal_modal__title")]']
    MAKE_ORDER_BUTTON = [By.XPATH, '//button[contains(text(), "Оформить заказ")]']

    @allure.step('Кликаем на кнопку "Войти в аккаунт"')
    def click_button_login_account(self):
        return self.click_button(self.LOGIN_BUTTON)

    @allure.step('Кликаем на кнопку "Личный кабинет"')
    def click_header_profile_button(self):
        return self.click_button(self.HEADER_PROFILE_BUTTON)

    @allure.step('Кликаем на кнопку "Конструктор"')
    def click_constructor_button(self):
        return self.click_button(self.CONSTRUCTOR_BUTTON)

    @allure.step('Кликаем на кнопку "Лента Заказов"')
    def click_order_feed_button(self):
        return self.click_button(self.ORDER_FEED_BUTTON)

    @allure.step('Кликаем на ингредиент "Флюорисцентная булка"')
    def click_ingredient_bun(self):
        return self.click_button(self.INGRIDIENT_CONTAINER)

    @allure.step('Кликаем на крестик окна с описанием ингредиента')
    def click_modal_close_button(self):
        return self.click_button(self.MODAL_CLOSE_BUTTON)

    @allure.step('Получаем идентификатор заказа')
    def get_order_id(self):
        self.wait_until_element_visible(self.MODAL_TITLE)
        return self.find_element(self.MODAL_TITLE).text

    @allure.step('Кликаем на кнопку "Оформить заказ"')
    def click_make_order_button(self):
        return self.click_button(self.MAKE_ORDER_BUTTON)

    @allure.step('Получаем первый ингредиент')
    def get_first_ingredient(self):
        self.wait_until_element_visible(self.INGRIDIENT_CONTAINER)
        return self.find_element(self.INGRIDIENT_CONTAINER)

    @allure.step('Получаем верхний элемент конструктора')
    def get_constructor_top_element(self):
        self.wait_until_element_visible(self.CONSTRUCTOR_ELEMENT_TOP)
        return self.find_element(self.CONSTRUCTOR_ELEMENT_TOP)

    @allure.step('Получаем каунтер первого ингредиента')
    def get_first_ingredient_counter(self):
        self.wait_until_element_visible(self.INGRIDIENT_COUNTER)
        return self.find_element(self.INGRIDIENT_COUNTER)

    @allure.step('Проверяем, что открылось модальное окно ингредиентов')
    def check_ingredient_modal_section_exists(self):
        return self.check_element_exists(self.MODAL_SECTION)

    @allure.step('Проверяем наличие кнопки "Оформить заказ" на странице')
    def check_order_button_exists(self):
        return self.check_element_exists(self.MAKE_ORDER_BUTTON)
