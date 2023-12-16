import uuid
from datetime import datetime
from typing import Union

from .conversation_style import CONVERSATION_STYLE_TYPE, ConversationStyle
from .utilities import get_location_hint_from_locale, get_ran_hex, guess_locale

BING_BLOB_URL = "https://copilot.microsoft.com/images/blob?bcid="


class ChatHubRequest:
    def __init__(
        self,
        conversation_signature: str,
        encrypted_conversation_signature: str,
        client_id: str,
        conversation_id: str,
        invocation_id: int = 3,
    ) -> None:
        self.struct: dict = {}

        self.client_id: str = client_id
        self.conversation_id: str = conversation_id
        self.conversation_signature: str = conversation_signature
        self.encrypted_conversation_signature: str = encrypted_conversation_signature
        self.invocation_id: int = invocation_id

    def update(
        self,
        prompt: str,
        conversation_style: CONVERSATION_STYLE_TYPE,
        webpage_context: Union[str, None] = None,
        search_result: bool = False,
        locale: str = guess_locale(),
        attachment_info: dict | None = None,
        mode: str = None,
        no_search: bool = True,
    ) -> None:
        options = [
            "deepleo",
            "enable_debug_commands",
            "disable_emoji_spoken_text",
            "enablemm",
        ]
        if conversation_style:
            if not isinstance(conversation_style, ConversationStyle):
                conversation_style = getattr(ConversationStyle, conversation_style)
            options = conversation_style.value
        #enable gpt4_turbo
        if mode == 'gpt4-turbo':
            options.append('dlgpt4t')
        
        if no_search:
            options.append('nosearchall')

        message_id = str(uuid.uuid4())
        # Get the current local time
        now_local = datetime.now()

        # Get the current UTC time
        now_utc = datetime.utcnow()

        # Calculate the time difference between local and UTC time
        timezone_offset = now_local - now_utc

        # Get the offset in hours and minutes
        offset_hours = int(timezone_offset.total_seconds() // 3600)
        offset_minutes = int((timezone_offset.total_seconds() % 3600) // 60)

        # Format the offset as a string
        offset_string = f"{offset_hours:+03d}:{offset_minutes:02d}"

        # Get current time
        timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S") + offset_string
        image_url, original_image_url = None, None

        if attachment_info:
            image_url = BING_BLOB_URL + attachment_info["blobId"]
            original_image_url = BING_BLOB_URL + attachment_info["blobId"]

        self.struct = {
            "arguments": [
                {
                    "source": "cib",
                    "scenario": "SERP",
                    "optionsSets": options,
                    "allowedMessageTypes": [
                        "ActionRequest",
                        "Chat",
                        "Context",
                        "InternalSearchQuery",
                        "InternalSearchResult",
                        "Disengaged",
                        "InternalLoaderMessage",
                        "Progress",
                        "RenderCardRequest",
                        "AdsQuery",
                        "SemanticSerp",
                        "GenerateContentQuery",
                        "SearchQuery",
                    ],
                    "sliceIds": [
                        "winmuid1tf",
                        "newmma-prod",
                        "imgchatgptv2",
                        "tts2",
                        "voicelang2",
                        "anssupfotest",
                        "emptyoson",
                        "tempcacheread",
                        "temptacache",
                        "ctrlworkpay",
                        "winlongmsg2tf",
                        "628fabocs0",
                        "531rai268s0",
                        "602refusal",
                        "621alllocs0",
                        "621docxfmtho",
                        "621preclsvn",
                        "330uaug",
                        "529rweas0",
                        "0626snptrcs0",
                        "619dagslnv1nr"
                    ],
                    "verbosity": "verbose",
                    "traceId": get_ran_hex(32),
                    "isStartOfSession": self.invocation_id == 3,
                    "message": {
                        "locale": locale,
                        "market": locale,
                        "region": locale[-2:],  # en-US -> US
                        "locationHints": get_location_hint_from_locale(locale),
                        "timestamp": timestamp,
                        "author": "user",
                        "inputMethod": "Keyboard",
                        "text": prompt,
                        "messageType": "Chat",
                        "messageId": message_id,
                        "requestId": message_id,
                        "imageUrl": image_url,
                        "originalImageUrl": original_image_url,
                    },
                    "tone": conversation_style.name.capitalize(),  # Make first letter uppercase
                    "spokenTextMode": "None",
                    "requestId": message_id,
                    "conversationSignature": self.conversation_signature,
                    "encryptedConversationSignature": self.encrypted_conversation_signature,
                    "participant": {
                        "id": self.client_id,
                    },
                    "conversationId": self.conversation_id,
                },
            ],
            "invocationId": str(self.invocation_id),
            "target": "chat",
            "type": 4,
        }
        if (not no_search) and (search_result):
            have_search_result = [
                "InternalSearchQuery",
                "InternalSearchResult",
                "InternalLoaderMessage",
                "RenderCardRequest",
            ]
            self.struct["arguments"][0]["allowedMessageTypes"] += have_search_result
        if webpage_context:
            self.struct["arguments"][0]["previousMessages"] = [
                {
                    "author": "user",
                    "description": webpage_context,
                    "contextType": "WebPage",
                    "messageType": "Context",
                    "messageId": "discover-web--page-ping-mriduna-----",
                },
            ]
        self.invocation_id += 1

        # print(timestamp)
