# swagger_client.NetworkApi

All URIs are relative to *https://matchmaking.braymatter.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**network_ip_v4_get**](NetworkApi.md#network_ip_v4_get) | **GET** /network/ip/v4 | Sends a plaintext representation of the callers ipv4 address
[**network_ip_v6_get**](NetworkApi.md#network_ip_v6_get) | **GET** /network/ip/v6 | Sends a plaintext representation of the callers ipv6 address

# **network_ip_v4_get**
> network_ip_v4_get()

Sends a plaintext representation of the callers ipv4 address

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetworkApi()

try:
    # Sends a plaintext representation of the callers ipv4 address
    api_instance.network_ip_v4_get()
except ApiException as e:
    print("Exception when calling NetworkApi->network_ip_v4_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_ip_v6_get**
> network_ip_v6_get()

Sends a plaintext representation of the callers ipv6 address

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetworkApi()

try:
    # Sends a plaintext representation of the callers ipv6 address
    api_instance.network_ip_v6_get()
except ApiException as e:
    print("Exception when calling NetworkApi->network_ip_v6_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

