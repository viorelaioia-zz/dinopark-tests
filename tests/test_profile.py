import pytest
from pages.homepage import Homepage


class TestProfile():

    @pytest.mark.nondestructive
    def test_login(self, selenium, base_url):
        homepage = Homepage(selenium, base_url).open()
        homepage.login("email", "password", "secret_seed")
        assert homepage.is_user_picture_displayed

    @pytest.mark.nondestructive
    def test_edit_first_name(self, selenium, base_url):
        homepage = Homepage(selenium, base_url).open()
        profile = homepage.go_to_my_profile()
        assert profile.is_profile_picture_shown
        initial_name = profile.name
        profile.edit_profile_intro()
        profile.add_first_name("Test")
        profile.save_intro()
        assert initial_name != profile.name
