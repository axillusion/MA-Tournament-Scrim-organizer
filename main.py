from discord import client
import Database
import os
import discord
import private
from Commands import execute_command

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

client.run ( private.TOKEN ) 