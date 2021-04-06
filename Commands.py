import discord
import private

def __init ( command ):
	memberList = command.guild.members
	for member in memberList:
		memberMMR[member] = defaultMMR

def executeCommand( command ):
	if command.content.startswith( commandSyntax + "init" ):
		__init ( command )


