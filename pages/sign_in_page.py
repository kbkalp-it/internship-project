from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignInPage(Page):
    USERNAME_FIELD = (By.ID, 'email-2')
    PASSWORD_FIELD = (By.ID, 'field')
    CONTINUE_BTN = (By.CSS_SELECTOR, '.login-button')

    username = 'kbkalp8@gmail.com'
    password = 'Jigidi@98765'

    def input_username(self):
        self.input_text(self.username, *self.USERNAME_FIELD)

    def input_password(self):
        self.input_text(self.password, *self.PASSWORD_FIELD)

    def click_continue(self):
        self.click(*self.CONTINUE_BTN)
