import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.forgot_password_page import ForgotPasswordPage
import test_data


class TestRecoveryPassword:
    @allure.title('Проверяем переход на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def test_go_to_recovery_password_page(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)

        main_page.to_main_page()
        main_page.click_button_login_account()
        login_page.click_recovery_password_button()
        forgot_password_page.wait_until_url_change(test_data.login_url)

        assert test_data.forgot_password_url == forgot_password_page.get_current_page()

    @allure.title('Проверяем ввод почты в поле Email и клик по кнопке "Восстановить"')
    def test_get_text_email_field(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)

        main_page.to_main_page()
        main_page.click_button_login_account()
        login_page.click_recovery_password_button()
        forgot_password_page.set_email(test_data.recovery_email)
        forgot_password_page.click_recovery_button()
        forgot_password_page.wait_until_url_change(test_data.forgot_password_url)

        assert test_data.reset_password_url == forgot_password_page.get_current_page()

    @allure.title('Проверяем, что клик по кнопке "Показать пароль" подсвечивает поле')
    def test_click_show_password_button(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)

        main_page.to_main_page()
        main_page.click_button_login_account()
        login_page.click_password_visible_button()
        label_class = login_page.get_password_label_class()
        input_type = login_page.get_password_input_type()

        assert input_type == test_data.password_input_visible_type
        assert label_class == test_data.password_label_visible_class
