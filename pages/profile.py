from selenium.webdriver.common.by import By

from pages.base import Base
from pages.edit_accounts import EditAccounts
from pages.edit_profile import EditProfile
from pages.edit_languages import EditLanguages


class Profile(Base):
    _profile_picture_locator = (By.CSS_SELECTOR, '.user-picture.user-picture--large')
    _edit_profile_intro_button_locator = (By.CSS_SELECTOR, '.profile__intro .edit-button')
    _name_locator = (By.CSS_SELECTOR, '.profile__name h1')
    _alternative_name_locator = (By.CSS_SELECTOR, '.profile__alternative-name')
    _fun_job_title_locator = (By.CSS_SELECTOR, '.profile__fun-title')
    _save_confirmation_message_locator = (By.CSS_SELECTOR, '.toast__content')
    _pronoun_locator = (By.CSS_SELECTOR, '.profile__pronoun')
    _location_locator = (By.CSS_SELECTOR, '.profile__location')
    _username_locator = (By.CSS_SELECTOR, '.profile__user-name')
    _timezone_locator = (By.CSS_SELECTOR, '.profile__location div')
    _bio_locator = (By.CSS_SELECTOR, '.profile__description h2')
    _edit_accounts_button_locator = (By.CSS_SELECTOR, 'a[href="/e?section=accounts"]')
    _discourse_locator = (By.ID, 'field-account-0-username')
    _edit_languages_button_locator = (By.CSS_SELECTOR, 'a[href="/e?section=languages"]')

    @property
    def is_profile_picture_shown(self):
        return self.is_element_displayed(*self._profile_picture_locator)

    @property
    def name(self):
        return self.find_element(*self._name_locator).text

    @property
    def username(self):
        return self.find_element(*self._username_locator).text

    @property
    def alternative_name(self):
        return self.find_element(*self._alternative_name_locator).text

    @property
    def fun_job_title(self):
        return self.find_element(*self._fun_job_title_locator).text

    @property
    def gender_pronoun(self):
        return self.find_element(*self._pronoun_locator).text

    @property
    def location(self):
        return self.find_element(*self._location_locator).text

    @property
    def timezone(self):
        return self.find_element(*self._timezone_locator).text

    @property
    def bio(self):
        return self.find_element(*self._bio_locator).text

    def edit_profile_intro(self):
        self.find_element(*self._edit_profile_intro_button_locator).click()
        return EditProfile(self.selenium, self.base_url)

    def edit_accounts(self):
        self.find_element(*self._edit_accounts_button_locator).click()
        return EditAccounts(self.selenium, self.base_url)

    @property
    def discourse_account(self):
        return self.find_element(*self._discourse_locator).text

    def edit_languages(self):
        self.find_element(*self._edit_languages_button_locator).click()
        return EditLanguages(self.selenium, self.base_url)
