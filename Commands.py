import discord
import private
from Database import execute_query, read_query

ongoingScrims = []
players = []
playersCount = []
lastscrim = -1;

async def __init ( command ):
	async for member in command.guild.fetch_members ( limit = None ):
		sql = """
		SELECT discord_id
		FROM MMR
		WHERE discord_id = {}
		""".format ( member.id )
		data = read_query ( private.db_connection, sql )
		if data == None:
			sql = """
			INSERT INTO MMR ( discord_id, discord_name, MMR, Wins, Loses )
			VALUES ( '{}', '{}', '{}', '{}', '{}' )
			""".format ( member.id, member.name, private.defaultMMR, 0, 0 )
			execute_query ( private.db_connection, sql )
		
def __setMmr ( command ):
	msg = command.content.split( " " )
	name = msg[1]
	mmr = msg[2]
	for member in private.memberList:
		if private.memberList[member].name == name:
			private.memberMMR[member] = mmr

def __startScrim ( command ):
	players.clear()
	playerCount = 0

def __endScrim ( command ):
	msg = command.content.split()
	ongoingScrims.pop ( msg[1] )

async def executeCommand( command ):
	msg = command.content
	if msg.startswith( private.COMMANDSYNTAX + "init" ):
		await __init ( command )
	elif msg.startswith( private.COMMANDSYNTAX + "setMMR" ):
		if "admin" in [x.name.lower() for x in command.author.roles] or command.author.name == "IlluSion":
			__setMmr ( command )
		else:
			await client.send_message ( command.channel, "You need to be an admin to use that command" )
	elif msg.startswith( private.COMMANDSYNTAX + "start scrim" ):
		__startScrim ( command )
	elif msg.startswith ( private.COMMANDSYNTAX + "join" ):
		players.append ( command.author.name )
		playerCount += 1
		if playersCount == 8:
			await client.send_message ( command.channel, "Scrim starting!\nTeam 1:" + players[0] + " & " + players[1] + "\n" + "Team 2:" + players[2] + " & " + players[3] + "\n" + "Team 3:" + players[4] + " & " + players[5] + "\n" + "Team 4:" + players[6] + " & " + players[7] + "\n")
	elif msg.startswith ( private.COMMANDSYNTAX + "end scrim"):
		__endScrim ( command )



		



