import pytest

from ui.fixtures import *


def pytest_addoption(parser):
    parser.addoption("--driver-path", default="/opt/homebrew/bin/chromedriver")
    parser.addoption("--url", default="https://target.my.com/")
    parser.addoption("--click-retry", default=5, type=int)
    parser.addoption("--email", default="qa-auto-python-k-denisov@mail.ru")
    parser.addoption("--password", default="2021-2-VKGROUP")


@pytest.fixture()
def config(request):
    driver_path = request.config.getoption("--driver-path")
    url = request.config.getoption("--url")
    click_retry = request.config.getoption("--click-retry")
    email = request.config.getoption("--email")
    password = request.config.getoption("--password")

    return {
        "driver_path": driver_path,
        "url": url,
        "click_retry": click_retry,
        "email": email,
        "password": password,
    }
