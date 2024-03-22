"""Code for chat completions."""

import typing

from openai import OpenAI
from openai._streaming import Stream
from openai.types.chat import ChatCompletion, ChatCompletionChunk
from openai.types.chat.chat_completion import Choice
from openai.types.chat.chat_completion_message import ChatCompletionMessage

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

    def _combine_chunks(self) -> typing.Union[ChatCompletion, None]:
        return combine_chunks(self._outputs)


FinishReason = typing.Literal["stop", "length", "tool_calls", "content_filter", "function_call"]

def combine_chunks(chunks: typing.List[ChatCompletionChunk]) -> ChatCompletion:
    if len(chunks) == 0:
        raise ValueError("Must have at least one chunk")

    num_choices = 0
    for chunk in chunks:
        if num_choices is 0:
            num_choices = len(chunk.choices)
        elif num_choices != len(chunk.choices):
            raise ValueError("All chunks must have the same number of choices")

    chatid = ""
    created = 0
    model = ""
    choice_contents: typing.List[typing.List[str]] = [[] for _ in range(num_choices)]
    # default to "assistant" for typing reasons
    # default to "stop" for typing reasons
    finish_reasons: typing.List[FinishReason] = ['stop' for _ in range(num_choices)]
    for chunk in chunks:
        # all `id` and `created` values are the same.
        chatid = chunk.id
        created = chunk.created
        model = chunk.model
        for choice in chunk.choices:
            if choice.delta.content is not None:
                choice_contents[choice.index].append(choice.delta.content)
            # default to "stop" for typing reasons
            finish_reasons[choice.index] = choice.finish_reason or 'stop'

    final_choices = []
    for i, choice_content in enumerate(choice_contents):
        final_choices.append(Choice(
            index=i,
            finish_reason=finish_reasons[i],
            logprobs=None,
            message=ChatCompletionMessage(
                # all output roles are assistants
                role='assistant',
                content="".join(choice_content)
            )
        ))

    return ChatCompletion(
        id=chatid,
        created=created,
        model=model,
        object='chat.completion',
        # The server will compute this when logging
        usage=None,
        choices=final_choices
    )



class Completions:
    def __init__(self, requester: Requester, client: OpenAI):
        self.client = client
        self._requester = requester

    def create(
        self, *args: typing.Any, **kwargs: typing.Any
    ) -> typing.Union[FixpointChatCompletion, FixpointChatCompletionStream]:
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

        return FixpointChatCompletion(
            completion=openai_response,
            input_log=input_resp,
            output_log=output_resp,
        )


class Chat:
    def __init__(self, requester: Requester, client: OpenAI):
        self.completions = Completions(requester, client)
