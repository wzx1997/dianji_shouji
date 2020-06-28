import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class AddressBookPage(BaseAction):

    add_contacts_button = By.ID,"com.android.contacts:id/floating_action_button"

    @allure.step(title="点击添加联系人")
    def add_contacts(self):
        self.click(self.add_contacts_button)