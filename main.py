import os
import discord
import private
from Commands import executeCommand

class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged on as', self.user)

	async def on_message( ctx, message ):
		if message.content.startswith ( ctx, commandSyntax ):
			executeCommand ( message )

client = MyClient()
client.run( private.TOKEN )