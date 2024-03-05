# coding: utf-8

"""
    Simple Matchmaking API

    This is a simple matchmaking API API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: you@your-company.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class LobbiesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_lobby(self, **kwargs):  # noqa: E501
        """creates a new lobby  # noqa: E501

        Creates a new lobby that other players can join  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_lobby(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LobbyCreateRequest body: Lobby to Create
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_lobby_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_lobby_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_lobby_with_http_info(self, **kwargs):  # noqa: E501
        """creates a new lobby  # noqa: E501

        Creates a new lobby that other players can join  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_lobby_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LobbyCreateRequest body: Lobby to Create
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_lobby" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/lobbies', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def join_lobby(self, name, **kwargs):  # noqa: E501
        """Join an existing lobby  # noqa: E501

        Joins an existing lobby  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.join_lobby(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.join_lobby_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.join_lobby_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def join_lobby_with_http_info(self, name, **kwargs):  # noqa: E501
        """Join an existing lobby  # noqa: E501

        Joins an existing lobby  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.join_lobby_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method join_lobby" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `join_lobby`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/lobbies/{name}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def lobbies_lobby_name_events_event_post(self, lobby_name, event, **kwargs):  # noqa: E501
        """Post an event to a lobby such as GameStarted or GameEnded  # noqa: E501

        This endpoint is used to send events to a lobby  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lobbies_lobby_name_events_event_post(lobby_name, event, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str lobby_name: (required)
        :param str event: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.lobbies_lobby_name_events_event_post_with_http_info(lobby_name, event, **kwargs)  # noqa: E501
        else:
            (data) = self.lobbies_lobby_name_events_event_post_with_http_info(lobby_name, event, **kwargs)  # noqa: E501
            return data

    def lobbies_lobby_name_events_event_post_with_http_info(self, lobby_name, event, **kwargs):  # noqa: E501
        """Post an event to a lobby such as GameStarted or GameEnded  # noqa: E501

        This endpoint is used to send events to a lobby  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lobbies_lobby_name_events_event_post_with_http_info(lobby_name, event, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str lobby_name: (required)
        :param str event: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['lobby_name', 'event']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lobbies_lobby_name_events_event_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'lobby_name' is set
        if ('lobby_name' not in params or
                params['lobby_name'] is None):
            raise ValueError("Missing the required parameter `lobby_name` when calling `lobbies_lobby_name_events_event_post`")  # noqa: E501
        # verify the required parameter 'event' is set
        if ('event' not in params or
                params['event'] is None):
            raise ValueError("Missing the required parameter `event` when calling `lobbies_lobby_name_events_event_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'lobby_name' in params:
            path_params['lobbyName'] = params['lobby_name']  # noqa: E501
        if 'event' in params:
            path_params['event'] = params['event']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/lobbies/{lobbyName}/events/{event}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def lobbies_lobby_name_players_player_name_event_post(self, lobby_name, player_name, event, **kwargs):  # noqa: E501
        """Post a player event to a lobby such as connected, disconnected, kicked  # noqa: E501

        This endpoint is used to send events to a lobby  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lobbies_lobby_name_players_player_name_event_post(lobby_name, player_name, event, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str lobby_name: (required)
        :param str player_name: (required)
        :param str event: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.lobbies_lobby_name_players_player_name_event_post_with_http_info(lobby_name, player_name, event, **kwargs)  # noqa: E501
        else:
            (data) = self.lobbies_lobby_name_players_player_name_event_post_with_http_info(lobby_name, player_name, event, **kwargs)  # noqa: E501
            return data

    def lobbies_lobby_name_players_player_name_event_post_with_http_info(self, lobby_name, player_name, event, **kwargs):  # noqa: E501
        """Post a player event to a lobby such as connected, disconnected, kicked  # noqa: E501

        This endpoint is used to send events to a lobby  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lobbies_lobby_name_players_player_name_event_post_with_http_info(lobby_name, player_name, event, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str lobby_name: (required)
        :param str player_name: (required)
        :param str event: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['lobby_name', 'player_name', 'event']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lobbies_lobby_name_players_player_name_event_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'lobby_name' is set
        if ('lobby_name' not in params or
                params['lobby_name'] is None):
            raise ValueError("Missing the required parameter `lobby_name` when calling `lobbies_lobby_name_players_player_name_event_post`")  # noqa: E501
        # verify the required parameter 'player_name' is set
        if ('player_name' not in params or
                params['player_name'] is None):
            raise ValueError("Missing the required parameter `player_name` when calling `lobbies_lobby_name_players_player_name_event_post`")  # noqa: E501
        # verify the required parameter 'event' is set
        if ('event' not in params or
                params['event'] is None):
            raise ValueError("Missing the required parameter `event` when calling `lobbies_lobby_name_players_player_name_event_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'lobby_name' in params:
            path_params['lobbyName'] = params['lobby_name']  # noqa: E501
        if 'player_name' in params:
            path_params['playerName'] = params['player_name']  # noqa: E501
        if 'event' in params:
            path_params['event'] = params['event']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/lobbies/{lobbyName}/players/{playerName}/{event}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pulse_lobby(self, name, **kwargs):  # noqa: E501
        """Heartbeat for a lobby  # noqa: E501

        Send a heartbeat to the lobby to let the server know you are still connected to it if the owner of a lobby doesn't ping within a set amount of time the lobby will be de-listed  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pulse_lobby(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pulse_lobby_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.pulse_lobby_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def pulse_lobby_with_http_info(self, name, **kwargs):  # noqa: E501
        """Heartbeat for a lobby  # noqa: E501

        Send a heartbeat to the lobby to let the server know you are still connected to it if the owner of a lobby doesn't ping within a set amount of time the lobby will be de-listed  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pulse_lobby_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pulse_lobby" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `pulse_lobby`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/lobbies/{name}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_lobbies(self, **kwargs):  # noqa: E501
        """Pulls a list of available lobbies  # noqa: E501

        Takes several filter parameters to filter for empty lobbies etc.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_lobbies(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool is_empty: pass an optional boolean to filter out empty lobbies
        :param str name: search for lobbies where lobby.name %like% this parameter
        :return: list[Lobby]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_lobbies_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.search_lobbies_with_http_info(**kwargs)  # noqa: E501
            return data

    def search_lobbies_with_http_info(self, **kwargs):  # noqa: E501
        """Pulls a list of available lobbies  # noqa: E501

        Takes several filter parameters to filter for empty lobbies etc.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_lobbies_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool is_empty: pass an optional boolean to filter out empty lobbies
        :param str name: search for lobbies where lobby.name %like% this parameter
        :return: list[Lobby]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['is_empty', 'name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_lobbies" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'is_empty' in params:
            query_params.append(('isEmpty', params['is_empty']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/lobbies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Lobby]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
