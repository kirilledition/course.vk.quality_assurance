from selenium.webdriver.common.by import By


class LoginLocators:
    LOG_IN_BUTTON = (
        By.XPATH,
        "//div[starts-with(@class, 'responseHead-module-button')]",
    )
    LOG_IN_FORM_BUTTON = (
        By.XPATH,
        "//div[starts-with(@class, 'authForm-module-button')]",
    )
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")


class DashboardLocators(LoginLocators):
    MAIL_BUTTON = (By.XPATH, "//div[starts-with(@class, 'right-module-rightButton')]")
    LOG_OUT_BUTTON = (By.XPATH, "//a[@href='/logout']")
    PROFILE = (By.XPATH, "//a[contains(@class, 'profile')]")
    STATISTICS = (By.XPATH, "//a[contains(@class, 'statistics')]")
    USER_NAME = (By.XPATH, "//div[contains(@class, 'userNameWrap')]")
    SPINNER = (By.CLASS_NAME, "spinner")


class ProfileLocators(DashboardLocators):
    FIO = (By.XPATH, "//div[@data-name='fio']/div/input")
    SAVE_BUTTON = (By.XPATH, "//button[@data-class-name='Submit']")
