from selenium.webdriver.common.by import By

from pages.base import Base


class Homepage(Base):
    _user_picture_locator = (By.CSS_SELECTOR, '.user-picture.user-picture--small')

    @property
    def is_user_picture_displayed(self):
        return self.is_element_displayed(*self._user_picture_locator)
