from selenium.webdriver.common.by import By

from pages.base import Base


class EditLanguages(Base):

    _add_languages_button_locator = (By.CSS_SELECTOR, '.button[class*="add-languages__add-more"]')
    _add_languages_input_locator = (By.CLASS_NAME, 'add-languages__input')
    _save_button_locator = (By.CSS_SELECTOR, '.button-bar button[type="submit"]')
    _submit_button_locator = (By.CSS_SELECTOR, 'button[class*="add-languages__add-more"]')

    def click_add_languages(self):
        self.find_element(*self._add_languages_button_locator).click()

    def add_language_value(self, new_language):
        language_input = self.find_element(*self._add_languages_input_locator)
        language_input.clear()
        language_input.send_keys(new_language)

    def click_submit_button(self):
        self.find_element(*self._submit_button_locator).click()

    def save_languages(self):
        self.find_element(*self._save_button_locator).click()
