import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
import test_data


class TestBaseFunctional:

    @allure.title('Проверяем переход по клику "Конструктор"')
    def test_go_to_click_constructor(self, driver):
        main_page = MainPage(driver)
        order_feed = OrderFeedPage(driver)

        main_page.to_main_page()
        main_page.full_screen()
        main_page.click_order_feed_button()
        order_feed.wait_until_url_change(test_data.main_url)
        order_feed.click_constructor_button()
        main_page.wait_until_url_change(test_data.feed_url)

        assert test_data.main_url == main_page.get_current_page()

    @allure.title('Проверяем переход по клику "Лента Заказов"')
    def test_go_to_click_order_feed(self, driver):
        main_page = MainPage(driver)
        order_feed = OrderFeedPage(driver)

        main_page.to_main_page()
        main_page.full_screen()
        main_page.click_order_feed_button()

        assert test_data.feed_url == order_feed.get_current_page()

    @allure.title('Проверяем появление всплывающего окна с деталями при нажатии на ингредиент')
    def test_details_ingredient(self, driver):
        main_page = MainPage(driver)

        main_page.to_main_page()
        main_page.click_ingredient_bun()
        main_page.wait_until_url_change(test_data.main_url)

        assert main_page.check_ingredient_modal_section_exists()

    @allure.title('Проверяем закрытие всплывающего окна с описанием ингредиента')
    def test_click_button_ingredient_modal_open(self, driver):
        main_page = MainPage(driver)

        main_page.to_main_page()
        main_page.click_ingredient_bun()
        main_page.click_modal_close_button()

        assert False == main_page.check_ingredient_modal_section_exists()

    @allure.title('Проверяем увеличение каунтера ингредиента при его добавлении в заказ')
    def test_increase_counter_ingredient(self, driver):
        main_page = MainPage(driver)

        main_page.to_main_page()
        ingredient = main_page.get_first_ingredient()
        constructor_top = main_page.get_constructor_top_element()
        main_page.drag_and_drop(ingredient, constructor_top)
        
        counter = main_page.get_first_ingredient_counter().text

        assert 0 < int(counter)

    @allure.title('Проверка, что залогиненный пользователь может оформить заказ')
    def test_make_order(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.to_main_page()
        main_page.click_button_login_account()
        login_page.wait_until_url_change(test_data.main_url)
        login_page.login_user(test_data.login)
        login_page.password_user(test_data.password)
        login_page.click_login_enter_button()
        main_page.wait_until_url_change(test_data.login_url)

        assert main_page.check_order_button_exists()
