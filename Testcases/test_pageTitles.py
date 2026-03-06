import logging
import pytest
from Testcases.BaseTest import BaseTest
from Pages.BasePage import BasePage
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)

PAGE_TITLES = [
    ("Admin", "Admin"),
    ("PIM", "PIM"),
    ("Leave", "Leave"),
    ("Time", "Time"),
    ("Recruitment", "Recruitment"),
    ("My Info", "PIM"),
    ("Performance", "Performance"),
    ("Directory", "Directory"),
    ("Dashboard", "Dashboard"),
    ("Claim", "Claim"),
    ("Buzz", "Buzz"),
]

@pytest.mark.usefixtures("logged_in")
class TestPageTitles(BaseTest):

    @pytest.mark.parametrize("module, expected_title", PAGE_TITLES)
    def test_page_title(self, driver, module, expected_title):
        log.logger.info("Test - page_title started")
        base = BasePage(driver)
        base.open_module(module)
        base.assert_page_title(expected_title)
        log.logger.info("Test - page_title ended")