import os
import discord
import private
from Commands import executeCommand

client = discord.Client()

class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged on as', self.user)

	async def on_message( ctx, message ):
		if message.content.startswith ( commandSyntax ):
			executeCommand ( message )

client = MyClient()
client.run( private.TOKEN )