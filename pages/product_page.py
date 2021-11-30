from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button_add_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button_add_basket.click()

    def should_be_correct_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE)
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)
        assert price.text == price_in_basket.text, (
            f'Actual price is "{price_in_basket.text}", but expected "{price.text}"'
        )

    def should_be_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_name_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_BASKET)
        assert book_name.text == book_name_in_basket.text, (
            f'Actual book name is "{book_name_in_basket.text}", but expected "{book_name.text}"'
        )

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
