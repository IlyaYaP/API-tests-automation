import pytest
import requests
import allure


class ApiClients:
    def __init__(self, base_url) -> None:
        self.base_url = base_url

    def get(self, path='/', params=None, headers=None):
        url = f"{self.base_url}{path}"
        return requests.get(url=url, params=params, headers=headers)

    def post(self, path='/', params=None, data=None, json=None, headers=None):
        try:
            url = f"{self.base_url}{path}"
            return requests.post(url=url, params=params, data=data, json=json, headers=headers)
        except requests.exceptions.ConnectionError:
            print("Connection refused")
    


class ResponseValidate:
    def __init__(self, response) -> None:
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate(self, schema):
        with allure.step('Проверка данных ответа.'):
            if isinstance(self.response_json, list):
                for item in self.response_json:
                    schema.model_validate(item)
            else:
                schema.model_validate(self.response_json)

    def assert_status_code(self, status_code):
        with allure.step(f'Проверка статус-код ответа. Ожидаем {status_code}'):
            if isinstance(status_code, list):
                assert self.response_status in status_code, f'Статус код {self.response_status}'
            else:
                assert self.response_status == status_code, f'Статус код {self.response_status}'



@pytest.fixture
def booker_api():
    return ApiClients(base_url="https://restful-booker.herokuapp.com")