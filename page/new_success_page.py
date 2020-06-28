import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class NewSuccessPage(BaseAction):
    name_text=By.ID,"com.android.contacts:id/large_title"

    @allure.step(title="检测是否输入到联系人当中")
    def name(self):
        return self.find_element(self.name_text).text