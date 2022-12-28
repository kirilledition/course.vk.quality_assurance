import pytest

import utils
from base_case import BaseCase


class TestMyTarget(BaseCase):
    @pytest.mark.UI
    def test_login(self):
        self.login_page.login()

        assert "dashboard" in self.browser.current_url

    @pytest.mark.UI
    def test_logout(self):
        self.login_page.login()
        self.dashboard_page.logout()

        assert self.browser.current_url == "https://target.my.com/"

    @pytest.mark.UI
    @pytest.mark.parametrize("locator_name", ["PROFILE", "STATISTICS"])
    def test_transition(self, locator_name):
        self.login_page.login()
        self.dashboard_page.transition(locator_name)

        assert locator_name.lower() in self.browser.current_url

    @pytest.mark.UI
    def test_profile_change(self):
        self.login_page.login()
        self.dashboard_page.transition("PROFILE")
        new_name = utils.get_random_string()
        self.profile_page.change_name(new_name)
        self.browser.refresh()
        user_name = self.dashboard_page.get_name()

        assert user_name == new_name
