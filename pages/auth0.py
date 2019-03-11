import pyotp
from pypom import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected


class Auth0(Page):
    _email_locator = (By.ID, 'field-email')
    _enter_email_button_locator = (By.ID, 'enter-initial')
    _enter_button_locator = (By.ID, 'authorise-ldap-credentials')
    _password_locator = (By.ID, 'field-password')
    _passcode_field_locator = (By.CSS_SELECTOR, '.passcode-label input[name="passcode"]')
    _login_form_locator = (By.ID, 'login-form')
    _enter_passcode_button = (By.CSS_SELECTOR, '.passcode-label .positive.auth-button')

    def enter_email(self, email):
        self.find_element(*self._email_locator).send_keys(email)
        self.find_element(*self._enter_email_button_locator).click()

    def enter_password(self, password):
        self.find_element(*self._password_locator).send_keys(password)
        self.find_element(*self._enter_button_locator).click()

    def enter_passcode(self, secret_seed):
        self.selenium.switch_to.frame('duo_iframe')
        self.wait.until(expected.visibility_of_element_located(self._login_form_locator))
        self.wait.until(expected.visibility_of_element_located(self._enter_passcode_button))
        self.find_element(*self._enter_passcode_button).click()
        passcode = pyotp.TOTP(secret_seed).now()
        self.find_element(*self._passcode_field_locator).send_keys(passcode)
        self.find_element(*self._enter_passcode_button).click()
        self.selenium.switch_to.default_content()
