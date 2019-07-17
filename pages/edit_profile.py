from selenium.webdriver.common.by import By

from pages.base import Base


class EditProfile(Base):
    _first_name_input_field_locator = (By.ID, 'field-first-name')
    _last_name_input_field_locator = (By.ID, 'field-last-name')
    _pronouns_field_locator = (By.ID, 'field-pronouns')
    _pronoun_options_locator = (By.CSS_SELECTOR, '.combobox__options.open .combobox__option')
    _alternative_name_field_locator = (By.ID, 'field-alt-name')
    _fun_job_title_field_locator = (By.ID, 'field-fun-job-title')
    _location_field_locator = (By.ID, 'field-location')
    _timezone_field_locator = (By.ID, 'field-timezone')
    _timezone_options_locator = (By.CSS_SELECTOR, '.combobox__options.open .combobox__option')
    _bio_field_locator = (By.ID, 'field-bio')
    _save_button_locator = (By.CSS_SELECTOR, '.button-bar button[type="submit"]')
    _first_name_privacy_locator = (By.CSS_SELECTOR, 'button[aria-controls="option-list-field-first-name-privacy"]')
    _first_name_privacy_options_locator = (By.CSS_SELECTOR, '#option-list-field-first-name-privacy label')

    @property
    def alternative_name(self):
        return self.find_element(*self._alternative_name_field_locator).get_attribute()

    @property
    def first_name_privacy(self):
        return self.find_element(*self._first_name_privacy_locator).get_attribute('title')

    def add_first_name(self, first_name):
        first_name_input = self.find_element(*self._first_name_input_field_locator)
        first_name_input.clear()
        first_name_input.send_keys(first_name)

    def add_last_name(self, last_name):
        last_name_input = self.find_element(*self._last_name_input_field_locator)
        last_name_input.clear()
        last_name_input.send_keys(last_name)

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

    def click_first_name_privacy(self):
        self.find_element(*self._first_name_input_field_locator)

    def set_privacy_for_first_name(self, privacy):
        self.find_element(*self._first_name_privacy_locator).click()
        [option.click() for option in
         self.find_elements(*self._first_name_privacy_options_locator) if option.text == privacy]

    def select_gender_pronoun(self, gender_pronoun):
        gender_pronoun_field = self.find_element(*self._pronouns_field_locator)
        gender_pronoun_field.click()
        gender_pronoun_field.clear()
        gender_pronoun_field.send_keys(gender_pronoun)
        gender_options = self.find_elements(*self._pronoun_options_locator)
        for option in gender_options:
            if option.text == gender_pronoun:
                option.click()

    def delete_gender_pronoun(self):
        gender_pronoun_field = self.find_element(*self._pronouns_field_locator)
        gender_pronoun_field.click()
        gender_pronoun_field.clear()

    def select_timezone(self, timezone):
        timezone_field = self.find_element(*self._timezone_field_locator)
        timezone_field.click()
        timezone_field.clear()
        timezone_field.send_keys(timezone)
        timezone_options = self.find_elements(*self._timezone_options_locator)
        for option in timezone_options:
            if option.text == timezone:
                option.click()

    def delete_timezone(self):
        timezone_field = self.find_element(*self._timezone_field_locator)
        timezone_field.click()
        timezone_field.clear()

    def add_location(self, location):
        location_input = self.find_element(*self._location_field_locator)
        location_input.clear()
        location_input.send_keys(location)

    def add_timezone(self, timezone):
        timezone_input = self.find_element(*self._timezone_field_locator)
        timezone_input.clear()
        timezone_input.send_keys(timezone)

    def add_bio(self, bio):
        bio_input = self.find_element(*self._bio_field_locator)
        bio_input.clear()
        bio_input.send_keys(bio)
