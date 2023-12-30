import unittest
from base_request import BaseRequest
from constants import BASE_URL_USER, BASE_URL_STORE
from user_operations import base_request_user
from store_operations import base_request_store
import pprint
import allure

class TestAPIRequests(unittest.TestCase):
    @allure.feature("User Operations")
    def test_user_operations(self):
        with allure.step("Get user information"):
            user_info_1 = base_request_user.get('1', expected_error=False)
            pprint.pprint(user_info_1)
            self.assertIsNotNone(user_info_1)

        with allure.step("Create a new user"):
            user_data = {'id': 1001, 'username': 'john_doe', 'email': 'john.doe@example.com'}
            try:
                User(**user_data)
                user_created = base_request_user.post('', '', user_data)
                pprint.pprint(user_created)
            except ValidationError as e:
                print(f"validation Error: {e}")
            self.assertIsNotNone(user_created)

        with allure.step("Update user information"):
            user_data_updated = {'id': 1, 'username': 'john_doe_updated', 'email': 'john.doe.updated@example.com'}
            try:
                User(**user_data_updated)
                user_updated = base_request_user.put('1', '', user_data_updated)
                pprint.pprint(user_updated)
            except ValidationError as e:
                print(f"validation Error: {e}")
            self.assertIsNotNone(user_updated)

        with allure.step("Delete user"):
            user_deleted = base_request_user.delete('1', '')
            pprint.pprint(user_deleted)
            self.assertIsNotNone(user_deleted)

    @allure.feature("Store Operations")
    def test_store_operations(self):
        with allure.step("Get order information"):
            order_info_1 = base_request_store.get('1', expected_error=False)
            pprint.pprint(order_info_1)
            self.assertIsNotNone(order_info_1)

        with allure.step("Create a new order"):
            order_data = {'id': 1001, 'item': 'item123', 'quantity': 3}
            try:
                Order(**order_data)
                order_created = base_request_store.post('', 'new', order_data)
                pprint.pprint(order_created)
            except ValidationError as e:
                print(f"Validation Error: {e}")
            self.assertIsNotNone(order_created)

        with allure.step("Update order information"):
            order_data_updated = {'id': 1, 'item': 'item123_updated', 'quantity': 5}
            try:
                Order(**order_data_updated)
                order_updated = base_request_store.put('1', '', order_data_updated)
                pprint.pprint(order_updated)
            except ValidationError as e:
                print(f"Validation Error: {e}")
            self.assertIsNotNone(order_updated)

        with allure.step("Delete order"):
            order_deleted = base_request_store.delete('1', '')
            pprint.pprint(order_deleted)
            self.assertIsNotNone(order_deleted)

if __name__ == '__main__':
    unittest.main()
