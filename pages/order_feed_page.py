import allure

from .base_page import BasePage
from locators import OrderFeedLocators


class OrderFeedPage(BasePage):
    @allure.step("Клик по заказу в ленте")
    def click_on_order(self):
        self.click_after_wait(OrderFeedLocators.ORDER_WINDOW)

    @allure.step("Проверяем отображение окна заказов")
    def check_order_info(self):
        return self.check_element(OrderFeedLocators.INFO_ORDER)

    @allure.step("Получить количество заказов Выполнено за все время")
    def check_orders_counter_all_time(self):
        return self.get_text_locator(OrderFeedLocators.COUNTER_ORDERS_ALL_TIME)

    @allure.step("Получить количество заказов Выполнено за сегодня")
    def check_orders_counter_today(self):
        return self.get_text_locator(OrderFeedLocators.COUNTER_ORDERS_TODAY)

    @allure.step("получаем номер заказа")
    def get_history_orders(self):
        numbers = self.get_text_element(OrderFeedLocators.ORDER_HISTORY)
        orders_list = []
        for number in numbers:
            order_number = number.text[2:]
            orders_list.append(order_number)
        return orders_list

    @allure.step("Получаем заказы В работе")
    def get_orders_progress(self):
        numbers = self.get_text_element(OrderFeedLocators.COUNTER_ORDERS_PROGRESS)
        orders_list = []
        for number in numbers:
            order_number = number.text[1:]
            orders_list.append(order_number)
        return orders_list
