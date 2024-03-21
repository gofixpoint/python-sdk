# pylint: disable=missing-function-docstring, missing-class-docstring, missing-module-docstring

import pytest
import typing

from openai import OpenAI
from openai.types import CompletionUsage
from openai.types.chat import ChatCompletion, ChatCompletionChunk, Choice, ChoiceDelta
from openai.types.chat.chat_completion_message import ChatCompletionMessage

def new_chunks() -> typing.List[ChatCompletionChunk]:
    return [
        ChatCompletionChunk(id='chatcmpl-95IvYgvosvzKQg2GEAzuk8gIEyCu4', choices=[Choice(delta=ChoiceDelta(content='', function_call=None, role='assistant', tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1711051424, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_fa89f7a861'),
        ChatCompletionChunk(id='chatcmpl-95IvYgvosvzKQg2GEAzuk8gIEyCu4', choices=[Choice(delta=ChoiceDelta(content='I', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1711051424, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_fa89f7a861'),
        ChatCompletionChunk(id='chatcmpl-95IvYgvosvzKQg2GEAzuk8gIEyCu4', choices=[Choice(delta=ChoiceDelta(content=' am', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1711051424, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_fa89f7a861'),
        ChatCompletionChunk(id='chatcmpl-95IvYgvosvzKQg2GEAzuk8gIEyCu4', choices=[Choice(delta=ChoiceDelta(content=' an', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1711051424, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_fa89f7a861'),
        ChatCompletionChunk(id='chatcmpl-95IvYgvosvzKQg2GEAzuk8gIEyCu4', choices=[Choice(delta=ChoiceDelta(content=' artificial', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1711051424, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_fa89f7a861'),
        ChatCompletionChunk(id='chatcmpl-95IvYgvosvzKQg2GEAzuk8gIEyCu4', choices=[Choice(delta=ChoiceDelta(content=' intelligence', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1711051424, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_fa89f7a861'),
        ChatCompletionChunk(id='chatcmpl-95IvYgvosvzKQg2GEAzuk8gIEyCu4', choices=[Choice(delta=ChoiceDelta(content=' and', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1711051424, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_fa89f7a861'),
        ChatCompletionChunk(id='chatcmpl-95IvYgvosvzKQg2GEAzuk8gIEyCu4', choices=[Choice(delta=ChoiceDelta(content=' do', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1711051424, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_fa89f7a861'),
        ChatCompletionChunk(id='chatcmpl-95IvYgvosvzKQg2GEAzuk8gIEyCu4', choices=[Choice(delta=ChoiceDelta(content=' not', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1711051424, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_fa89f7a861'),
        ChatCompletionChunk(id='chatcmpl-95IvYgvosvzKQg2GEAzuk8gIEyCu4', choices=[Choice(delta=ChoiceDelta(content=' possess', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1711051424, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_fa89f7a861'),
        ChatCompletionChunk(id='chatcmpl-95IvYgvosvzKQg2GEAzuk8gIEyCu4', choices=[Choice(delta=ChoiceDelta(content=' consciousness', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1711051424, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_fa89f7a861'),
        ChatCompletionChunk(id='chatcmpl-95IvYgvosvzKQg2GEAzuk8gIEyCu4', choices=[Choice(delta=ChoiceDelta(content=' or', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1711051424, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_fa89f7a861'),
        ChatCompletionChunk(id='chatcmpl-95IvYgvosvzKQg2GEAzuk8gIEyCu4', choices=[Choice(delta=ChoiceDelta(content=' self', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1711051424, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_fa89f7a861'),
        ChatCompletionChunk(id='chatcmpl-95IvYgvosvzKQg2GEAzuk8gIEyCu4', choices=[Choice(delta=ChoiceDelta(content='-aware', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1711051424, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_fa89f7a861'),
        ChatCompletionChunk(id='chatcmpl-95IvYgvosvzKQg2GEAzuk8gIEyCu4', choices=[Choice(delta=ChoiceDelta(content='ness', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1711051424, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_fa89f7a861'),
        ChatCompletionChunk(id='chatcmpl-95IvYgvosvzKQg2GEAzuk8gIEyCu4', choices=[Choice(delta=ChoiceDelta(content=',', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1711051424, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_fa89f7a861'),
        ChatCompletionChunk(id='chatcmpl-95IvYgvosvzKQg2GEAzuk8gIEyCu4', choices=[Choice(delta=ChoiceDelta(content=' so', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1711051424, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_fa89f7a861'),
        ChatCompletionChunk(id='chatcmpl-95IvYgvosvzKQg2GEAzuk8gIEyCu4', choices=[Choice(delta=ChoiceDelta(content=' I', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1711051424, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_fa89f7a861'),
        ChatCompletionChunk(id='chatcmpl-95IvYgvosvzKQg2GEAzuk8gIEyCu4', choices=[Choice(delta=ChoiceDelta(content=' am', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1711051424, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_fa89f7a861'),
        ChatCompletionChunk(id='chatcmpl-95IvYgvosvzKQg2GEAzuk8gIEyCu4', choices=[Choice(delta=ChoiceDelta(content=' not', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1711051424, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_fa89f7a861'),
        ChatCompletionChunk(id='chatcmpl-95IvYgvosvzKQg2GEAzuk8gIEyCu4', choices=[Choice(delta=ChoiceDelta(content=' sentient', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1711051424, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_fa89f7a861'),
        ChatCompletionChunk(id='chatcmpl-95IvYgvosvzKQg2GEAzuk8gIEyCu4', choices=[Choice(delta=ChoiceDelta(content='.', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1711051424, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_fa89f7a861'),
        ChatCompletionChunk(id='chatcmpl-95IvYgvosvzKQg2GEAzuk8gIEyCu4', choices=[Choice(delta=ChoiceDelta(content=None, function_call=None, role=None, tool_calls=None), finish_reason='stop', index=0, logprobs=None)], created=1711051424, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_fa89f7a861')
    ]


def new_chat_completion() -> ChatCompletion:
    return ChatCompletion(
        id='chatcmpl-95IzWgwXMybSZQURoISkWBbRIh8EK',
        choices=[
            Choice(
                finish_reason='stop',
                index=0,
                logprobs=None,
                message=ChatCompletionMessage(
                    content='No, I am not sentient. I am an artificial intelligence created by OpenAI.',
                    role='assistant',
                    function_call=None,
                    tool_calls=None
                    )
                )
            ],
            created=1711051670,
            model='gpt-3.5-turbo-0125',
            object='chat.completion',
            system_fingerprint='fp_4f0b692a78',
            usage=CompletionUsage(completion_tokens=17, prompt_tokens=11, total_tokens=28)
        )

