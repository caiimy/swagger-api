# swagger_client.LobbiesApi

All URIs are relative to *https://matchmaking.braymatter.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_lobby**](LobbiesApi.md#create_lobby) | **POST** /lobbies | creates a new lobby
[**join_lobby**](LobbiesApi.md#join_lobby) | **PUT** /lobbies/{name} | Join an existing lobby
[**lobbies_lobby_name_events_event_post**](LobbiesApi.md#lobbies_lobby_name_events_event_post) | **POST** /lobbies/{lobbyName}/events/{event} | Post an event to a lobby such as GameStarted or GameEnded
[**lobbies_lobby_name_players_player_name_event_post**](LobbiesApi.md#lobbies_lobby_name_players_player_name_event_post) | **POST** /lobbies/{lobbyName}/players/{playerName}/{event} | Post a player event to a lobby such as connected, disconnected, kicked
[**pulse_lobby**](LobbiesApi.md#pulse_lobby) | **PATCH** /lobbies/{name} | Heartbeat for a lobby
[**search_lobbies**](LobbiesApi.md#search_lobbies) | **GET** /lobbies | Pulls a list of available lobbies

# **create_lobby**
> create_lobby(body=body)

creates a new lobby

Creates a new lobby that other players can join

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LobbiesApi()
body = swagger_client.LobbyCreateRequest() # LobbyCreateRequest | Lobby to Create (optional)

try:
    # creates a new lobby
    api_instance.create_lobby(body=body)
except ApiException as e:
    print("Exception when calling LobbiesApi->create_lobby: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LobbyCreateRequest**](LobbyCreateRequest.md)| Lobby to Create | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **join_lobby**
> join_lobby(name)

Join an existing lobby

Joins an existing lobby

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LobbiesApi()
name = 'name_example' # str | 

try:
    # Join an existing lobby
    api_instance.join_lobby(name)
except ApiException as e:
    print("Exception when calling LobbiesApi->join_lobby: %s\n" % e)
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

# **lobbies_lobby_name_events_event_post**
> lobbies_lobby_name_events_event_post(lobby_name, event)

Post an event to a lobby such as GameStarted or GameEnded

This endpoint is used to send events to a lobby

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LobbiesApi()
lobby_name = 'lobby_name_example' # str | 
event = 'event_example' # str | 

try:
    # Post an event to a lobby such as GameStarted or GameEnded
    api_instance.lobbies_lobby_name_events_event_post(lobby_name, event)
except ApiException as e:
    print("Exception when calling LobbiesApi->lobbies_lobby_name_events_event_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lobby_name** | **str**|  | 
 **event** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lobbies_lobby_name_players_player_name_event_post**
> lobbies_lobby_name_players_player_name_event_post(lobby_name, player_name, event)

Post a player event to a lobby such as connected, disconnected, kicked

This endpoint is used to send events to a lobby

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LobbiesApi()
lobby_name = 'lobby_name_example' # str | 
player_name = 'player_name_example' # str | 
event = 'event_example' # str | 

try:
    # Post a player event to a lobby such as connected, disconnected, kicked
    api_instance.lobbies_lobby_name_players_player_name_event_post(lobby_name, player_name, event)
except ApiException as e:
    print("Exception when calling LobbiesApi->lobbies_lobby_name_players_player_name_event_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lobby_name** | **str**|  | 
 **player_name** | **str**|  | 
 **event** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pulse_lobby**
> pulse_lobby(name)

Heartbeat for a lobby

Send a heartbeat to the lobby to let the server know you are still connected to it if the owner of a lobby doesn't ping within a set amount of time the lobby will be de-listed

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LobbiesApi()
name = 'name_example' # str | 

try:
    # Heartbeat for a lobby
    api_instance.pulse_lobby(name)
except ApiException as e:
    print("Exception when calling LobbiesApi->pulse_lobby: %s\n" % e)
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

# **search_lobbies**
> list[Lobby] search_lobbies(is_empty=is_empty, name=name)

Pulls a list of available lobbies

Takes several filter parameters to filter for empty lobbies etc.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LobbiesApi()
is_empty = true # bool | pass an optional boolean to filter out empty lobbies (optional)
name = 'name_example' # str | search for lobbies where lobby.name %like% this parameter (optional)

try:
    # Pulls a list of available lobbies
    api_response = api_instance.search_lobbies(is_empty=is_empty, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LobbiesApi->search_lobbies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_empty** | **bool**| pass an optional boolean to filter out empty lobbies | [optional] 
 **name** | **str**| search for lobbies where lobby.name %like% this parameter | [optional] 

### Return type

[**list[Lobby]**](Lobby.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

