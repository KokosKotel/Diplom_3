import allure

from .base_page import BasePage
from locators import PersonalAccountLocators


class PersonalAccountPage(BasePage):
    @allure.step("Проверяем форму личного кабинета")
    def check_account_form(self):
        return self.check_element(PersonalAccountLocators.ACCOUNT_FORM)

    @allure.step("Клик по кнопке История заказов")
    def click_history_button(self):
        self.click_button(PersonalAccountLocators.BUTTON_HISTORY_ORDER)

    @allure.step("Проверяем форму истории")
    def check_history_form(self):
        return self.check_element(PersonalAccountLocators.FORM_HISTORY_FORM)

    @allure.step("Клик по кнопке Выход")
    def click_logout_button(self):
        self.click_button(PersonalAccountLocators.BUTTON_LOGOUT)
