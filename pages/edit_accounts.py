from selenium.webdriver.common.by import By

from pages.base import Base


class EditAccounts(Base):

    _discourse_account_field_locator = (By.ID, 'field-account-0-username')
    _save_button_locator = (By.CSS_SELECTOR, '.button-bar button[type="submit"]')
    _add_accounts_button_locator = (By.CSS_SELECTOR, '.button[class*="edit-accounts__add-more"]')

    def click_add_accounts (self):
        self.find_element(*self._add_accounts_button_locator).click()

    def add_account_value(self, discourse_account):
        account_input = self.find_element(*self._discourse_account_field_locator)
        account_input.clear()
        account_input.send_keys(discourse_account)

    def save_accounts(self):
        self.find_element(*self._save_button_locator).click()
