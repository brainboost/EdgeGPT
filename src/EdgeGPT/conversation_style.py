from enum import Enum

try:
    from typing import Literal, Union
except ImportError:
    from typing_extensions import Literal
from typing import Optional

_BASE_OPTION_SETS = [
    "nlu_direct_response_filter",
    "deepleo",
    "disable_emoji_spoken_text",
    "responsible_ai_policy_235",
    "enablemm",
    "iycapbing",
    "iyxapbing",
    "dv3sugg",
    "iyoloxap",
    "iyoloneutral",
    "gencontentv3",
    "nojbf",
]

class ConversationStyle(Enum):
    creative = _BASE_OPTION_SETS + ["h3imaginative"]
    balanced = _BASE_OPTION_SETS + ["galileo"]
    precise = _BASE_OPTION_SETS + ["h3precise"]



CONVERSATION_STYLE_TYPE = Optional[
    Union[ConversationStyle, Literal["creative", "balanced", "precise"]]
]
