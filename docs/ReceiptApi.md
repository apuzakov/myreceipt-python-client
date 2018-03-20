# swagger_client.ReceiptApi

All URIs are relative to *https://api.myreceipt.tk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**receipt_compose**](ReceiptApi.md#receipt_compose) | **POST** /receipt/compose | Пробитие чека


# **receipt_compose**
> ReceiptResponse receipt_compose(request)

Пробитие чека



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ReceiptApi(swagger_client.ApiClient(configuration))
request = swagger_client.ReceiptRequest() # ReceiptRequest | Полная информация о чеке

try:
    # Пробитие чека
    api_response = api_instance.receipt_compose(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptApi->receipt_compose: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ReceiptRequest**](ReceiptRequest.md)| Полная информация о чеке | 

### Return type

[**ReceiptResponse**](ReceiptResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

