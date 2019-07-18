import pytest
from pages.homepage import Homepage


class TestProfile():

    @pytest.mark.nondestructive
    def test_edit_first_name(self, selenium, base_url):
        homepage = Homepage(selenium, base_url).open()
        homepage.login("email", "password", "secret_seed")
        assert homepage.is_user_picture_displayed
        profile = homepage.go_to_my_profile()
        assert profile.is_profile_picture_shown
        initial_name = profile.name
        edit_profile = profile.edit_profile_intro()
        edit_profile.add_first_name("Test")
        edit_profile.save_intro()
        assert initial_name != profile.name

    @pytest.mark.nondestructive
    def test_edit_last_name(self, selenium, base_url):
        homepage = Homepage(selenium, base_url).open()
        homepage.login("email", "password", "secret_seed")
        profile = homepage.go_to_my_profile()
        assert profile.is_profile_picture_shown
        initial_last_name = profile.name
        edit_profile = profile.edit_profile_intro()
        edit_profile.add_last_name("Test")
        edit_profile.save_intro()
        assert initial_last_name != profile.name

    @pytest.mark.nondestructive
    def test_select_gender_pronoun(self, selenium, base_url):
        homepage = Homepage(selenium, base_url).open()
        homepage.login("email", "password", "secret_seed")
        profile = homepage.go_to_my_profile()
        assert profile.is_profile_picture_shown
        profile.edit_profile_intro()
        profile.add_gender_pronoun("Test")
        profile.save_intro()

    @pytest.mark.nondestructive
    def test_edit_alternative_name(self, selenium, base_url):
        homepage = Homepage(selenium, base_url).open()
        homepage.login("email", "password", "secret_seed")
        profile = homepage.go_to_my_profile()
        assert profile.is_profile_picture_shown
        initial_alternative_name = profile.alternative_name
        edit_profile = profile.edit_profile_intro()
        edit_profile.add_alternative_name("super 88 bau")
        edit_profile.save_intro()
        assert initial_alternative_name != profile.alternative_name

    @pytest.mark.nondestructive
    def test_edit_fun_job_title(self, selenium, base_url):
        homepage = Homepage(selenium, base_url).open()
        homepage.login("email", "password", "secret_seed")
        profile = homepage.go_to_my_profile()
        assert profile.is_profile_picture_shown
        initial_fun_job_title = profile.fun_job_title
        edit_profile = profile.edit_profile_intro()
        edit_profile.add_fun_job_title("make fun of bugs")
        edit_profile.save_intro()
        assert initial_fun_job_title != profile.fun_job_title

    @pytest.mark.nondestructive
    def test_change_privacy_for_first_name(self, selenium, base_url):
        homepage = Homepage(selenium, base_url).open()
        homepage.login("email", "password", "secret_seed")
        profile = homepage.go_to_my_profile()
        assert profile.is_profile_picture_shown
        edit_profile = profile.edit_profile_intro()
        initial_privacy = edit_profile.first_name_privacy
        edit_profile.set_privacy_for_first_name("Public")
        edit_profile.save_intro()
        assert edit_profile.first_name_privacy != initial_privacy

    @pytest.mark.nondestructive
    def test_select_timezone(self, selenium, base_url):
        homepage = Homepage(selenium, base_url).open()
        homepage.login("email", "password", "secret_seed")
        profile = homepage.go_to_my_profile()
        assert profile.is_profile_picture_shown
        edit_profile = profile.edit_profile_intro()
        timezone = "Europe/Bucharest"
        edit_profile.select_timezone(timezone)
        edit_profile.save_intro()
        assert profile.timezone == timezone
        edit_profile = profile.edit_profile_intro()
        edit_profile.delete_timezone()
        edit_profile.save_intro()

    @pytest.mark.nondestructive
    def test_edit_accounts(self, selenium, base_url):
        homepage = Homepage(selenium, base_url).open()
        homepage.login("email", "password", "secret_seed")
        profile = homepage.go_to_my_profile()
        assert profile.is_profile_picture_shown
        edit_accounts = profile.edit_accounts()
        edit_accounts.click_add_accounts()
        edit_accounts.add_account_value("testing")
        edit_accounts.save_accounts()

    @pytest.mark.nondestructive
    def test_edit_languages(self, selenium, base_url):
        homepage = Homepage(selenium, base_url).open()
        homepage.login("email", "password", "secret_seed")
        profile = homepage.go_to_my_profile()
        assert profile.is_profile_picture_shown
        edit_languages = profile.edit_languages()
        edit_languages.click_add_languages()
        edit_languages.add_language_value("french")
        edit_languages.click_submit_button()
        edit_languages.save_languages()
