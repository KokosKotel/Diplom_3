import allure

from data import URLs
from pages.main_page import MainPage


@allure.feature("Тест главной страницы")
class TestMainPage:
    @allure.title("Переход к Конструктору")
    @allure.description("Тест проверяет переход к форме конструктора бургеров")
    def test_switching_constructor(self, driver):
        main = MainPage(driver)
        main.click_button_account_main()
        main.click_construction_button()
        assert main.check_constructor_form()
        assert main.get_current_url() == URLs.BASE_URL

    @allure.title("Переход к Ленте Заказов")
    @allure.description("Тест проверяет переход к форме ленты заказов")
    def test_switching_order_feed(self, driver):
        main = MainPage(driver)
        main.click_feed_button()
        assert main.check_order_feed_form()
        assert main.get_current_url() == URLs.URL_FEED

    @allure.title("Детали ингредиента")
    @allure.description("Тест проверяет отображение окна Детали ингредиента")
    def test_check_details(self, driver):
        main = MainPage(driver)
        main.click_ingredient()
        assert main.check_details()

    @allure.title("Закрытие Деталей ингредиента")
    @allure.description("Тест проверяет закрытие окна Деталей ингредиента")
    def test_check_close_details(self, driver):
        main = MainPage(driver)
        main.click_ingredient()
        main.close_info_popup()
        assert main.check_close_details()

    @allure.title("Счетчик ингредиентов")
    @allure.description("Тест проверяет, что счетчик ингредиентов увеличивается")
    def test_increases_counter(self, driver):
        main = MainPage(driver)
        main.bun_add_basket()
        assert int(main.get_counter_ingredients()) > 0

    @allure.title("Создание заказа авторизованным пользователем")
    @allure.description("Тест проверяет успешное создание заказа")
    def test_create_order_login_user(self, driver, create_user, login_user):
        main = MainPage(driver)
        main.click_construction_button()
        main.create_order()
        assert main.check_order_form()
