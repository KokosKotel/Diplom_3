import allure

from .base_page import BasePage
from locators import MainPageLocators, HeaderLocators


class MainPage(BasePage):
    @allure.step("Клик по кнопке Конструктор")
    def click_construction_button(self):
        self.click_button(HeaderLocators.CONSTRUCT_BUTTON)

    @allure.step("Клик по кнопке Лента Заказов")
    def click_feed_button(self):
        self.click_button(HeaderLocators.FEED_BUTTON)

    @allure.step("Клик по кнопке Личный Кабинет")
    def click_account_button(self):
        self.click_button(HeaderLocators.ACCOUNT_BUTTON)

    @allure.step("Проверка формы конструктора")
    def check_constructor_form(self):
        return self.check_element(MainPageLocators.CONSTRUCT_FORM)

    @allure.step("Проверка формы лента заказов")
    def check_order_feed_form(self):
        return self.check_element(MainPageLocators.FEED_FORM)

    @allure.step("Клик по кнопке Войти в аккаунт")
    def click_button_account_main(self):
        self.click_button(MainPageLocators.LOGIN_ACCOUNT_BUTTON)

    @allure.step("Клик по ингредиенту")
    def click_ingredient(self):
        self.click_button(MainPageLocators.INGREDIENT_BUN)

    @allure.step("Проверяем появление Детали ингредиента")
    def check_details(self):
        return self.check_element(MainPageLocators.POPUP_FORM_DETAILS)

    @allure.step("Закрытие Деталей ингредиента")
    def close_info_popup(self):
        self.click_button(MainPageLocators.CLOSE_DETAILS_BUTTON)

    @allure.step("Проверяем закрытие Деталей ингредиента")
    def check_close_details(self):
        return self.check_element_not_visible(MainPageLocators.POPUP_FORM_DETAILS)

    @allure.step("Проверяем отображение кнопки Оформить заказ")
    def check_order_button_visible(self):
        self.wait_element(MainPageLocators.ORDER_BUTTON)

    @allure.step("Проверяем отображение формы заказа")
    def check_order_form(self):
        return self.check_element(MainPageLocators.ORDER_FORM)

    @allure.step("Добавляем булку в корзину")
    def bun_add_basket(self):
        self.drag_drop(MainPageLocators.INGREDIENT_BUN, MainPageLocators.BASKET)

    @allure.step("Клик по кнопке Оформить заказ")
    def click_order_button(self):
        self.click_button(MainPageLocators.ORDER_BUTTON)

    @allure.step("Создаем заказ")
    def create_order(self):
        self.bun_add_basket()
        self.click_order_button()

    @allure.step("Получаем счетчик количества ингредиентов")
    def get_counter_ingredients(self):
        self.wait_element(MainPageLocators.COUNTER_INGREDIENT)
        return self.get_text_locator(MainPageLocators.COUNTER_INGREDIENT)
