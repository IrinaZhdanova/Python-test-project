from .base_page import BasePage
from .locators import BasketLocators


class BasketPage(BasePage):
    def should_be_open_basket(self):
        self.browser.find_element(*BasketLocators.BASKET_BUTTON).click()

    def should_be_empty_basket(self):
        assert "Ваша корзина пуста" in self.browser.find_element(*BasketLocators.EMPTY_BASKET). \
                   text

    def should_not_be_present_basket_products(self):
        assert self.is_not_element_present(*BasketLocators.BASKET_WITH_PRODUCTS), \
            "Basket is not empty"
