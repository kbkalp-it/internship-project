from pages.base_page import Page
from selenium.webdriver.common.by import By

class SettingsMenu(Page):
    MENU_SETTINGS = (By.CSS_SELECTOR, "[class='menu-block'] [href='/settings']")

    def click_settings(self):
        self.click(*self.MENU_SETTINGS)




