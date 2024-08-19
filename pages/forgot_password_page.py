import allure

from .base_page import BasePage
from locators import ForgotPasswordPageLocators


class ForgotPasswordPage(BasePage):
    @allure.step("Проверка формы восстановления")
    def check_recovery_form(self):
        return self.check_element(ForgotPasswordPageLocators.TITLE_RECOVER)

    @allure.step("Заполнение поля email")
    def send_keys_email(self, email):
        self.send_keys(ForgotPasswordPageLocators.FIELD_EMAIL, email)

    @allure.step("Заполнения поля пароль")
    def send_keys_password(self, password):
        self.send_keys(ForgotPasswordPageLocators.FIELD_NEW_PASSWORD, password)

    @allure.step("Клик по кнопке Восстановить")
    def click_recovery_button(self):
        self.click_button(ForgotPasswordPageLocators.BUTTON_RECOVER)

    @allure.step("Проверка кнопки Сохранить")
    def check_save_button(self):
        return self.check_element(ForgotPasswordPageLocators.SAVE_BUTTON)

    @allure.step("Проверка, что поле пароль активно")
    def check_active_password(self, password):
        self.send_keys_password(password)
        self.click_button(ForgotPasswordPageLocators.SHOW_PASSWORD)
        return self.check_element(ForgotPasswordPageLocators.ACTIVE_PASSWORD_FIELD)
