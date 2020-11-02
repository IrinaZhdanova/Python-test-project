# -*- coding: utf-8 -*-
from .base_page import BasePage
from .locators import PurchaseCard


class BookPage(BasePage):
    def should_be_basket_button(self):
        self.browser.find_element(*PurchaseCard.ADD_TO_BASKET). \
            click(), "Purchase card is not presented"

    def should_be_book_name(self):
        self.book_name_before = self.browser.find_element(*PurchaseCard.BOOK_NAME_BEFORE).text

    def should_be_popup_purchase(self):
        assert "был добавлен в вашу корзину" in \
               self.browser.find_element(*PurchaseCard.POP_UP_AFTER_PURCHASE).text

    def book_name_after_purchase(self):
        self.book_name_after = self.browser.find_element(*PurchaseCard.BOOK_NAME_AFTER).text

    def should_be_the_same_book(self):
        assert self.book_name_before == self.book_name_after, \
            f"There is no the same book"

    def should_not_be_successful_popup(self):
        assert self.is_not_element_present(*PurchaseCard.POP_UP_AFTER_PURCHASE), \
            "Success message is presented, but should not be"

    def should_not_be_successful_popup_disappeared(self):
        assert self.is_disappeared(*PurchaseCard.POP_UP_AFTER_PURCHASE), \
            "Success message is presented, but should not be"
