from .base_page import BasePage
from .locators import AddToBasketLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button_add_basket = self.browser.find_element(*AddToBasketLocators.ADD_TO_BASKET)
        button_add_basket.click()

    def should_be_correct_price(self):
        price = self.browser.find_element(*AddToBasketLocators.PRICE)
        price_in_basket = self.browser.find_element(*AddToBasketLocators.PRICE_IN_BASKET)
        assert price.text == price_in_basket.text, (
            f'Actual price is "{price_in_basket.text}", but expected "{price.text}"'
        )

    def should_be_book_name(self):
        book_name = self.browser.find_element(*AddToBasketLocators.BOOK_NAME)
        book_name_in_basket = self.browser.find_element(*AddToBasketLocators.BOOK_NAME_IN_BASKET)
        assert book_name.text == book_name_in_basket.text, (
            f'Actual book name is "{book_name_in_basket.text}", but expected "{book_name.text}"'
        )
