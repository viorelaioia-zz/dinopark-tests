from selenium.webdriver.common.by import By

from pages.base import Base
from pages.edit_profile import EditProfile


class Profile(Base):
    _profile_picture_locator = (By.CSS_SELECTOR, '.user-picture.user-picture--large')
    _edit_profile_intro_button_locator =  (By.CSS_SELECTOR, '.profile__intro .edit-button')
    _name_locator = (By.CSS_SELECTOR, '.profile__name h1')
    _alternative_name_locator = (By.CSS_SELECTOR, '.profile__alternative-name')
    _fun_job_title_locator = (By.CSS_SELECTOR, '.profile__fun-title')
    _save_confirmation_message_locator = (By.CSS_SELECTOR, '.toast__content')

    @property
    def is_profile_picture_shown(self):
        return self.is_element_displayed(*self._profile_picture_locator)

    @property
    def name(self):
        return self.find_element(*self._name_locator).text

    @property
    def alternative_name(self):
        return self.find_element(*self._alternative_name_locator).text

    @property
    def fun_job_title(self):
        return self.find_element(*self._fun_job_title_locator).text

    def edit_profile_intro(self):
        self.find_element(*self._edit_profile_intro_button_locator).click()
        return EditProfile(self.selenium, self.base_url)
