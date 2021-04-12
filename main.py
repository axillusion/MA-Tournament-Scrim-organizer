import Database
import os
import discord
import private
from Commands import executeCommand

db_connection = None

class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged on as', self.user)
		db_connection = Database.create_db_connection ( private.DatabaseHost, private.DatabaseUser, private.DatabasePassword, private.DatabaseName )

	async def on_message( ctx, message ):
		if message.content.startswith ( private.COMMANDSYNTAX ):
			await executeCommand ( ctx, message )

client = MyClient()
client.run( private.TOKEN )