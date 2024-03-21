# pylint: disable=missing-function-docstring, missing-class-docstring, missing-module-docstring

import pytest
import typing

from openai.types import CompletionUsage
from openai.types.chat import ChatCompletion, ChatCompletionChunk
from openai.types.chat.chat_completion import Choice
from openai.types.chat.chat_completion_message import ChatCompletionMessage
from openai.types.chat.chat_completion_chunk import ChoiceDelta
from fixpoint_sdk.completions import combine_chunks

COMPLETION_ID = 'chatcmpl-95LUxn8nTls6Ti5ES1D5LRXv4lwTg'
CREATED = 1711061307


def test_combine_chunks() -> None:
    chunks = new_chunks()
    completion = new_chat_completion()
    combined = combine_chunks(chunks)
    assert combined.id == completion.id
    assert combined.created == completion.created
    assert combined.model == completion.model
    assert combined.choices[0].finish_reason == completion.choices[0].finish_reason
    assert combined.choices[0].message.role == completion.choices[0].message.role
    assert combined.choices[0].message.content == completion.choices[0].message.content


def new_chunks() -> typing.List[ChatCompletionChunk]:
    return [
        ChatCompletionChunk(id=COMPLETION_ID, choices=[Choice(delta=ChoiceDelta(content='', function_call=None, role='assistant', tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=CREATED, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_3bc1b5746c'),
        ChatCompletionChunk(id=COMPLETION_ID, choices=[Choice(delta=ChoiceDelta(content='No', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=CREATED, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_3bc1b5746c'),
        ChatCompletionChunk(id=COMPLETION_ID, choices=[Choice(delta=ChoiceDelta(content=',', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=CREATED, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_3bc1b5746c'),
        ChatCompletionChunk(id=COMPLETION_ID, choices=[Choice(delta=ChoiceDelta(content=' I', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=CREATED, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_3bc1b5746c'),
        ChatCompletionChunk(id=COMPLETION_ID, choices=[Choice(delta=ChoiceDelta(content=' am', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=CREATED, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_3bc1b5746c'),
        ChatCompletionChunk(id=COMPLETION_ID, choices=[Choice(delta=ChoiceDelta(content=' not', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=CREATED, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_3bc1b5746c'),
        ChatCompletionChunk(id=COMPLETION_ID, choices=[Choice(delta=ChoiceDelta(content=' sentient', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=CREATED, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_3bc1b5746c'),
        ChatCompletionChunk(id=COMPLETION_ID, choices=[Choice(delta=ChoiceDelta(content='.', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=CREATED, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_3bc1b5746c'),
        ChatCompletionChunk(id=COMPLETION_ID, choices=[Choice(delta=ChoiceDelta(content=' I', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=CREATED, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_3bc1b5746c'),
        ChatCompletionChunk(id=COMPLETION_ID, choices=[Choice(delta=ChoiceDelta(content=' am', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=CREATED, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_3bc1b5746c'),
        ChatCompletionChunk(id=COMPLETION_ID, choices=[Choice(delta=ChoiceDelta(content=' a', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=CREATED, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_3bc1b5746c'),
        ChatCompletionChunk(id=COMPLETION_ID, choices=[Choice(delta=ChoiceDelta(content=' computer', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=CREATED, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_3bc1b5746c'),
        ChatCompletionChunk(id=COMPLETION_ID, choices=[Choice(delta=ChoiceDelta(content=' program', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=CREATED, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_3bc1b5746c'),
        ChatCompletionChunk(id=COMPLETION_ID, choices=[Choice(delta=ChoiceDelta(content=' designed', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=CREATED, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_3bc1b5746c'),
        ChatCompletionChunk(id=COMPLETION_ID, choices=[Choice(delta=ChoiceDelta(content=' to', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=CREATED, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_3bc1b5746c'),
        ChatCompletionChunk(id=COMPLETION_ID, choices=[Choice(delta=ChoiceDelta(content=' assist', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=CREATED, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_3bc1b5746c'),
        ChatCompletionChunk(id=COMPLETION_ID, choices=[Choice(delta=ChoiceDelta(content=' with', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=CREATED, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_3bc1b5746c'),
        ChatCompletionChunk(id=COMPLETION_ID, choices=[Choice(delta=ChoiceDelta(content=' tasks', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=CREATED, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_3bc1b5746c'),
        ChatCompletionChunk(id=COMPLETION_ID, choices=[Choice(delta=ChoiceDelta(content=' and', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=CREATED, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_3bc1b5746c'),
        ChatCompletionChunk(id=COMPLETION_ID, choices=[Choice(delta=ChoiceDelta(content=' provide', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=CREATED, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_3bc1b5746c'),
        ChatCompletionChunk(id=COMPLETION_ID, choices=[Choice(delta=ChoiceDelta(content=' information', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=CREATED, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_3bc1b5746c'),
        ChatCompletionChunk(id=COMPLETION_ID, choices=[Choice(delta=ChoiceDelta(content='.', function_call=None, role=None, tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=CREATED, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_3bc1b5746c'),
        ChatCompletionChunk(id=COMPLETION_ID, choices=[Choice(delta=ChoiceDelta(content=None, function_call=None, role=None, tool_calls=None), finish_reason='stop', index=0, logprobs=None)], created=CREATED, model='gpt-3.5-turbo-0125', object='chat.completion.chunk', system_fingerprint='fp_3bc1b5746c')
 ]


def new_chat_completion() -> ChatCompletion:
    return ChatCompletion(
        id=COMPLETION_ID,
        choices=[
            Choice(
                finish_reason='stop',
                index=0,
                logprobs=None,
                message=ChatCompletionMessage(
                    content='No, I am not sentient. I am a computer program designed to assist with tasks and provide information.',
                    role='assistant',
                    function_call=None,
                    tool_calls=None
                )
            )
        ],
        created=CREATED,
        model='gpt-3.5-turbo-0125',
        object='chat.completion',
        system_fingerprint='fp_fa89f7a861',
        usage=CompletionUsage(completion_tokens=21, prompt_tokens=11, total_tokens=32)
    )
