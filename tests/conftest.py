import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from web_driver_factory import WebDriverFactory
import test_data


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    driver_factory = WebDriverFactory()
    driver = driver_factory.get_webdriver(request.param)

    yield driver

    driver.quit()


@pytest.fixture()
def make_order():
    def make_order_func(main_page: MainPage, login_page: LoginPage):
        main_page.click_button_login_account()
        login_page.wait_until_url_change(test_data.main_url)
        login_page.login_user(test_data.login)
        login_page.password_user(test_data.password)
        login_page.click_login_enter_button()
        main_page.wait_until_url_change(test_data.login_url)
        
        ingredient = main_page.get_first_ingredient()
        constructor_top = main_page.find_element(main_page.CONSTRUCTOR_ELEMENT_TOP)
        main_page.drag_and_drop(ingredient, constructor_top)

        main_page.click_make_order_button()
        main_page.wait_until_element_invisible(main_page.MODAL_LOADER)
        order_id = main_page.get_order_id()
        main_page.click_modal_close_button()

        return order_id
    
    return make_order_func
