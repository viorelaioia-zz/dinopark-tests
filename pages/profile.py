from selenium.webdriver.common.by import By

from pages.base import Base


class Profile(Base):
    _profile_picture_locator = (By.CSS_SELECTOR, '.user-picture.user-picture--large')
    _edit_profile_intro_button_locator =  (By.CSS_SELECTOR, '.profile__intro .profile__edit-button')
    _first_name_input_field_locator = (By.ID, 'field-first-name')
    _save_button_locator = (By.CSS_SELECTOR, '.button-bar button[type="submit"]')
    _name_locator = (By.CSS_SELECTOR, '.profile__name h1')

    @property
    def is_profile_picture_shown(self):
        return self.is_element_displayed(*self._profile_picture_locator)

    @property
    def name(self):
        return self.find_element(*self._name_locator).text

    def edit_profile_intro(self):
        self.find_element(*self._edit_profile_intro_button_locator).click()

    def add_first_name(self, first_name):
        first_name_input = self.find_element(*self._first_name_input_field_locator)
        first_name_input.clear()
        first_name_input.send_keys(first_name)

    def save_intro(self):
        self.find_element(*self._save_button_locator).click()
