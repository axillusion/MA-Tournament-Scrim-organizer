import os
import discord

TOKEN = 'ODI4MjE3MTI2MTMyMzgzNzU0.YGmXTg._NPjqeFRnIjEb6V72VvBBR3yh3c'

client = discord.Client()
memberList = []
memberMMR = []
command = '--'
botId = 4908390289403
defaultMMR = 1000

class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged on as', self.user)

	async def on_message( ctx, message ):
		if message.content.startswith ( command ):
			msg = message.content
			msg.split( '- ' )
			if msg[0] == 'init':
				memberList = message.guild.members
				for member in memberList:
					memberMMR[member] = defaultMMR

client = MyClient()
client.run( TOKEN )