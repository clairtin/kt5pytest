from base_request import BaseRequest, User
from constants import BASE_URL_USER
import pprint
from pydantic import ValidationError

base_request_user = BaseRequest(BASE_URL_USER)

user_info_1 = base_request_user.get('1', expected_error=False)
pprint.pprint(user_info_1)

user_data = {'id': 1001, 'username': 'sasha_snow', 'email': 'sasha.snow@gmail.com'}
try:
    User(**user_data)
    user_created = base_request_user.post('', '', user_data)
    pprint.pprint(user_created)
except ValidationError as e:
    print(f"validation Error: {e}")

user_data_updated = {'id': 1, 'username': 'sasha_snow_updated', 'email': 'sasha.snow.updated@gmail.com'}
try:
    User(**user_data_updated)
    user_updated = base_request_user.put('1', '', user_data_updated)
    pprint.pprint(user_updated)
except ValidationError as e:
    print(f"validation Error: {e}")

user_deleted = base_request_user.delete('1', '')
pprint.pprint(user_deleted)
