from selenium.webdriver.common.by import By


class LoginPageElements:
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")
    INVALID_CREDENTIALS_ERROR_MESSAGE = (By.ID, "error-message")


class DashboardPageElements:
    LOGOUT_BUTTON = (By.ID, "logout")
    NOTIFICATION = (By.ID, "notification")
    NOTIFICATION_CLOSE_BUTTON = (By.CLASS_NAME, "close-button")
    # Остальные локаторы...
