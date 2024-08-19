import allure
import requests
from faker import Faker
from data import Ingredients, URLs


class PersonData:
    @staticmethod
    def create_user():
        faker = Faker()
        data = {
            'email': faker.email(),
            'password': faker.password(),
            'name': faker.first_name()
        }
        return data


class Order:
    @allure.step("Создает заказ")
    def create_order(self, create_user):
        token = create_user[1].json()['accessToken']
        header = {'Authorization': token}
        ingredients = Ingredients.ingredients_data
        requests.post(URLs.CREATE_ORDER, headers=header, data=ingredients)

    @allure.step("Получение заказов пользователя")
    def get_user_orders(self, create_user):
        token = create_user[1].json()['accessToken']
        header = {'Authorization': token}
        response = requests.get(URLs.GET_ORDERS, headers=header)
        return response.json()['orders'][0]['number']
