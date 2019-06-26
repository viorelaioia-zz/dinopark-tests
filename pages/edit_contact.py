from selenium.webdriver.common.by import By

from pages.base import Base


class EditContact(Base):
    _add_phone_button_locator = (By.CSS_SELECTOR, 'button[class*="edit-contact__add-more"]')
    _phone_type_dropdown_locator = (By.CSS_SELECTOR, 'button[aria-controls="option-list-field-phone-0-type"]')
    _phone_types_list_locator = (By.CSS_SELECTOR, '#option-list-field-phone-0-type label span')
    _phone_number_field_locator = (By.ID, 'field-phone-0-value')
    _save_button_locator = (By.CSS_SELECTOR, '.button-bar button[type="submit"]')

    def click_add_phone(self):
        self.find_element(*self._add_phone_button_locator).click()

    def select_phone_type(self, phone_type):
        self.find_element(*self._phone_type_dropdown_locator).click()
        for type in self.find_elements(*self._phone_types_list_locator):
            if type.text == phone_type:
                type.click()
                break

    def enter_phone_number(self, phone_number):
        self.find_element(*self._phone_number_field_locator).send_keys(phone_number)

    def save_contact_section(self):
        self.find_element(*self._save_button_locator).click()
