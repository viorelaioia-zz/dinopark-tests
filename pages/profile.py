from pages.base import Base


class Profile(Base):
    _profile_picture_locator = (By.CSS_SELECTOR, 'user-picture user-picture--large')

    @property
    def profile_picture(self):
        return self.is_element_displayed(*self._profile_picture_locator)
