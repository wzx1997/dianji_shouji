import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class NewContactsPage(BaseAction):
    name_text=By.XPATH,"//*[@text='姓名']"
    mobile_text=By.XPATH,"//*[@text='电话']"

    @allure.step(title="输入姓名")
    def name(self,text):
        self.input(self.name_text,text)

    @allure.step(title="输入电话号码")
    def mobile(self,text):
        self.input(self.mobile_text,text)

    @allure.step(title="点击返回")
    def back(self):
        self.press_back()
