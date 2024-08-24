import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage


class TestRecoveryPassword:
    @allure.title('Проверяем переход на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def test_go_to_recovery_password_page(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)

        main_page.to_main_page()
        main_page.click_button_login_account()
        login_page.click_recovery_password_button()
        forgot_password_page.wait_until_url_change(login_page.URL)

        assert forgot_password_page.URL == forgot_password_page.get_current_page()

    @allure.title('Проверяем ввод почты в поле Email и клик по кнопке "Восстановить"')
    def test_get_text_email_field(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)

        main_page.to_main_page()
        main_page.click_button_login_account()
        login_page.click_recovery_password_button()
        forgot_password_page.set_email('ulia346@mail.ru')
        forgot_password_page.click_recovery_button()
        reset_password_page.wait_until_url_change(forgot_password_page.URL)

        assert reset_password_page.URL == reset_password_page.get_current_page()

    @allure.title('Проверяем, что клик по кнопке "Показать пароль" подсвечивает поле')
    def test_click_show_password_button(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)

        main_page.to_main_page()
        main_page.click_button_login_account()
        login_page.click_password_visible_button()
        label_class = login_page.get_password_label_class()
        input_type = login_page.get_password_input_type()

        assert input_type == 'text'
        assert label_class == 'input__placeholder text noselect text_type_main-default input__placeholder-focused'
