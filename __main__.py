import discord
from dotenv import load_dotenv
import os




load_dotenv()
token = str(os.getenv("TOKEN"))

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True


print(token)
client = MyClient(intents=intents)
client.run(token)
