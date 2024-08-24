import allure

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


class TestBaseFunctional:

    @allure.title('Проверяем переход по клику "Конструктор"')
    def test_go_to_click_constructor(self, driver):
        main_page = MainPage(driver)
        order_feed = OrderFeedPage(driver)

        main_page.to_main_page()
        main_page.full_screen()
        main_page.click_order_feed_button()
        order_feed.wait_until_url_change(main_page.URL)
        order_feed.click_constructor_button()
        main_page.wait_until_url_change(order_feed.URL)

        assert main_page.URL == main_page.get_current_page()

    @allure.title('Проверяем переход по клику "Лента Заказов"')
    def test_go_to_click_order_feed(self, driver):
        main_page = MainPage(driver)
        order_feed = OrderFeedPage(driver)

        main_page.to_main_page()
        main_page.full_screen()
        main_page.click_order_feed_button()

        assert order_feed.URL == order_feed.get_current_page()

    @allure.title('Проверяем появление всплывающего окна с деталями при нажатии на ингредиент')
    def test_details_ingredient(self, driver):
        main_page = MainPage(driver)

        main_page.to_main_page()
        main_page.click_ingredient_bun()
        main_page.wait_until_url_change(main_page.URL)

        assert True == main_page.check_element_exists(main_page.MODAL_SECTION)

    @allure.title('Проверяем закрытие всплывающего окна с описанием ингредиента')
    def test_click_button_ingredient_modal_open(self, driver):
        main_page = MainPage(driver)

        main_page.to_main_page()
        main_page.click_ingredient_bun()
        main_page.click_modal_close_button()

        assert False == main_page.check_element_exists(main_page.MODAL_SECTION)

    @allure.title('Проверяем увеличение каунтера ингредиента при его добавлении в заказ')
    def test_increase_counter_ingredient(self, driver):
        main_page = MainPage(driver)

        main_page.to_main_page()
        ingredient = main_page.get_first_ingridient()
        constructor_top = main_page.find_element(main_page.CONSTRUCTOR_ELEMENT_TOP)
        main_page.drag_and_drop(ingredient, constructor_top)
        
        counter = main_page.find_element(main_page.INGRIDIENT_COUNTER).text

        assert 0 < int(counter)

    @allure.title('Проверка, что залогиненный пользователь может оформить заказ')
    def test_make_order(self, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.to_main_page()
        main_page.click_button_login_account()
        login_page.wait_until_url_change(base_page.URL)
        login_page.login_user('ulia_manaenkova_10_088@google.com')
        login_page.password_user('123456')
        login_page.click_login_enter_button()
        main_page.wait_until_url_change(login_page.URL)

        assert True == main_page.check_element_exists(main_page.MAKE_ORDER_BUTTON)
