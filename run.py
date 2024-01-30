import asyncio
import json

from src.EdgeGPT.EdgeGPT import Chatbot, ConversationStyle


async def async_main() -> None:
    """
    Main function
    """
    print("Initializing...")
    print("Enter `alt+enter` or `escape+enter` to send a message")
    # Read and parse cookies
    cookies = json.loads(
        open("C:\\Users\\Codete\\.config\\bing-cookies.json", encoding="utf-8").read()
    )
    bot = await Chatbot.create(cookies=cookies)
    response = await bot.ask(
        prompt="what parameters can be used in prompts with DALLE-3 in Bing Image Creator and for what purpose?",
        conversation_style=ConversationStyle.balanced,
        simplify_response=True,
    )
    await bot.close()
    print(json.dumps(response, indent=2))


asyncio.run(async_main())
