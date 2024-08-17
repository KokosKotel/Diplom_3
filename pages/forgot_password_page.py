import allure

from .base_page import BasePage
from locators import RecoverAndResetPageLocators


class ForgotPasswordPage(BasePage):
    @allure.step("Проверка формы восстановления")
    def check_recovery_form(self):
        return self.check_element(RecoverAndResetPageLocators.TITLE_RECOVER)

    @allure.step("Заполнение поля email")
    def send_keys_email(self, email):
        self.send_keys(RecoverAndResetPageLocators.FIELD_EMAIL, email)

    @allure.step("Заполнения поля пароль")
    def send_keys_password(self, password):
        self.send_keys(RecoverAndResetPageLocators.FIELD_NEW_PASSWORD, password)

    @allure.step("Клик по кнопке Восстановить")
    def click_recovery_button(self):
        self.click_button(RecoverAndResetPageLocators.BUTTON_RECOVER)

    @allure.step("Проверка кнопки Сохранить")
    def check_save_button(self):
        return self.check_element(RecoverAndResetPageLocators.SAVE_BUTTON)

    @allure.step("Проверка, что поле пароль активно")
    def check_active_password(self, password):
        self.send_keys_password(password)
        self.click_button(RecoverAndResetPageLocators.SHOW_PASSWORD)
        return self.check_element(RecoverAndResetPageLocators.ACTIVE_PASSWORD_FIELD)
