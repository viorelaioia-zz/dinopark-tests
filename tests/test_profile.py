from pages.homepage import Homepage


class TestProfile():



    def test_check_username(self, selenium, base_url):
        homepage = Homepage(selenium, base_url).open()
        homepage.login("email", "pass", "secret_seed")
        assert homepage.is_user_picture_displayed()
