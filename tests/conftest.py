import pytest
from web_driver_factory import WebDriverFactory


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    driver_factory = WebDriverFactory()
    driver = driver_factory.get_webdriver(request.param)

    yield driver

    driver.quit()
