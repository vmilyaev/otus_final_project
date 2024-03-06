from selenium.webdriver.common.by import By


class LoginPageElements:
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")
    INVALID_CREDENTIALS_ERROR_MESSAGE = (By.ID, "error-message")


class DashboardPageElements:
    ADD_TASK_BUTTON = (By.ID, "add-task")
    TASK_NAME_INPUT = (By.ID, "task-name")
    TASK_DESCRIPTION_INPUT = (By.ID, "task-description")
    SUBMIT_TASK_BUTTON = (By.ID, "submit-task")
    TASK_DELETE_BUTTON = lambda task_name: (
        By.XPATH, f"//li[contains(text(), '{task_name}')]/following-sibling::button[@class='delete-button']")
    PROFILE_SETTINGS_BUTTON = (By.ID, "profile-settings")
    LOGGED_IN_USERNAME = (By.ID, "logged-in-username")
