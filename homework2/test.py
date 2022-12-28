import pytest

from base_case import BaseCase


class TestMyTarget(BaseCase):
    @pytest.mark.UI
    def test_login_no_credits(self):
        self.login_page.login(email='', password='')

    @pytest.mark.UI
    def test_login_no_password(self):
        self.login_page.login(password='')

    @pytest.mark.UI
    def test_compain_create(self):
        pass

    @pytest.mark.UI
    def test_segment_create(self):
        pass
