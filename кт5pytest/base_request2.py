import requests
import pprint
from pydantic import BaseModel
import allure

class BaseRequest:
    def __init__(self, base_url):
        self.base_url = base_url

    def _request(self, url, request_type, data=None, expected_error=False):
        stop_flag = False
        while not stop_flag:
            if request_type == 'GET':
                response = requests.get(url)
            elif request_type == 'POST':
                response = requests.post(url, json=data)
            elif request_type == 'PUT':
                response = requests.put(url, json=data)
            else:
                response = requests.delete(url)

            if not expected_error and response.status_code == 200:
                stop_flag = True
            elif expected_error:
                stop_flag = True

            # log
            self.log_request(response, request_type)
            return response

    def log_request(self, response, request_type):
        allure.attach(f"{request_type} example", name="Request type", attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.url, name="URL", attachment_type=allure.attachment_type.TEXT)
        allure.attach(str(response.status_code), name="Status Code", attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.reason, name="Reason", attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.text, name="Response Text", attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.json(), name="Response JSON", attachment_type=allure.attachment_type.JSON)

    @allure.step("GET request")
    def get(self, endpoint, endpoint_id, expected_error=False):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'GET', expected_error=expected_error)
        return response.json()

    @allure.step("POST request")
    def post(self, endpoint, endpoint_id, body):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'POST', data=body)
        return response.json()['message']

    @allure.step("PUT request")
    def put(self, endpoint, endpoint_id, body):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'PUT', data=body)
        return response.json()['message']

    @allure.step("DELETE request")
    def delete(self, endpoint, endpoint_id):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'DELETE')
        return response.json()['message']

class User(BaseModel):
    id: int
    username: str
    email: str

class Order(BaseModel):
    id: int
    item: str
    quantity: int
