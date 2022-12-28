import time

from selenium.common import exceptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ui import locators


class BasePage:
    locators = None

    def __init__(self, browser, config):
        self.browser = browser
        self.config = config
        self.click_retry = self.config["click_retry"]

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.browser, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def wait_to_disappear(self, locator, timeout=None):
        try:
            self.wait(timeout).until(EC.presence_of_element_located(locator))
        except exceptions.TimeoutException:
            return

        self.wait(timeout).until(EC.invisibility_of_element_located(locator))

    def click(self, locator, timeout=None):
        for i in range(self.click_retry):
            try:
                elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                elem.click()
                return
            except exceptions.StaleElementReferenceException:
                if i == self.click_retry - 1:
                    raise
            except exceptions.ElementClickInterceptedException:
                if i == self.click_retry - 1:
                    raise
                time.sleep(0.5)

    def send_keys(self, locator, keys):
        inp = self.find(locator)
        inp.clear()
        inp.send_keys(keys)


class LoginPage(BasePage):
    locators = locators.LoginLocators()

    def login(self, email=None, password=None):
        email = email if email is not None else self.config["email"]
        password = password if password is not None else self.config["password"]

        self.click(self.locators.LOG_IN_BUTTON)
        self.send_keys(self.locators.EMAIL, email)
        self.send_keys(self.locators.PASSWORD, password)
        self.click(self.locators.LOG_IN_FORM_BUTTON)


class DashboardPage(BasePage):
    locators = locators.DashboardLocators()

    def logout(self):
        self.wait_to_disappear(self.locators.SPINNER)
        self.click(self.locators.MAIL_BUTTON)
        self.click(self.locators.LOG_OUT_BUTTON)

    def transition(self, locator_name):
        locator = getattr(self.locators, locator_name)
        self.click(locator)

    def get_name(self):
        return self.find(self.locators.USER_NAME).text


class ProfilePage(DashboardPage):
    locators = locators.ProfileLocators()

    def change_name(self, new_name):
        self.send_keys(self.locators.FIO, new_name)
        self.click(self.locators.SAVE_BUTTON)
