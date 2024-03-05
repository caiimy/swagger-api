# swagger_client.PlayersApi

All URIs are relative to *https://matchmaking.braymatter.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**players_names_name_get**](PlayersApi.md#players_names_name_get) | **GET** /players/names/{name} | Checks if a player name is available

# **players_names_name_get**
> players_names_name_get(name)

Checks if a player name is available

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PlayersApi()
name = 'name_example' # str | 

try:
    # Checks if a player name is available
    api_instance.players_names_name_get(name)
except ApiException as e:
    print("Exception when calling PlayersApi->players_names_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

