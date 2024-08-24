from selenium import webdriver


class WebDriverFactory:

    browsers = {
        'firefox': webdriver.Firefox,
        'chrome': webdriver.Chrome
    }

    def get_webdriver(self, browser_name):
        if browser_name in self.browsers:
            driver = self.browsers[browser_name]()
        else:
            driver = webdriver.Chrome()

        return driver
