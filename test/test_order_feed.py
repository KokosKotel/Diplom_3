import allure

from helpers import Order
from locators import OrderFeedLocators
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Тест страницы Лента Заказов")
class TestOrderFeedPage:
    @allure.title("Окно деталей в ленте заказов")
    @allure.description("Тест проверяет отображение окна деталей в ленте заказов")
    def test_check_details(self, driver):
        main = MainPage(driver)
        feed = OrderFeedPage(driver)
        main.click_feed_button()
        feed.click_on_order()
        assert feed.check_order_info()

    @allure.title("Заказ пользователя в истории")
    @allure.description("Тест проверяет, что заказ пользователя отображается в истории заказов")
    def test_check_user_order_displayed_history(self, driver, create_user, create_new_order, login_user):
        order = Order()
        feed = OrderFeedPage(driver)
        main = MainPage(driver)
        main.click_feed_button()
        user_order = str(order.get_user_orders(create_user))
        history_of_orders = feed.get_history_orders()
        assert user_order in history_of_orders

    @allure.title("Счетчик Выполнено за все время")
    @allure.description("Тест проверяет, что счетчик увеличивается при создании заказа пользователем")
    def test_counter_updated_all_time(self, driver, create_user, login_user):
        order = Order()
        feed = OrderFeedPage(driver)
        main = MainPage(driver)
        main.click_feed_button()
        current_counter = int(feed.check_orders_counter(OrderFeedLocators.COUNTER_ORDERS_ALL_TIME))
        order.create_order(create_user)
        updated_counter = int(feed.check_orders_counter(OrderFeedLocators.COUNTER_ORDERS_ALL_TIME))
        assert updated_counter > current_counter

    @allure.title("Счетчик Выполнено за сегодня")
    @allure.description("Тест проверяет, что счетчик увеличивается при создании заказа пользователем")
    def test_counter_updated_today(self, driver, create_user, login_user):
        order = Order()
        feed = OrderFeedPage(driver)
        main = MainPage(driver)
        main.click_feed_button()
        current_counter = int(feed.check_orders_counter(OrderFeedLocators.COUNTER_ORDERS_TODAY))
        order.create_order(create_user)
        updated_counter = int(feed.check_orders_counter(OrderFeedLocators.COUNTER_ORDERS_TODAY))
        assert updated_counter > current_counter

    @allure.title("Заказ пользователя в работе")
    @allure.description("Тест проверяет, что заказ пользователя отображается В работе")
    def test_check_progress_order_user(self, driver, create_user, login_user):
        order = Order()
        main = MainPage(driver)
        feed = OrderFeedPage(driver)
        main.click_feed_button()
        order.create_order(create_user)
        orders_progress = feed.get_orders_progress()
        user_order = str(order.get_user_orders(create_user))
        assert user_order in orders_progress
