from .base_page import BasePage
from .elements import DashboardPageElements

class DashboardPage(BasePage):
    def add_task(self, task_name, task_description):
        self.click_element(DashboardPageElements.ADD_TASK_BUTTON)
        self.type_text(DashboardPageElements.TASK_NAME_INPUT, task_name)
        self.type_text(DashboardPageElements.TASK_DESCRIPTION_INPUT, task_description)
        self.click_element(DashboardPageElements.SUBMIT_TASK_BUTTON)

    def delete_task(self, task_name):
        self.click_element(DashboardPageElements.TASK_DELETE_BUTTON(task_name))

    def open_profile_settings(self):
        self.click_element(DashboardPageElements.PROFILE_SETTINGS_BUTTON)

    def get_logged_in_username(self):
        return self.get_element_text(DashboardPageElements.LOGGED_IN_USERNAME)
