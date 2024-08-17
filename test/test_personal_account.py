import allure

from data import URLs
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage


@allure.feature("Тест страницы Личный кабинет")
class TestPersonalProfilePage:
    @allure.title("Переход в Личный Кабинет")
    @allure.description("Тест проверяет переход в личный кабинет")
    def test_switching_account(self, driver, create_user, login_user):
        main = MainPage(driver)
        account = PersonalAccountPage(driver)
        main.click_account_button()
        assert account.check_account_form()
        assert account.get_current_url() == URLs.URL_ACCOUNT

    @allure.title("Переход в историю заказов пользователя")
    @allure.description("Тест проверяет переход в историю заказов пользователя")
    def test_switching_order_history(self, driver, create_user, login_user):
        main = MainPage(driver)
        account = PersonalAccountPage(driver)
        main.click_account_button()
        account.click_history_button()
        assert account.check_history_form()
        assert account.get_current_url() == URLs.URL_HISTORY

    @allure.title("Выход из аккаунта")
    @allure.description("Тест проверяет выход из аккаунта")
    def test_logout_account(self, driver, create_user, login_user):
        main = MainPage(driver)
        login = LoginPage(driver)
        account = PersonalAccountPage(driver)
        main.click_account_button()
        account.click_logout_button()
        assert login.check_auth_form()
        assert login.get_current_url() == URLs.URL_LOGIN
