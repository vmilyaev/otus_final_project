import pytest
from selenium import webdriver
from page_objects.LoginPage import LoginPage
from page_objects.DashboardPage import DashboardPage
import allure


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("admin", "password")
    yield
    dashboard_page = DashboardPage(driver)
    dashboard_page.logout()


@allure.feature("Task Management")
@allure.title("Test adding and deleting task")
def test_add_and_delete_task(driver, login):
    dashboard_page = DashboardPage(driver)
    dashboard_page.open()

    task_name = "New Task"
    task_description = "Description of the new task"
    dashboard_page.add_task(task_name, task_description)
    assert dashboard_page.is_task_displayed(task_name)

    dashboard_page.delete_task(task_name)
    assert not dashboard_page.is_task_displayed(task_name)


@allure.feature("Profile Settings")
@allure.title("Test changing profile settings")
def test_change_profile_settings(driver, login):
    dashboard_page = DashboardPage(driver)
    dashboard_page.open()
    dashboard_page.open_profile_settings()

    new_username = "new_username"
    dashboard_page.change_username(new_username)
    dashboard_page.save_changes()

    assert dashboard_page.get_logged_in_username() == new_username


@allure.feature("Login")
@allure.title("Test login with invalid credentials")
def test_login_with_invalid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("invalid_username", "invalid_password")
    assert login_page.is_invalid_credentials_error_displayed()


@allure.feature("Task Management")
@allure.title("Test handling large data")
def test_handle_large_data(driver, login):
    dashboard_page = DashboardPage(driver)
    dashboard_page.open()
    for _ in range(100):
        dashboard_page.add_task("Task", "Description")

    assert dashboard_page.are_all_tasks_displayed()


@allure.feature("Logout")
@allure.title("Test logout redirects to login page")
def test_logout_redirects_to_login_page(driver, login):
    dashboard_page = DashboardPage(driver)
    dashboard_page.logout()
    assert "login" in driver.current_url


@allure.feature("Login")
@allure.title("Test login without credentials")
def test_login_without_credentials(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("", "")
    assert not login_page.is_logged_in()


@allure.feature("Task Management")
@allure.title("Test editing task")
def test_edit_task(driver, login):
    dashboard_page = DashboardPage(driver)
    dashboard_page.open()

    task_name = "Task to Edit"
    task_description = "Description of the task to edit"
    new_task_name = "Edited Task"
    new_task_description = "Description of the edited task"
    dashboard_page.add_task(task_name, task_description)

    dashboard_page.edit_task(task_name, new_task_name, new_task_description)
    assert dashboard_page.is_task_displayed(new_task_name)


@allure.feature("Profile Settings")
@allure.title("Test changing profile picture")
def test_change_profile_picture(driver, login):
    dashboard_page = DashboardPage(driver)
    dashboard_page.open()
    dashboard_page.open_profile_settings()

    dashboard_page.change_profile_picture("path/to/new/picture.jpg")
    assert dashboard_page.is_profile_picture_changed()


@allure.feature("Task Management")
@allure.title("Test sorting tasks")
def test_sort_tasks(driver, login):
    dashboard_page = DashboardPage(driver)
    dashboard_page.open()

    tasks_before_sorting = dashboard_page.get_tasks_list()
    dashboard_page.sort_tasks_by_due_date()
    tasks_after_sorting = dashboard_page.get_tasks_list()

    assert tasks_before_sorting != tasks_after_sorting


@allure.feature("Task Management")
@allure.title("Test searching tasks")
def test_search_tasks(driver, login):
    dashboard_page = DashboardPage(driver)
    dashboard_page.open()

    search_query = "Task"
    dashboard_page.search_tasks(search_query)
    assert dashboard_page.are_search_results_correct(search_query)


@allure.feature("Notifications")
@allure.title("Test receiving notifications")
def test_receive_notifications(driver, login):
    dashboard_page = DashboardPage(driver)
    dashboard_page.open()

    dashboard_page.enable_notifications()
    dashboard_page.add_task("New Task", "Description")
    assert dashboard_page.is_notification_displayed()


@allure.feature("Dashboard")
@allure.title("Test dashboard elements visibility")
def test_dashboard_elements_visibility(driver, login):
    dashboard_page = DashboardPage(driver)
    dashboard_page.open()

    assert dashboard_page.are_dashboard_elements_visible()
