import allure

from data import URLs
from helpers import PersonData
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.feature("Тест страницы Восстановление пароля")
class TestForgotPasswordPage:
    @allure.title("Форма Восстановить пароль")
    @allure.description("Тест проверяет, что форма Восстановить пароль отображается")
    def test_forgot_password(self, driver):
        main = MainPage(driver)
        login = LoginPage(driver)
        recovery = ForgotPasswordPage(driver)
        main.click_button_account_main()
        login.click_recovery_button()
        assert recovery.check_recovery_form()
        assert recovery.get_current_url() == URLs.URL_FORGOT_PASSWORD

    @allure.title("Форма Восстановления пароля")
    @allure.description("Тест проверяет, что при клике по кнопке Восстановить,"
                        "переходит на форму Восстановления пароля")
    def test_click_recover_button(self, driver):
        main = MainPage(driver)
        login = LoginPage(driver)
        recovery = ForgotPasswordPage(driver)
        user = PersonData().create_user()
        main.click_button_account_main()
        login.click_recovery_button()
        recovery.send_keys_email(user.get('email'))
        recovery.click_recovery_button()
        assert recovery.check_save_button()
        assert recovery.get_current_url() == URLs.URL_RESET_PASSWORD

    @allure.title("Поле Пароль")
    @allure.description("Тест проверяет, что поле пароль активно при клике на кнопку Показать пароль")
    def test_check_active_password_field(self, driver):
        main = MainPage(driver)
        login = LoginPage(driver)
        recovery = ForgotPasswordPage(driver)
        user = PersonData().create_user()
        main.click_button_account_main()
        login.click_recovery_button()
        recovery.send_keys_email(user.get('email'))
        recovery.click_recovery_button()
        assert recovery.check_active_password(user.get('password'))
