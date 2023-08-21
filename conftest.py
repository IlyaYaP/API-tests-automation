import pytest
import requests
import allure

class ApiClients:
    def __init__(self, base_url):
        self.base_url = base_url
    
    def get(self, path='/', params=None, headers=None):
        url = f"{self.base_url}{path}"
        return requests.get(url=url, params=params, headers=headers)
    
    def post(self, path='/', params=None, data=None, json=None, headers=None):
        url = f"{self.base_url}{path}"
        return requests.post(url=url, params=params, data=data, json=json, headers=headers)