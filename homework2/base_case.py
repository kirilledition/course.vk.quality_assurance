import pytest
from _pytest.fixtures import FixtureRequest

from ui import pages


class BaseCase:

    browser = None

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, config, request: FixtureRequest):
        self.browser = browser
        self.config = config

        self.dashboard_page: pages.DashboardPage = request.getfixturevalue(
            "get_dashboard_page"
        )
        self.login_page: pages.LoginPage = request.getfixturevalue("get_login_page")
        self.profile_page: pages.LoginPage = request.getfixturevalue("get_profile_page")
