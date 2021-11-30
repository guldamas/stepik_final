from .base_page import BasePage
from .locators import BasketLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        empty_basket = self.browser.find_element(*BasketLocators.EMPTY_BASKET)
        assert empty_basket.text == "Your basket is empty. Continue shopping", "Basket not empty"
