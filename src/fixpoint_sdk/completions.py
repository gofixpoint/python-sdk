"""Code for chat completions."""

import typing

from openai import OpenAI
from openai._streaming import Stream
from openai.types.chat import ChatCompletion, ChatCompletionChunk

from .lib.requests import Requester
from .lib.debugging import dprint
from . import types


class FixpointChatCompletion:
    def __init__(self, completion: ChatCompletion, input_log: types.InputLog, output_log: types.OutputLog):
        self.completion = completion
        self.input_log = input_log
        self.output_log = output_log


class FixpointChatCompletionStream:
    def __init__(self, stream: Stream[ChatCompletionChunk], input_log: types.InputLog):
        self._stream = stream
        self.input_log = input_log
        self.output_log = None
        self._outputs = []

    def __next__(self) -> ChatCompletionChunk:
        try:
            self._last_output = self._stream.__next__()
            return self._last_output
        except StopIteration:
            # Send HTTP request after calling create
            output_resp = self._requester.create_openai_output_log(
                req_copy["model_name"],
                self.input_log,
                openai_response,
                trace_id=trace_id,
                mode=mode_type,
            )
            self.output_log = output_resp
            raise

    def __iter__(self) -> typing.Iterator[ChatCompletionChunk]:
        for item in self._stream:
            yield item

    def _combine_chunks(self) -> types.Union[ChatCompletion, None]:
        return _combine_chunks(self._outputs)


def _combine_chunks(chunks: typing.List[ChatCompletionChunk]) -> types.Union[ChatCompletion, None]:
    if len(chunks) == 0:
        return None

    chatid = ""
    choices = []
    for chunk in chunks:
        chatid = chunk.id
        pass

    # return ChatCompletion(id=)
    return None



class Completions:
    def __init__(self, requester: Requester, client: OpenAI):
        self.client = client
        self._requester = requester

    def create(
        self, *args: typing.Any, **kwargs: typing.Any
    ) -> typing.Tuple[ChatCompletion, Stream[ChatCompletionChunk]]:
        """Create an OpenAI completion and log the LLM input and output."""
        # Do not mutate the input kwargs. That is an unexpected behavior for
        # our caller.
        kwargs = kwargs.copy()
        # Extract trace_id from kwargs, if it exists, otherwise set it to None
        trace_id = kwargs.pop("trace_id", None)
        mode_type = types.parse_mode_type(kwargs.pop("mode", "unspecified"))

        # Deep copy the kwargs to avoid modifying the original
        req_copy = kwargs.copy()
        if "model" not in req_copy:
            raise ValueError("model needs to be passed in as a kwarg")
        req_copy["model_name"] = req_copy.pop("model")

        # Send HTTP request before calling create
        input_resp = self._requester.create_openai_input_log(
            req_copy["model_name"],
            # TODO(dbmikus) fix sloppy typing
            typing.cast(types.OpenAILLMInputLog, req_copy),
            trace_id=trace_id,
            mode=mode_type,
        )
        dprint(f'Created an input log: {input_resp["name"]}')

        # Make create call to OPEN AI
        openai_response = self.client.chat.completions.create(*args, **kwargs)
        dprint(f"Received an openai response: {openai_response.id}")

        # Send HTTP request after calling create
        output_resp = self._requester.create_openai_output_log(
            req_copy["model_name"],
            input_resp,
            openai_response,
            trace_id=trace_id,
            mode=mode_type,
        )
        dprint(f"Created an output log: {output_resp['name']}")

        return openai_response, input_resp, output_resp


class Chat:
    def __init__(self, requester: Requester, client: OpenAI):
        self.completions = Completions(requester, client)
