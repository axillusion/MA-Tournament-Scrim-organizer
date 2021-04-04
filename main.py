import os
import discord
import private

client = discord.Client()
memberList = []
memberMMR = []
command = '--'
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
client.run( private.TOKEN )