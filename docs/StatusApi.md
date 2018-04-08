# swagger_client.StatusApi

All URIs are relative to *https://api.check-sender.ru*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_status**](StatusApi.md#device_status) | **GET** /status/device/{id} | Полная информация об устройстве


# **device_status**
> DeviceStatusResponse device_status(id)

Полная информация об устройстве



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
api_instance = swagger_client.StatusApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Уникальный ID устройства (ККТ)

try:
    # Полная информация об устройстве
    api_response = api_instance.device_status(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusApi->device_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Уникальный ID устройства (ККТ) | 

### Return type

[**DeviceStatusResponse**](DeviceStatusResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

