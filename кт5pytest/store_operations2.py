from base_request import BaseRequest, Order
from constants import BASE_URL_STORE
import pprint
from pydantic import ValidationError

base_request_store = BaseRequest(BASE_URL_STORE)

order_info_1 = base_request_store.get('1', expected_error=False)
pprint.pprint(order_info_1)

order_data = {'id': 1001, 'item': 'item123', 'quantity': 3}
try:
    Order(**order_data)
    order_created = base_request_store.post('', 'new', order_data)
    pprint.pprint(order_created)
except ValidationError as e:
    print(f"validation Error: {e}")

order_data_updated = {'id': 1, 'item': 'item123_updated', 'quantity': 5}
try:
    Order(**order_data_updated)
    order_updated = base_request_store.put('1', '', order_data_updated)
    pprint.pprint(order_updated)
except ValidationError as e:
    print(f"validation Error: {e}")

order_deleted = base_request_store.delete('1', '')
pprint.pprint(order_deleted)
