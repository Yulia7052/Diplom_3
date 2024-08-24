import allure

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.order_feed_page import OrderFeedPage


class TestOrderFeed:

    @allure.step('Вспомогательный метод, который помогает делать заказ залогиненному пользователю')
    def make_order(self, base_page: BasePage, main_page: MainPage, login_page: LoginPage):
        main_page.click_button_login_account()
        login_page.wait_until_url_change(base_page.URL)
        login_page.login_user('ulia_manaenkova_10_088@google.com')
        login_page.password_user('123456')
        login_page.click_login_enter_button()
        main_page.wait_until_url_change(login_page.URL)
        
        ingredient = main_page.get_first_ingridient()
        constructor_top = main_page.find_element(main_page.CONSTRUCTOR_ELEMENT_TOP)
        main_page.drag_and_drop(ingredient, constructor_top)

        main_page.click_make_order_button()
        main_page.wait_until_element_invisible(main_page.MODAL_LOADER)
        order_id = main_page.get_order_id()
        main_page.click_modal_close_button()

        return order_id

    @allure.title('Проверяем открытие окна с описанием заказа при нажатии на заказ')
    def test_order_modal_open(self, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.to_main_page()
        main_page.full_screen()
        self.make_order(base_page, main_page, login_page)

        main_page.click_order_feed_button()
        order_feed_page.click_order_container()

        assert True == order_feed_page.check_element_exists(order_feed_page.MODAL_SECTION)

    @allure.title('Проверяем, что заказы, которые есть в "История заказов" есть в "Лента заказов"')
    def test_history_orders_exists_in_order_feed(self, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.to_main_page()
        main_page.full_screen()
        self.make_order(base_page, main_page, login_page)
        
        main_page.click_header_profile_button()
        profile_page.click_history_orders_button()
        history_order_ids = profile_page.get_order_ids()

        main_page.click_order_feed_button()
        order_ids = order_feed_page.get_order_ids()

        assert history_order_ids[::-1][0] in order_ids

    @allure.title('Проверяем, что при создании заказа счетчик "Выполнено за все время" увеличивается')
    def test_complete_for_all_time_increase(self, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.to_main_page()
        main_page.full_screen()

        main_page.click_order_feed_button()
        old_all_time_number = order_feed_page.get_compete_all_time()

        main_page.to_main_page()
        main_page.full_screen()
        self.make_order(base_page, main_page, login_page)

        main_page.click_order_feed_button()
        new_all_time_number = order_feed_page.get_compete_all_time()

        assert int(old_all_time_number) < int(new_all_time_number)

    @allure.title('Проверяем, что при создании заказа счетчик "Выполнено за сегодня" увеличивается')
    def test_complete_for_today_increase(self, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.to_main_page()
        main_page.full_screen()

        main_page.click_order_feed_button()
        old_today_number = order_feed_page.get_compete_today()

        main_page.to_main_page()
        main_page.full_screen()
        self.make_order(base_page, main_page, login_page)

        main_page.click_order_feed_button()
        new_today_number = order_feed_page.get_compete_today()

        assert int(old_today_number) < int(new_today_number)

    @allure.title('Проверяем, что при создании заказа его номер появляется в разделе "В работе"')
    def test_order_in_progress(self, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.to_main_page()
        main_page.full_screen()
        order_id = self.make_order(base_page, main_page, login_page)

        main_page.click_order_feed_button()
        orders_in_progress = order_feed_page.get_orders_in_progress()

        assert f"0{order_id}" in orders_in_progress
