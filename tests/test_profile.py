from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage
import allure

import test_data


class TestProfile:

    @allure.title('Проверяем переход по клику "Личный кабинет"')
    def test_click_header_profile_button(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        main_page.to_main_page()
        main_page.click_button_login_account()
        login_page.wait_until_url_change(test_data.main_url)
        login_page.login_user(test_data.login)
        login_page.password_user(test_data.password)
        login_page.click_login_enter_button()
        main_page.click_header_profile_button()
        profile_page.wait_until_url_change(test_data.main_url)
        profile_page.wait_until_url_change(profile_page.get_current_page())

        assert test_data.profile_url == profile_page.get_current_page()

    @allure.title('Проверяем переход по клику "История заказов"')
    def test_click_history_orders(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        main_page.to_main_page()
        main_page.click_button_login_account()
        login_page.wait_until_url_change(test_data.main_url)
        login_page.login_user(test_data.login)
        login_page.password_user(test_data.password)
        login_page.click_login_enter_button()
        main_page.click_header_profile_button()
        profile_page.wait_until_url_change(test_data.main_url)
        profile_page.wait_until_url_change(profile_page.get_current_page())
        profile_page.click_history_orders_button()

        assert test_data.order_history_url == profile_page.get_current_page()

    @allure.title('Проверяем выход из аккаунта')
    def test_logout_account(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        main_page.to_main_page()
        main_page.click_button_login_account()
        login_page.wait_until_url_change(test_data.main_url)
        login_page.login_user(test_data.login)
        login_page.password_user(test_data.password)
        login_page.click_login_enter_button()
        main_page.click_header_profile_button()
        profile_page.wait_until_url_change(test_data.main_url)
        profile_page.wait_until_url_change(profile_page.get_current_page())
        profile_page.click_logout_button()
        login_page.wait_until_url_change(test_data.profile_url)

        assert test_data.login_url == login_page.get_current_page()
