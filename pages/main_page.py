from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        self.is_element_present_on_page(*LoginPageLocators.LOGIN_FORM)
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login link is not presented"

    def should_be_register_page(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form is not presented"
