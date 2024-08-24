import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    URL = 'https://stellarburgers.nomoreparties.site/forgot-password'
    EMAIL_FIELD = [By.NAME, 'name']
    RECOVERY_BUTTON = [By.XPATH, '//button[contains(text(), "Восстановить")]']

    @allure.step('Заполняем Email')
    def set_email(self, email):
        self.set_input_value(self.EMAIL_FIELD, email)

    @allure.step('Нажимаем на кнопку "Восстановить пароль"')
    def click_recovery_button(self):
        self.click_button(self.RECOVERY_BUTTON)
