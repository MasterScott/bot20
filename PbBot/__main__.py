#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Aayush Kumar - @ayushk780


from discord.ext import commands
import discord
import os
import time
from PbBot import (
    BOT_TOKEN,
    Delete_after_duration,
    LOG_CHANNEL_ID
    )
import logging
from datetime import datetime
# for custom help command visit da.gd/VSjOf

if __name__ == "__main__":
    client = commands.Bot(command_prefix='!',
                          description='Made with Love by Simp#0174',
                          case_insensitive=True
                          )
    # await client.change_presence(status=discord.Status.online, activity=discord.Game('samzydev.xyz'))
    
    @commands.has_role('Admin')
    @client.command(name='message',brief='Sends an announcement (only for admins)', description='Sends an announcement (only for admins)', usage='!message' )
	async def on_message:
        embedVar = discord.Embed(title="Announcement", description="Desc", color=0x00ff00)
        embedVar.add_field(name="Field1", value="hi", inline=False)
        embedVar.add_field(name="Field2", value="hi2", inline=False)
        await message.channel.send(embed=embedVar)

    @client.event
    async def on_ready():
        await client.change_presence(status=discord.Status.online, activity=discord.Game('samzydev.xyz'))

    client.run(BOT_TOKEN)
