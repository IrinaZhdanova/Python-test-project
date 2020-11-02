import pytest
from pages.main_page import MainPage
from pages.product_page import BookPage
from pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link2 = ['0',
         '1',
         '2',
         '3',
         '4',
         '5',
         '6',
         '7',
         '8',
         '9']


def test_guest_can_add_product_to_basket(browser):
    page = MainPage(browser, link)
    page.open()
    book_card = BookPage(browser, browser.current_url)
    book_card.should_be_book_name()
    book_card.should_be_basket_button()
    page.solve_quiz_and_get_code()
    book_card.should_be_popup_purchase()
    book_card.book_name_after_purchase()
    book_card.should_be_the_same_book()


@pytest.mark.parametrize('param', link2)
@pytest.mark.xfail(link2[7], reason="test with bug")
def test_guest_can_add_product_to_basket_several_times(browser, param):
    link_null = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{param}"
    page = MainPage(browser, link_null)
    page.open()
    book_card = BookPage(browser, browser.current_url)
    book_card.should_be_book_name()
    book_card.should_be_basket_button()
    page.solve_quiz_and_get_code()
    book_card.should_be_popup_purchase()
    book_card.book_name_after_purchase()
    book_card.should_be_the_same_book()


@pytest.mark.xfail(reason="test with popup bug")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = MainPage(browser, link)
    page.open()
    book_card = BookPage(browser, browser.current_url)
    book_card.should_be_book_name()
    book_card.should_be_basket_button()
    book_card.should_not_be_successful_popup()


def test_guest_cant_see_success_message(browser):
    page = MainPage(browser, link)
    page.open()
    book_card = BookPage(browser, browser.current_url)
    book_card.should_not_be_successful_popup()


@pytest.mark.xfail(reason="test with popup bug")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = MainPage(browser, link)
    page.open()
    book_card = BookPage(browser, browser.current_url)
    book_card.should_be_book_name()
    book_card.should_be_basket_button()
    book_card.should_not_be_successful_popup_disappeared()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = MainPage(browser, link)
    page.open()
    basket = BasketPage(browser, browser.current_url)
    basket.should_be_open_basket()
    basket.should_be_empty_basket()
    basket.should_not_be_present_basket_products()
