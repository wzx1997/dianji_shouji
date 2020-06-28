from page.address_book_page import AddressBookPage
from page.new_contacts_page import NewContactsPage
from page.new_success_page import NewSuccessPage


class Page:
    def __init__(self,driver):
        self.driver=driver
    @property
    def address_book(self):
        return AddressBookPage(self.driver)
    @property
    def new_contacts(self):
        return NewContactsPage(self.driver)
    @property
    def new_success(self):
        return NewSuccessPage(self.driver)