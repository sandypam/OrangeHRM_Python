import logging
import pytest

from Pages.claimPage import ClaimPage

from Testcases.BaseTest import BaseTest
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)

@pytest.mark.usefixtures("logged_in")
class TestClaimPage(BaseTest):
    pass
