from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC

class LanguageSettingPage(Page):

    LANGUAGE_DROPDOWN = (By.CSS_SELECTOR, "[class*='w-dropdown-toggle']")
    LANGUAGE_OPTION_RU = (By.XPATH, "//a[@lang='ru' and text()='RU']")
    CURRENT_LANGUAGE = (By.CSS_SELECTOR, "[class*='wg-dd-1-togle-3']")


    def select_language(self):
        toggle = self.find_element(*self.LANGUAGE_DROPDOWN)
        # Used ActionChains here because the dropdown requires a mouse hover
        # to trigger the visibility of the language options. A regular .click()
        # does not work as the element remains unselectable until hovered over.
        ActionChains(self.driver).move_to_element(toggle).perform()
        self.driver.implicitly_wait(1)
        print("Dropdown clicked")
        ru_option = self.driver.wait.until(EC.visibility_of_element_located(self.LANGUAGE_OPTION_RU))
        print("Dropdown opened and RU option is visible.")
        ru_option.click()
        sleep(1)

    def verify_selected_language(self):
        selected_lang = self.find_element(*self.CURRENT_LANGUAGE)
        # Using get_attribute("lang") to retrieve the current language code (e.g., 'ru', 'en')
        # from the selected element.
        lang_value = selected_lang.get_attribute("lang")
        print("Selected language is: " + lang_value)
        assert lang_value == "ru", f"Expected 'ru', but got '{lang_value}'"
        print("Language changed to Russian successfully!")