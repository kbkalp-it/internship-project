from pages.base_page import Page
from selenium.webdriver.common.by import By

class SettingsMenu(Page):
    # MENU_SETTINGS = (By.CSS_SELECTOR, "[class='menu-block'] [href='/settings']")
    ### Added the locator for chrome mobile testing ###
    MENU_SETTINGS = (By.CSS_SELECTOR, "div.new-market-menu.mobil a[href='/settings']")

    def click_settings(self):
        self.click(*self.MENU_SETTINGS)




