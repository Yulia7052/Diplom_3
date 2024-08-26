import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    RECOVERY_PASSWORD_BUTTON = [By.XPATH, '//a[@href="/forgot-password"]']
    PASSWORD_VISIBLE_BUTTON = [By.CLASS_NAME, 'input__icon-action']
    LOGIN_ENTER_BUTTON = [By.XPATH, '//button[contains(text(), "Войти")]']
    PASSWORD_LABEL = [By.XPATH, '//label[contains(text(), "Пароль") and contains(@class, "input__placeholder")]']
    PASSWORD_INPUT = [By.NAME, "Пароль"]
    LOGIN_EMAIL_FIELD_NAME = [By.NAME, 'name']
    PASS_FIELD_NAME = [By.NAME, 'Пароль']

    @allure.step('Кликаем на кнопку "Восстановить пароль"')
    def click_recovery_password_button(self):
        return self.click_button(self.RECOVERY_PASSWORD_BUTTON)

    @allure.step('Кликаем на кнопку, которая показывает пароль')
    def click_password_visible_button(self):
        return self.click_button(self.PASSWORD_VISIBLE_BUTTON)

    @allure.step('Получаем лэйбл класса поля с паролем')
    def get_password_label_class(self):
        return self.get_attribute(self.PASSWORD_LABEL, 'class')

    @allure.step('Получаем тип класса поля с паролем')
    def get_password_input_type(self):
        return self.get_attribute(self.PASSWORD_INPUT, 'type')

    @allure.step('Вводим Email для входа в аккаунт')
    def login_user(self, email):
        return self.set_input_value(self.LOGIN_EMAIL_FIELD_NAME, email)

    @allure.step('Вводим пароль для входа в аккаунт')
    def password_user(self, password):
        return self.set_input_value(self.PASS_FIELD_NAME, password)

    @allure.step('Кликаем на кнопку "Войти"')
    def click_login_enter_button(self):
        return self.click_button(self.LOGIN_ENTER_BUTTON)


