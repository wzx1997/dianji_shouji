import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestNewContacts:
    def setup(self):
        self.driver=init_driver()
        self.page=Page(self.driver)
    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_file("test_new_contacts.yaml", "test_new_contacts"))
    def test_new_contacts(self,args):
        name=args["name"]
        mobile=args["mobile"]
        self.page.address_book.add_contacts()
        self.page.new_contacts.name(name)
        self.page.new_contacts.mobile(mobile)
        self.page.new_contacts.back()
        assert name == self.page.new_success.name()


