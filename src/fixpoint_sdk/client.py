"""Defines the Fixpoint client, which is the main interface for the SDK."""

import typing

from openai import OpenAI

from fixpoint_sdk.openapi.gen.openapi_client.configuration import Configuration
from fixpoint_sdk.openapi.gen.openapi_client.api_client import ApiClient
from fixpoint_sdk.openapi.gen.openapi_client.api.llm_proxy_api import LLMProxyApi

from .lib.env import get_fixpoint_api_key, get_api_base_url
from .lib.requests import Requester
from . import types
from .completions import Chat, ChatWithRouter



class FixpointClient:
    """The FixpointClient lets you interact with the Fixpoint API."""

    def __init__(
        self,
        *args: typing.Any,
        fixpoint_api_key: typing.Optional[str] = None,
        openai_api_key: typing.Optional[str] = None,
        api_base_url: typing.Optional[str] = None,
        use_router: bool = False,
        **kwargs: typing.Any,
    ):
        # Check that the environment variable FIXPOINT_API_KEY is set
        _api_key = get_fixpoint_api_key(fixpoint_api_key)

        self._api_key = _api_key
        self._requester = Requester(self._api_key, get_api_base_url(api_base_url))
        if openai_api_key:
            kwargs = dict(kwargs, api_key=openai_api_key)
        self.client = OpenAI(*args, **kwargs)
        if use_router:
            self.chat = ChatWithRouter(self._requester, self.client)
        else:
            self.chat = Chat(self._requester, self.client)
        self.fixpoint = self._Fixpoint(self._requester)

    class _Fixpoint:
        def __init__(self, requester: Requester):
            self.user_feedback = self._UserFeedback(requester)
            self.attributes = self._Attributes(requester)

            configuration = Configuration(
                host=get_api_base_url(requester.base_url),
            )

            api_client = ApiClient(
                configuration,
                header_name="Authorization",
                header_value=f"Bearer {requester.api_key}",
            )
            self.proxy_client = LLMProxyApi(api_client)

        class _UserFeedback:
            def __init__(self, requester: Requester):
                self._requester = requester

            def create(
                self, request: types.CreateUserFeedbackRequest
            ) -> types.CreateUserFeedbackResponse:
                """Attach user feedback to an LLM log."""
                return self._requester.create_user_feedback(request)

        class _Attributes:
            def __init__(self, requester: Requester):
                self._requester = requester

            def create(
                self, request: types.CreateLogAttributeRequest
            ) -> types.LogAttribute:
                """Attach a log attribute to an LLM log."""
                return self._requester.create_attribute(request)
