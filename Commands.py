import discord
import private

ongoingScrims = []
players = []
playersCount = []
lastscrim = -1;

def __init ( command ):
	memberList = command.guild.members
	for member in memberList:
		memberMMR[member] = defaultMMR

def __setMMR ( command ):
	msg = command.content.split( " " )
	name = msg[1]
	mmr = msg[2]
	for member in memberList:
		if memberList[member].name == name:
			memberMMR[member] = mmr

def __startScrim ( command ):
	players.clear()
	playerCount = 0

def __endScrim ( command ):
	msg = command.content.split()
	ongoingScrims.pop ( msg[1] )

async def executeCommand( ctx, command ):
	msg = command.content
	if msg.startswith( commandSyntax + "init" ):
		__init ( command )
	elif msg.startswith( commandSyntax + "setMMR" ):
		if "admin" in [x.name.lower() for x in command.author.roles] or command.author.name == "IlluSion":
			__setMMR ( command )
		else:
			await client.send_message ( ctx.message.channel, "You need to be an admin to use that command" )
	elif msg.startswith( commandSyntax + "start scrim" ):
		__startScrim ( command )
	elif msg.startswith ( commandSyntax + "join" ):
		players.append ( command.author.name )
		playerCount += 1
		if playersCount == 8:
			await client.send_message ( ctx.message.channel, "Scrim starting!\nTeam 1:" + players[0] + " & " + players[1] + "\n" + "Team 2:" + players[2] + " & " + players[3] + "\n" + "Team 3:" + players[4] + " & " + players[5] + "\n" + "Team 4:" + players[6] + " & " + players[7] + "\n")
	elif msg.startswith ( commandSyntax + "end scrim"):
		__endScrim ( command )



		



