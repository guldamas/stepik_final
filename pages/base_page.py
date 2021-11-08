from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser: webdriver.WebKitGTK, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def get_current_url(self):
        return self.browser.current_url


if __name__ == '__main__':
    page = BasePage(webdriver.Chrome(), 'https://google.com')
    page.open()
    print(page.get_current_url())
