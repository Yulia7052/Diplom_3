from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage
from pages.history_orders_page import HistoryOrdersPage
import allure


class TestProfile:

    @allure.title('Проверяем переход по клику "Личный кабинет"')
    def test_click_header_profile_button(self, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        main_page.to_main_page()
        main_page.click_button_login_account()
        login_page.wait_until_url_change(base_page.URL)
        login_page.login_user('ulia_manaenkova_10_088@google.com')
        login_page.password_user('123456')
        login_page.click_login_enter_button()
        main_page.click_header_profile_button()
        profile_page.wait_until_url_change(main_page.URL)
        profile_page.wait_until_url_change(profile_page.get_current_page())

        assert profile_page.URL == profile_page.get_current_page()

    @allure.title('Проверяем переход по клику "История заказов"')
    def test_click_history_orders(self, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)
        history_orders = HistoryOrdersPage(driver)  

        main_page.to_main_page()
        main_page.click_button_login_account()
        login_page.wait_until_url_change(base_page.URL)
        login_page.login_user('ulia_manaenkova_10_088@google.com')
        login_page.password_user('123456')
        login_page.click_login_enter_button()
        main_page.click_header_profile_button()
        profile_page.wait_until_url_change(main_page.URL)
        profile_page.wait_until_url_change(profile_page.get_current_page())
        profile_page.click_history_orders_button()

        assert history_orders.URL == history_orders.get_current_page()

    @allure.title('Проверяем выход из аккаунта')
    def test_logout_account(self, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        main_page.to_main_page()
        main_page.click_button_login_account()
        login_page.wait_until_url_change(base_page.URL)
        login_page.login_user('ulia_manaenkova_10_088@google.com')
        login_page.password_user('123456')
        login_page.click_login_enter_button()
        main_page.click_header_profile_button()
        profile_page.wait_until_url_change(main_page.URL)
        profile_page.wait_until_url_change(profile_page.get_current_page())
        profile_page.click_logout_button()
        login_page.wait_until_url_change(profile_page.URL)

        assert login_page.URL == login_page.get_current_page()
