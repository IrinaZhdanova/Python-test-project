from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '.col-sm-6.register_form')


class PurchaseCard:
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    BOOK_NAME_BEFORE = (By.CSS_SELECTOR, '.col-sm-6.product_main >h1')
    BOOK_NAME_AFTER = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    POP_UP_AFTER_PURCHASE = (By.XPATH, '//*[@id="messages"]/div[1]/div')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasketLocators:
    BASKET_BUTTON = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner >p")
    BASKET_WITH_PRODUCTS = (By.CSS_SELECTOR, '.basket_summary')
