from selenium.webdriver.common.by import By

from pages.base import Base


class EditProfile(Base):
    _first_name_input_field_locator = (By.ID, 'field-first-name')
    _last_name_input_field_locator = (By.ID, 'field-last-name')
    _pronouns_field_locator = (By.ID, 'field-pronouns')
    _alternative_name_field_locator = (By.ID, 'field-alt-name')
    _fun_job_title_field_locator = (By.ID, 'field-fun-job-title')
    _location_field_locator = (By.ID, 'field-location')
    _timezone_field_locator = (By.ID, 'field-timezone')
    _bio_field_locator = (By.ID, 'field-bio')
    _save_button_locator = (By.CSS_SELECTOR, '.button-bar button[type="submit"]')

    @property
    def alternative_name(self):
        return self.find_element(*self._alternative_name_field_locator).get_attribute()

    def add_first_name(self, first_name):
        first_name_input = self.find_element(*self._first_name_input_field_locator)
        first_name_input.clear()
        first_name_input.send_keys(first_name)

    def add_last_name(self, last_name):
        last_name_input = self.find_element(*self._last_name_input_field_locator)
        last_name_input.clear()
        last_name_input.send_keys(last_name)

    def add_gender_pronoun(self, gender_pronoun):
        gender_pronoun_field = self.find_element(*self._pronouns_field_locator)
        gender_pronoun_field.click()

    def add_alternative_name(self, alternative_name):
        alternative_name_input = self.find_element(*self._alternative_name_field_locator)
        alternative_name_input.clear()
        alternative_name_input.send_keys(alternative_name)

    def add_fun_job_title(self, fun_job__title):
        fun_job_title_input = self.find_element(*self._fun_job_title_field_locator)
        fun_job_title_input.clear()
        fun_job_title_input.send_keys(fun_job__title)

    def save_intro(self):
        self.find_element(*self._save_button_locator).click()
