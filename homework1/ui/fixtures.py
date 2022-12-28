import pytest
from selenium import webdriver

from ui import pages


@pytest.fixture(scope="function")
def browser(config):
    url = config["url"]
    driver = config["driver_path"]

    browser = webdriver.Chrome(executable_path=driver)
    browser.maximize_window()
    browser.get(url)

    yield browser
    browser.quit()


@pytest.fixture
def get_login_page(browser, config):
    return pages.LoginPage(browser=browser, config=config)


@pytest.fixture
def get_dashboard_page(browser, config):
    return pages.DashboardPage(browser=browser, config=config)


@pytest.fixture
def get_profile_page(browser, config):
    return pages.ProfilePage(browser=browser, config=config)
