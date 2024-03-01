import requests
import typing

from openai import OpenAI
from openai.types.chat import ChatCompletion

from .lib.env import get_fixpoint_api_key
from .lib.requests import Requester
from .lib.debugging import dprint
from . import types


class FixpointClient:
    def __init__(
        self,
        fixpoint_api_key: typing.Optional[str],
        openai_api_key: typing.Optional[str],
        api_base_url: typing.Optional[str],
        *args: typing.Any,
        **kwargs: typing.Any,
    ):
        # Check that the environment variable FIXPOINT_API_KEY is set
        _api_key = get_fixpoint_api_key(fixpoint_api_key)

        self._api_key = _api_key
        self._requester = Requester(self._api_key, api_base_url)
        if openai_api_key:
            kwargs = dict(kwargs, api_key=openai_api_key)
        self.client = OpenAI(*args, **kwargs)
        self.chat = self._Chat(self._requester, self.client)
        self.fixpoint = self._Fixpoint(self._requester)

    class _Fixpoint:
        def __init__(self, requester: Requester):
            self.user_feedback = self._UserFeedback(requester)
            self.attributes = self._Attributes(requester)

        class _UserFeedback:
            def __init__(self, requester: Requester):
                self._requester = requester

            def create(
                self, request: types.CreateUserFeedbackRequest
            ) -> types.CreateUserFeedbackResponse:
                return self._requester.create_user_feedback(request)

        class _Attributes:
            def __init__(self, requester: Requester):
                self._requester = requester

            def create(
                self, request: types.CreateLogAttributeRequest
            ) -> requests.Response:
                return self._requester.create_attribute(request)

    class _Completions:
        def __init__(self, requester: Requester, client: OpenAI):
            self.client = client
            self._requester = requester

        def create(
            self, *args: typing.Any, **kwargs: typing.Any
        ) -> typing.Tuple[ChatCompletion, typing.Any, typing.Any]:
            # Extract trace_id from kwargs, if it exists, otherwise set it to None
            trace_id = kwargs.pop("trace_id", None)

            # Deep copy the kwargs to avoid modifying the original
            reqCopy = kwargs.copy()
            if "model" not in reqCopy:
                raise ValueError("model needs to be passed in as a kwarg")
            reqCopy["model_name"] = reqCopy.pop("model")

            # Send HTTP request before calling create
            input_resp = self._requester.create_openai_input_log(
                reqCopy["model_name"],
                # TODO(dbmikus) fix sloppy typing
                typing.cast(types.OpenAILLMInputLog, reqCopy),
                trace_id=trace_id,
            )
            dprint("Created an input log: {}".format(input_resp["name"]))

            # Make create call to OPEN AI
            openai_response = self.client.chat.completions.create(*args, **kwargs)
            dprint("Received an openai response: {}".format(openai_response.id))

            # Send HTTP request after calling create
            output_resp = self._requester.create_openai_output_log(
                reqCopy["model_name"], input_resp, openai_response, trace_id=trace_id
            )
            dprint("Created an output log: {}".format(output_resp["name"]))

            return openai_response, input_resp, output_resp

    class _Chat:
        def __init__(self, requester: Requester, client: OpenAI):
            self.completions = FixpointClient._Completions(requester, client)
