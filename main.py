from discord import client
import Database
import os
import discord
import private
from Commands import execute_command, add_player

intents = discord.Intents.default()
intents.members = True
client = discord.Client( intents = intents )

@client.event
async def on_ready():
	print('Logged on as {0.user}'.format(client))
	private.db_connection = Database.create_db_connection ( private.DatabaseHost, private.DatabaseUser, private.DatabasePassword, private.DatabaseName )

@client.event
async def on_message( message ):
	if message.content.startswith ( private.COMMANDSYNTAX ):
		await execute_command ( message )

@client.event
async def on_reaction_add ( reaction, user ):
	if user.id != private.botId and private.LastScrim != None:
		if reaction.message.id == private.LastScrim.id and reaction.emoji == '👍':
			await add_player ( user )
client.run ( private.TOKEN ) 