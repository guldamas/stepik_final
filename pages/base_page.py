from selenium import webdriver

class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self, url=None):
        self.browser.get(url or self.url)


if __name__ == '__main__':
    page = BasePage(webdriver.Chrome(), 'https://google.com')
    page.open()
