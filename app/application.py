from pages.base_page import Page
from pages.main_page import MainPage
from pages.sign_in_page import SignInPage
from pages.settings_menu_page import SettingsMenu
from pages.language_setting_page import LanguageSettingPage

class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.language_setting_page = LanguageSettingPage(driver)
        self.main_page = MainPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.settings_menu_page = SettingsMenu(driver)
