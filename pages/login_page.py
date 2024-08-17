import allure

from .base_page import BasePage
from locators import LoginPageLocators


class LoginPage(BasePage):
    @allure.step("Проверка формы входа")
    def check_auth_form(self):
        return self.check_element(LoginPageLocators.AUTH_FORM)

    @allure.step("Клик по кнопке Восстановить пароль")
    def click_recovery_button(self):
        self.click_button(LoginPageLocators.RECOVER_BUTTON)

    @allure.step("Заполнить поле email")
    def send_keys_email(self, email):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)

    @allure.step("Заполнить поле пароль")
    def send_keys_password(self, password):
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step("Клик по кнопке Войти")
    def click_button_login(self):
        self.click_button(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Авторизация пользователя")
    def login(self, email, password):
        self.send_keys_email(email)
        self.send_keys_password(password)
        self.click_button_login()
