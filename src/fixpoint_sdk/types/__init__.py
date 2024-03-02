"""Type definitions for the Fixpoint SDK."""

from dataclasses import dataclass, asdict
import enum
from typing import Any, Dict, List, Optional, TypedDict
from openai.types.chat import ChatCompletionMessageParam


class ThumbsReaction(enum.Enum):
    """The specific user feedback reaction."""
    THUMBS_UNSPECIFIED = 0
    THUMBS_UP = 1
    THUMBS_DOWN = 2


class OriginType(enum.Enum):
    """The origin of a user feedback.

    User feedback can come from end-users, or it can come from the developers of
    the LLM deployment being monitored.
    """
    ORIGIN_UNSPECIFIED = 0
    ORIGIN_USER_FEEDBACK = 1
    ORIGIN_ADMIN = 2


@dataclass
class CreateLLMInputLogRequest:
    """Request to create a log of a chat completion input."""
    model_name: str
    messages: List[ChatCompletionMessageParam]
    user_id: Optional[str] = None
    temperature: Optional[float] = None
    trace_id: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert this request to a dictionary."""
        return asdict(self)


class OpenAILLMInputLog(TypedDict):
    """An input log with attributes from OpenAI response.

    This input log has some attributes that come directly from an OpenAI
    response. Some of the field names are slightly off from what our Fixpoint
    API expects, so we need to transform this to a `CreateLLMInputLogRequest`.
    """
    model: str
    messages: List[ChatCompletionMessageParam]
    user: Optional[str]
    temperature: Optional[float]
    trace_id: Optional[str]


# TODO(dbmikus) this is an incomplete definition.
class InputLog(TypedDict):
    """An LLM input log."""
    name: str


# TODO(dbmikus) this is an incomplete definition.
class OutputLog(TypedDict):
    """An LLM output log."""
    name: str


class UserFeedbackLike(TypedDict):
    """A user feedback like."""
    log_name: str
    thumbs_reaction: ThumbsReaction
    user_id: str
    origin: OriginType


class CreateUserFeedbackRequest(TypedDict):
    """Request to create a user feedback."""
    likes: List[UserFeedbackLike]


class CreateUserFeedbackResponse(TypedDict):
    """Response to a CreateUserFeedbackRequest."""
    success: bool


class LogAttribute(TypedDict):
    """A log attribute."""""
    log_name: str
    key: str
    value: str


class CreateLogAttributeRequest(TypedDict):
    """Request to create a log attribute."""
    log_attribute: LogAttribute
