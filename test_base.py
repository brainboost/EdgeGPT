import json
import os

import pytest

from src.EdgeGPT.EdgeGPT import Chatbot, ConversationStyle

pytest_plugins = ("pytest_asyncio",)

from os import getenv

cookies = json.loads(
    open("C:\\Users\\Codete\\.config\\bing-cookies_1.json", encoding="utf-8").read()
)


# @pytest.disable()
@pytest.mark.asyncio()
async def test_ask() -> None:
    bot = await Chatbot.create(cookies=cookies or getenv("EDGE_COOKIES"))
    response = await bot.ask(
        prompt="tell me a joke about cats",
        conversation_style=ConversationStyle.balanced,
        simplify_response=True,
    )
    await bot.close()
    print(json.dumps(response, indent=2))
    assert response
