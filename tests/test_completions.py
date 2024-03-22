# pylint: disable=missing-function-docstring, missing-class-docstring, missing-module-docstring

import typing
import pytest

from openai.types import CompletionUsage
from openai.types.chat import ChatCompletion, ChatCompletionChunk
from openai.types.chat.chat_completion import Choice as CompletionChoice
from openai.types.chat.chat_completion_message import ChatCompletionMessage
from openai.types.chat.chat_completion_chunk import ChoiceDelta, Choice

from fixpoint_sdk.completions import combine_chunks, FinishReason

COMPLETION_ID = "chatcmpl-95LUxn8nTls6Ti5ES1D5LRXv4lwTg"
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


def test_combine_multichoice_chunks() -> None:
    chunks = zip_choices(
        new_chunks(), new_chunks(), append_text="!", finish_reason="tool_calls"
    )
    completion = new_chat_completion()
    combined = combine_chunks(chunks)
    assert combined.id == completion.id
    assert combined.created == completion.created
    assert combined.model == completion.model
    assert combined.choices[0].finish_reason == completion.choices[0].finish_reason
    assert combined.choices[0].message.role == completion.choices[0].message.role
    assert combined.choices[0].message.content == completion.choices[0].message.content

    assert combined.choices[1].finish_reason == "tool_calls"
    # all output roles are the same: "assistant"
    assert (
        combined.choices[1].message.content
        == "!No!,! I! am! not! sentient!.! I! am! a! computer! program! designed! to! assist! with! tasks! and! provide! information!.!"  # pylint: disable=line-too-long
    )


def test_invalid_choices() -> None:
    chunks = zip_choices(new_chunks(), new_chunks(), drop_indexes={2})
    with pytest.raises(ValueError):
        combine_chunks(chunks)


def new_chunks() -> typing.List[ChatCompletionChunk]:
    return [
        ChatCompletionChunk(
            id=COMPLETION_ID,
            choices=[
                Choice(
                    delta=ChoiceDelta(
                        content="",
                        function_call=None,
                        role="assistant",
                        tool_calls=None,
                    ),
                    finish_reason=None,
                    index=0,
                    logprobs=None,
                )
            ],
            created=CREATED,
            model="gpt-3.5-turbo-0125",
            object="chat.completion.chunk",
            system_fingerprint="fp_3bc1b5746c",
        ),
        ChatCompletionChunk(
            id=COMPLETION_ID,
            choices=[
                Choice(
                    delta=ChoiceDelta(
                        content="No", function_call=None, role=None, tool_calls=None
                    ),
                    finish_reason=None,
                    index=0,
                    logprobs=None,
                )
            ],
            created=CREATED,
            model="gpt-3.5-turbo-0125",
            object="chat.completion.chunk",
            system_fingerprint="fp_3bc1b5746c",
        ),
        ChatCompletionChunk(
            id=COMPLETION_ID,
            choices=[
                Choice(
                    delta=ChoiceDelta(
                        content=",", function_call=None, role=None, tool_calls=None
                    ),
                    finish_reason=None,
                    index=0,
                    logprobs=None,
                )
            ],
            created=CREATED,
            model="gpt-3.5-turbo-0125",
            object="chat.completion.chunk",
            system_fingerprint="fp_3bc1b5746c",
        ),
        ChatCompletionChunk(
            id=COMPLETION_ID,
            choices=[
                Choice(
                    delta=ChoiceDelta(
                        content=" I", function_call=None, role=None, tool_calls=None
                    ),
                    finish_reason=None,
                    index=0,
                    logprobs=None,
                )
            ],
            created=CREATED,
            model="gpt-3.5-turbo-0125",
            object="chat.completion.chunk",
            system_fingerprint="fp_3bc1b5746c",
        ),
        ChatCompletionChunk(
            id=COMPLETION_ID,
            choices=[
                Choice(
                    delta=ChoiceDelta(
                        content=" am", function_call=None, role=None, tool_calls=None
                    ),
                    finish_reason=None,
                    index=0,
                    logprobs=None,
                )
            ],
            created=CREATED,
            model="gpt-3.5-turbo-0125",
            object="chat.completion.chunk",
            system_fingerprint="fp_3bc1b5746c",
        ),
        ChatCompletionChunk(
            id=COMPLETION_ID,
            choices=[
                Choice(
                    delta=ChoiceDelta(
                        content=" not", function_call=None, role=None, tool_calls=None
                    ),
                    finish_reason=None,
                    index=0,
                    logprobs=None,
                )
            ],
            created=CREATED,
            model="gpt-3.5-turbo-0125",
            object="chat.completion.chunk",
            system_fingerprint="fp_3bc1b5746c",
        ),
        ChatCompletionChunk(
            id=COMPLETION_ID,
            choices=[
                Choice(
                    delta=ChoiceDelta(
                        content=" sentient",
                        function_call=None,
                        role=None,
                        tool_calls=None,
                    ),
                    finish_reason=None,
                    index=0,
                    logprobs=None,
                )
            ],
            created=CREATED,
            model="gpt-3.5-turbo-0125",
            object="chat.completion.chunk",
            system_fingerprint="fp_3bc1b5746c",
        ),
        ChatCompletionChunk(
            id=COMPLETION_ID,
            choices=[
                Choice(
                    delta=ChoiceDelta(
                        content=".", function_call=None, role=None, tool_calls=None
                    ),
                    finish_reason=None,
                    index=0,
                    logprobs=None,
                )
            ],
            created=CREATED,
            model="gpt-3.5-turbo-0125",
            object="chat.completion.chunk",
            system_fingerprint="fp_3bc1b5746c",
        ),
        ChatCompletionChunk(
            id=COMPLETION_ID,
            choices=[
                Choice(
                    delta=ChoiceDelta(
                        content=" I", function_call=None, role=None, tool_calls=None
                    ),
                    finish_reason=None,
                    index=0,
                    logprobs=None,
                )
            ],
            created=CREATED,
            model="gpt-3.5-turbo-0125",
            object="chat.completion.chunk",
            system_fingerprint="fp_3bc1b5746c",
        ),
        ChatCompletionChunk(
            id=COMPLETION_ID,
            choices=[
                Choice(
                    delta=ChoiceDelta(
                        content=" am", function_call=None, role=None, tool_calls=None
                    ),
                    finish_reason=None,
                    index=0,
                    logprobs=None,
                )
            ],
            created=CREATED,
            model="gpt-3.5-turbo-0125",
            object="chat.completion.chunk",
            system_fingerprint="fp_3bc1b5746c",
        ),
        ChatCompletionChunk(
            id=COMPLETION_ID,
            choices=[
                Choice(
                    delta=ChoiceDelta(
                        content=" a", function_call=None, role=None, tool_calls=None
                    ),
                    finish_reason=None,
                    index=0,
                    logprobs=None,
                )
            ],
            created=CREATED,
            model="gpt-3.5-turbo-0125",
            object="chat.completion.chunk",
            system_fingerprint="fp_3bc1b5746c",
        ),
        ChatCompletionChunk(
            id=COMPLETION_ID,
            choices=[
                Choice(
                    delta=ChoiceDelta(
                        content=" computer",
                        function_call=None,
                        role=None,
                        tool_calls=None,
                    ),
                    finish_reason=None,
                    index=0,
                    logprobs=None,
                )
            ],
            created=CREATED,
            model="gpt-3.5-turbo-0125",
            object="chat.completion.chunk",
            system_fingerprint="fp_3bc1b5746c",
        ),
        ChatCompletionChunk(
            id=COMPLETION_ID,
            choices=[
                Choice(
                    delta=ChoiceDelta(
                        content=" program",
                        function_call=None,
                        role=None,
                        tool_calls=None,
                    ),
                    finish_reason=None,
                    index=0,
                    logprobs=None,
                )
            ],
            created=CREATED,
            model="gpt-3.5-turbo-0125",
            object="chat.completion.chunk",
            system_fingerprint="fp_3bc1b5746c",
        ),
        ChatCompletionChunk(
            id=COMPLETION_ID,
            choices=[
                Choice(
                    delta=ChoiceDelta(
                        content=" designed",
                        function_call=None,
                        role=None,
                        tool_calls=None,
                    ),
                    finish_reason=None,
                    index=0,
                    logprobs=None,
                )
            ],
            created=CREATED,
            model="gpt-3.5-turbo-0125",
            object="chat.completion.chunk",
            system_fingerprint="fp_3bc1b5746c",
        ),
        ChatCompletionChunk(
            id=COMPLETION_ID,
            choices=[
                Choice(
                    delta=ChoiceDelta(
                        content=" to", function_call=None, role=None, tool_calls=None
                    ),
                    finish_reason=None,
                    index=0,
                    logprobs=None,
                )
            ],
            created=CREATED,
            model="gpt-3.5-turbo-0125",
            object="chat.completion.chunk",
            system_fingerprint="fp_3bc1b5746c",
        ),
        ChatCompletionChunk(
            id=COMPLETION_ID,
            choices=[
                Choice(
                    delta=ChoiceDelta(
                        content=" assist",
                        function_call=None,
                        role=None,
                        tool_calls=None,
                    ),
                    finish_reason=None,
                    index=0,
                    logprobs=None,
                )
            ],
            created=CREATED,
            model="gpt-3.5-turbo-0125",
            object="chat.completion.chunk",
            system_fingerprint="fp_3bc1b5746c",
        ),
        ChatCompletionChunk(
            id=COMPLETION_ID,
            choices=[
                Choice(
                    delta=ChoiceDelta(
                        content=" with", function_call=None, role=None, tool_calls=None
                    ),
                    finish_reason=None,
                    index=0,
                    logprobs=None,
                )
            ],
            created=CREATED,
            model="gpt-3.5-turbo-0125",
            object="chat.completion.chunk",
            system_fingerprint="fp_3bc1b5746c",
        ),
        ChatCompletionChunk(
            id=COMPLETION_ID,
            choices=[
                Choice(
                    delta=ChoiceDelta(
                        content=" tasks", function_call=None, role=None, tool_calls=None
                    ),
                    finish_reason=None,
                    index=0,
                    logprobs=None,
                )
            ],
            created=CREATED,
            model="gpt-3.5-turbo-0125",
            object="chat.completion.chunk",
            system_fingerprint="fp_3bc1b5746c",
        ),
        ChatCompletionChunk(
            id=COMPLETION_ID,
            choices=[
                Choice(
                    delta=ChoiceDelta(
                        content=" and", function_call=None, role=None, tool_calls=None
                    ),
                    finish_reason=None,
                    index=0,
                    logprobs=None,
                )
            ],
            created=CREATED,
            model="gpt-3.5-turbo-0125",
            object="chat.completion.chunk",
            system_fingerprint="fp_3bc1b5746c",
        ),
        ChatCompletionChunk(
            id=COMPLETION_ID,
            choices=[
                Choice(
                    delta=ChoiceDelta(
                        content=" provide",
                        function_call=None,
                        role=None,
                        tool_calls=None,
                    ),
                    finish_reason=None,
                    index=0,
                    logprobs=None,
                )
            ],
            created=CREATED,
            model="gpt-3.5-turbo-0125",
            object="chat.completion.chunk",
            system_fingerprint="fp_3bc1b5746c",
        ),
        ChatCompletionChunk(
            id=COMPLETION_ID,
            choices=[
                Choice(
                    delta=ChoiceDelta(
                        content=" information",
                        function_call=None,
                        role=None,
                        tool_calls=None,
                    ),
                    finish_reason=None,
                    index=0,
                    logprobs=None,
                )
            ],
            created=CREATED,
            model="gpt-3.5-turbo-0125",
            object="chat.completion.chunk",
            system_fingerprint="fp_3bc1b5746c",
        ),
        ChatCompletionChunk(
            id=COMPLETION_ID,
            choices=[
                Choice(
                    delta=ChoiceDelta(
                        content=".", function_call=None, role=None, tool_calls=None
                    ),
                    finish_reason=None,
                    index=0,
                    logprobs=None,
                )
            ],
            created=CREATED,
            model="gpt-3.5-turbo-0125",
            object="chat.completion.chunk",
            system_fingerprint="fp_3bc1b5746c",
        ),
        ChatCompletionChunk(
            id=COMPLETION_ID,
            choices=[
                Choice(
                    delta=ChoiceDelta(
                        content=None, function_call=None, role=None, tool_calls=None
                    ),
                    finish_reason="stop",
                    index=0,
                    logprobs=None,
                )
            ],
            created=CREATED,
            model="gpt-3.5-turbo-0125",
            object="chat.completion.chunk",
            system_fingerprint="fp_3bc1b5746c",
        ),
    ]


def zip_choices(
    chunks1: typing.List[ChatCompletionChunk],
    chunks2: typing.List[ChatCompletionChunk],
    append_text: typing.Optional[str] = None,
    drop_indexes: typing.Optional[typing.Set[int]] = None,
    finish_reason: FinishReason = "stop",
) -> typing.List[ChatCompletionChunk]:
    """Zips chunks2 into chunks1, overwriting the choices in chunks1."""
    if not drop_indexes:
        drop_indexes = set()
    if len(chunks1) != len(chunks2):
        raise ValueError("Chunks must have the same length")
    if len(chunks1) == 0:
        return []

    for i, chunk in enumerate(chunks1):
        if i in drop_indexes:
            continue
        mixin_choice = chunks2[i].choices[0]
        mixin_choice.index = len(chunk.choices)
        if append_text and mixin_choice.delta.content is not None:
            mixin_choice.delta.content += append_text
        chunk.choices.append(mixin_choice)

    chunks1[-1].choices[1].finish_reason = finish_reason

    return chunks1


def new_chat_completion() -> ChatCompletion:
    return ChatCompletion(
        id=COMPLETION_ID,
        choices=[
            CompletionChoice(
                finish_reason="stop",
                index=0,
                logprobs=None,
                message=ChatCompletionMessage(
                    # pylint: disable=line-too-long
                    content="No, I am not sentient. I am a computer program designed to assist with tasks and provide information.",
                    role="assistant",
                    function_call=None,
                    tool_calls=None,
                ),
            )
        ],
        created=CREATED,
        model="gpt-3.5-turbo-0125",
        object="chat.completion",
        system_fingerprint="fp_fa89f7a861",
        usage=CompletionUsage(completion_tokens=21, prompt_tokens=11, total_tokens=32),
    )
