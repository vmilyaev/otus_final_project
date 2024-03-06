from page_objects.BasePage import BasePage
from elements.locators import LoginPageElements


class LoginPage(BasePage):
    def login(self, username, password):
        self.type_text(LoginPageElements.USERNAME_INPUT, username)
        self.type_text(LoginPageElements.PASSWORD_INPUT, password)
        self.click_element(LoginPageElements.LOGIN_BUTTON)

    def is_invalid_credentials_error_displayed(self):
        return self.is_element_displayed(LoginPageElements.INVALID_CREDENTIALS_ERROR_MESSAGE)

    def is_logged_in(self):
        pass
