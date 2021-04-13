import discord
from discord import message
import private
from Database import execute_query, read_query
import random

scrim_message = ''

async def __init ( command ):
	async for member in command.guild.fetch_members ( limit = None ):
		sql = """
		SELECT discord_id
		FROM MMR
		WHERE discord_id = {}
		""".format ( member.id )
		data = read_query ( private.db_connection, sql )
		data = data[2:-2]
		if data == None:
			sql = """
			INSERT INTO MMR ( discord_id, discord_name, MMR, Wins, Loses )
			VALUES ( '{}', '{}', '{}', '{}', '{}' )
			""".format ( member.id, member.name, private.defaultMMR, 0, 0 )
			execute_query ( private.db_connection, sql )
	
	await command.reply ( 'Registered all the new members!', mention_author = False )

async def __setMmr ( command ):
	msg = command.content.split( " " )
	member_id = msg[1][3:-1]
	mmr = msg[2]
	sql = """
	SELECT discord_id
	FROM MMR
	WHERE discord_id = {}
	""".format ( member_id )
	data = read_query ( private.db_connection, sql )
	result = ''
	for x in data:
		result += str ( x )
	if result[1:-1] != '': 
		sql = """
		UPDATE MMR
		SET MMR = {}
		WHERE discord_id = {}
		""".format ( mmr, member_id )
		execute_query ( private.db_connection, sql )
		await command.reply ( 'Succesfully changed the mmr to {}!'.format ( mmr ), mention_author = False )
	else:
		await command.reply ( 'The mentioned user is not registered or you did not ping a member, use to --init to update with all the new members', mention_author = False )

async def __mmr ( command ):
	member_id = command.author.id
	sql = """
	SELECT MMR
	FROM MMR
	WHERE discord_id = {}
	""".format ( member_id )
	data = read_query ( private.db_connection, sql )
	result = ''
	for x in data:
		result += str ( x )
	if data != None:
		await command.reply ( 'Your MMR is : {}'.format ( result[1:-2] ),  mention_author = False )
	else:
		await command.reply ( 'You are not registered, use to --init to update with all the new members', mention_author = False )

async def __getMmrList ( command ):
	sql = """
	SELECT discord_name, MMR, Wins, Loses
	FROM MMR
	"""
	data = read_query ( private.db_connection, sql )
	message = ''
	for x in data:
		message += str ( x ) + '\n'
	send = """
	```
	{}
	```
	""".format ( message )
	await command.reply ( 'Check your dms', mention_author = False )
	await command.author.send ( send )
	
async def __startScrim ( command ):
	scrim_id = random.randint ( 100000, 999999 )
	message_content = ''
	message_content += """
	The Scrim id is : {}
	Type 'join' to join the current scrim
	Players are :
	""".format ( scrim_id )
	players = ''
	message = await command.channel.send ( message_content )
	print ( message.content )
	def check ( m ):
		return m.content == 'join'
	for _ in range ( 0, 8 ):
		user = await private.client.wait_for ( 'message', check = check )
		message_content += str ( user.name ) + ' '
		players += str ( user.name ) + ', '
		sql = """
		SELECT MMR
		FROM MMR
		WHERE discord_id = {}
		""".format ( user.id )
		data = read_query ( private.db_connection, sql )
		data = str ( data )
		message_content += data[2:-3]
		await message.edit ( message_content )
		print ( message_content )
	sql = """
	INSERT INTO SCRIMS ( scrim_id, players, finished )
	VALUES ( '{}', '{}', '{}' )
	""".format ( scrim_id, players, False )
	execute_query ( private.db_connection, sql )

async def __endScrim ( command ):
	msg = command.content.split()
	ongoingScrims.pop ( msg[1] )

async def execute_command( command ):
	msg = command.content
	if msg.startswith( private.COMMANDSYNTAX + "init" ):
		await __init ( command )
	elif msg.startswith ( private.COMMANDSYNTAX + 'MMR' ):
		await __mmr ( command )
	elif msg.startswith( private.COMMANDSYNTAX + "setMMR" ):
		if "admin" in [x.name.lower() for x in command.author.roles] or command.author.id == private.OwnerID:
			await __setMmr ( command )
		else:
			await command.reply ( "You need to be an admin to use that command!", mention_author = False )
	elif msg.startswith( private.COMMANDSYNTAX + "getMMRList" ):
		if "admin" in [x.name.lower() for x in command.author.roles] or command.author.id == private.OwnerID:
			await __getMmrList ( command )
		else:
			await command.reply ( "You need to be an admin to use that command!", mention_author = False )
	elif msg.startswith( private.COMMANDSYNTAX + "start scrim" ):
		await __startScrim ( command )
	elif msg.startswith ( private.COMMANDSYNTAX + "end scrim"):
		__endScrim ( command )