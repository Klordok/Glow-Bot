
import discord
import urllib
import json

def get_catfact():
    site_data = urllib.request.urlopen('https://catfact.ninja/fact')
    jsonPart = site_data.read().decode("utf-8")
    fact_data = json.loads(jsonPart)
    return fact_data['fact']

with open("D:/GitHub/Discord Bot/tokens.txt") as f:
	file_content = f.read()

token = file_content.strip()


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))
            
        if message.content.startswith('!catfact'):
            await message.channel.send(get_catfact())

client = MyClient()

client.run(token)