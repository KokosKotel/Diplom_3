import allure
import pytest
import requests

from selenium import webdriver
from data import URLs, Ingredients
from helpers import PersonData
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    browser = None
    if request.param == 'chrome':
        browser = webdriver.Chrome()
    elif request.param == 'firefox':
        browser = webdriver.Firefox()
    browser.get(URLs.BASE_URL)
    yield browser
    browser.quit()


@pytest.fixture
@allure.title("Создает пользователя и удаляет его после теста")
def create_user():
    payload = PersonData.create_user()
    response = requests.post(URLs.CREATE_USER, data=payload)
    yield payload, response
    token = response.json()['accessToken']
    header = {'Authorization': token}
    requests.delete(URLs.DELETE_USER, headers=header)


@pytest.fixture
@allure.title("Авторизует пользователя")
def login_user(driver, create_user):
    user_data = create_user[0]
    login = LoginPage(driver)
    main = MainPage(driver)
    main.click_account_button()
    login.login(user_data['email'], user_data['password'])
    main.check_order_button_visible()


@pytest.fixture
@allure.title("Создает заказ")
def create_new_order(create_user):
    token = create_user[1].json()['accessToken']
    header = {"Authorization": token}
    ingredients = Ingredients.ingredients_data
    response = requests.post(URLs.CREATE_ORDER, headers=header, data=ingredients)
    return response.json()['order']['number']
