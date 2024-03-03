from dataclasses import dataclass, asdict
import enum
from typing import Any, Dict, List, Optional, TypedDict
from openai.types.chat import ChatCompletionMessageParam


class ThumbsReaction(enum.Enum):
  THUMBS_UNSPECIFIED = 0
  THUMBS_UP = 1
  THUMBS_DOWN = 2


class OriginType(enum.Enum):
  ORIGIN_UNSPECIFIED = 0
  ORIGIN_USER_FEEDBACK = 1
  ORIGIN_ADMIN = 2


@dataclass
class CreateLLMInputLogRequest:
    model_name: str
    messages: List[ChatCompletionMessageParam]
    user_id: Optional[str] = None
    temperature: Optional[float] = None
    trace_id: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class OpenAILLMInputLog(TypedDict):
    model: str
    messages: List[ChatCompletionMessageParam]
    user: Optional[str]
    temperature: Optional[float]
    trace_id: Optional[str]


# TODO(dbmikus) this is an incomplete definition.
class InputLog(TypedDict):
    name: str


# TODO(dbmikus) this is an incomplete definition.
class OutputLog(TypedDict):
    name: str


class UserFeedbackLike(TypedDict):
    log_name: str
    thumbs_reaction: ThumbsReaction
    user_id: str
    origin: OriginType


class CreateUserFeedbackRequest(TypedDict):
    likes: List[UserFeedbackLike]


class CreateUserFeedbackResponse(TypedDict):
    success: bool


class LogAttribute(TypedDict):
    log_name: str
    key: str
    value: str


class CreateLogAttributeRequest(TypedDict):
    log_attribute: LogAttribute
