import discord
import private

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

async def executeCommand( ctx, command ):
	msg = command.content
	if msg.startswith( commandSyntax + "init" ):
		__init ( command )
	elif msg.startswith( commandSyntax + "setMMR" ):
		if "admin" in [x.name.lower() for x in command.author.roles] or command.author.name == "IlluSion":
			__setMMR ( command )
		else:
			client.send_message ( ctx.message.channel, "You need to be an admin to use that command" )
		



