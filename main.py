import os
import discord
import private
import Commands

class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged on as', self.user)

	async def on_message( ctx, message ):
		if message.content.startswith ( private.COMMANDSYNTAX ):
			await Commands.executeCommand ( ctx, message )

client = MyClient()
client.run( private.TOKEN )