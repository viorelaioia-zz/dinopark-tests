from pypom import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected

from pages.auth0 import Auth0


class Base(Page):

    _user_menu_locator = (By.CSS_SELECTOR, '.show-more__button.top-bar__user-menu-toggle')
    _my_profile_menu_locator = (By.CSS_SELECTOR, '.user-menu__items a[href="/beta/p/fiji"]')

    def __init__(self, selenium, base_url, locale='en-US', **url_kwargs):
        super(Base, self).__init__(selenium, base_url, locale=locale, **url_kwargs)

    def login(self, email, password, secret_seed):
        auth0 = Auth0(self.selenium, self.base_url)
        auth0.enter_email(email)
        auth0.enter_password(password)
        auth0.enter_passcode(secret_seed)

    def go_to_my_profile(self):
        self.wait.until(expected.visibility_of_element_located(self._user_menu_locator))
        self.find_element(*self._user_menu_locator).click()
        self.wait.until(expected.visibility_of_element_located(self._my_profile_menu_locator))
        self.find_element(*self._my_profile_menu_locator).click()
        from pages.profile import Profile
        return Profile(self.selenium, self.base_url)
