# -*- coding: utf-8 -*-

from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: token
# Configuration.api_key = ''
swagger_client.configuration.api_key = {'X-Auth-Token': 'YOUR_API_KEY'}
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# create an instance of the API class
api_instance = swagger_client.ReceiptApi()
request = swagger_client.ReceiptRequest()
# ReceiptRequest | Полная информация о чеке

try:
    # Пробитие чека
    api_response = api_instance.receipt_compose(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptApi->receipt_compose: %s\n" % e)