
import discord
from discord.ext import commands, tasks
import os
import random
from itertools import cycle
import json

the_list = ['hello', 'yesssss']
cybercount = 5

arkcount = 0

shadowcount = 0

hyrdacount = 0

catching = False

poke_list = ['mega charizard x', 'mega charizard y', 'lucario', 'rayquaza', 'pikachu', 'dragonite', 'charmander', 'charizard', 'mewtwo', 'greninja', 'charmeleon', 'mega blaziken']

#poke_list = []

final = 'pokemon'

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


  

client = commands.Bot(command_prefix = get_prefix)

#-------

@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '.'

    with open ('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open ('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


@client.command()
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix
    await ctx.send (f'Changed prefix to {prefix}')

    with open ('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.command()
async def start(ctx):
    person = ctx.author.id
    with open('test.json', 'r') as f:
        test = json.load(f)
    test[str(person)] = 0
    await ctx.send('Started your adventure')
    with open ('test.json', 'w') as f:
        json.dump(test, f, indent=4)
    #--
    with open('polist.json', 'r') as f:
        pol = json.load(f)
    pol[person] = []
    with open ('polist.json', 'w') as f:
        json.dump(pol, f, indent=4)
        



    


    
def image_spawn(poke):
    global final
    if poke == "charmander":
        final = 'https://cdn.bulbagarden.snet/upload/7/73/004Charmander.png'
        
    elif poke == "charizard":
        final = 'https://cdn.bulbagarden.net/upload/thumb/7/7e/006Charizard.png/1200px-006Charizard.png'

    elif poke == "charmeleon":
        final = 'https://live.staticflickr.com/8332/8445334961_fa3df984f3_c.jpg'

    elif poke == "mewtwo":
        final = 'https://cdn.bulbagarden.net/upload/thumb/7/78/150Mewtwo.png/1200px-150Mewtwo.png'
        
    elif poke == "greninja":
        final = 'https://vignette.wikia.nocookie.net/characterprofile/images/4/46/Greninja%2C_the_Ninja_Pokemon.png/revision/latest?cb=20170914211357'
        

    elif poke == "pikachu":
        final = 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/f91279e6-bcd2-45ab-aa9a-da8370953c52/daajzx2-a4ba3c36-a3e3-48a7-bfbc-a4b8a2cbc1ef.jpg/v1/fill/w_800,h_1018,q_75,strp/pikachu_by_disse86_daajzx2-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3siaGVpZ2h0IjoiPD0xMDE4IiwicGF0aCI6IlwvZlwvZjkxMjc5ZTYtYmNkMi00NWFiLWFhOWEtZGE4MzcwOTUzYzUyXC9kYWFqengyLWE0YmEzYzM2LWEzZTMtNDhhNy1iZmJjLWE0YjhhMmNiYzFlZi5qcGciLCJ3aWR0aCI6Ijw9ODAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.gtw7j2k7fCIQOBi4KnojqttQ6XYqJeKDbJ3sZLDKnf8'    

    elif poke == "mega blaziken":
        final = 'https://sg.portal-pokemon.com/play/resources/pokedex/img/pm/2d68fc9cdab6d79725910a7a28a14443fccec48e.png'

    elif poke == "lucario":
        final = 'https://cdn.bulbagarden.net/upload/thumb/d/d7/448Lucario.png/1200px-448Lucario.png'

    elif poke == "rayquaza":
        final = "https://cdn.bulbagarden.net/upload/thumb/e/e4/384Rayquaza.png/1200px-384Rayquaza.png"

    elif poke == "dragonite":
        final = 'https://cdn.bulbagarden.net/upload/8/8b/149Dragonite.png'
        
    elif poke == "mega charizard x":
        final = 'https://i.pinimg.com/originals/a7/a2/c4/a7a2c4ff3772516835ebc3a7ad60c355.png'

    elif poke == "mega charizard y":
        final = 'https://www.kindpng.com/picc/m/264-2645478_mega-charizard-y-mega-charizard-y-png-transparent.png'

        

    
client.remove_command('help')
@client.event
async def on_ready():
    
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f'Hey there! My prefix is .'))
    
    print('Bot is ready.')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {client.latency * 1000}ms')
        
        
@client.command()
async def creator(ctx):
    await ctx.send('My creator is Abish yup hes awesome ik')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['Yessss', 'Nope', 'Ofcourse', 'Never', 'Nahhhh Braaah (Tanish)', 'Duh']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def hello(ctx):
    await ctx.send('hey there')

                   
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send (f'Kicked {member.mention}')

        

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send (f'Banned {member.mention}')
    

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
            return



@client.command()
async def image(ctx):
    await ctx.channel.send('Hello', file=discord.File('cool.jpg'))




@client.command()
async def spawn(ctx):
    global pokespawn, poke_list, catching, final
    pokespawn = random.choice(poke_list)
    image_spawn(pokespawn)
    await ctx.send('A pokemon spawned')
    await ctx.send(final )
    catching = True


@client.command()
async def catch(ctx, *, pokemon):
    global pokespawn, poke_list, catching
    if catching == True:
        if pokemon == pokespawn:
            person = ctx.author.mention
            await ctx.send( f'{person} you caught a {pokespawn}')
            num = ctx.author.id
            with open('test.json', 'r') as f:
                test = json.load(f)

            getter = test[str(num)]

            getter = int(getter)
            getter += 1
            
            with open('test.json', 'r') as f:
                test = json.load(f)

            test[str(num)] = getter

            with open ('test.json', 'w') as f:
                json.dump(test, f, indent=4)

            #-----------------------------------
            #personlist = "sup"
            with open('polist.json', 'r') as f:
                pol = json.load(f)
            pokelist = pol[str(num)]
            pokelist.append(pokespawn)
            pol[str(num)] = pokelist
            with open ('polist.json', 'w') as f:
                json.dump(pol, f, indent=4)

            
            
            
            
            catching = False
            
        else:
            await ctx.send(f'Wrong pokemon')
    else:
        await ctx.send('No pokemon has spawned')

@client.command()
async def pokenumber(ctx):
    person = ctx.author.id
    with open('test.json', 'r') as f:
        test = json.load(f)

    getter = test[str(person)]

    await ctx.send(f'You have {getter} pokemon')

    
@client.command()
async def pokelist(ctx):
    person = ctx.author.id
    with open('polist.json', 'r') as f:
        pol = json.load(f)

    getter = pol[str(person)]

    await ctx.send(f'Your pokemon are:\n{getter}')
    

        
@client.command()
async def id(ctx):
    person = ctx.author.id
    await ctx.send(person)
    
    
    
    

@client.command()
async def kiu(ctx, member = 'someone'):
    await ctx.send(f'OK kiued {member}')


@client.command()
async def linktest (ctx):
    await ctx.send('')


@client.command()
async def say(ctx, *context):
    await ctx.channel.purge(limit=1)
    
    await ctx.send(' '.join(map(str, context)))

@client.command()
async def help(ctx):
    embed = discord.Embed(color = ctx.author.color, timestamp = ctx.message.created_at)

    embed.set_author(name="Help Commands")

    embed.add_field(name="fun", value="Have a fun time, ask questions, play games, kiu people and much more!", inline=False)
    embed.add_field(name="mod", value="Moderate and manage your server, ban, kick, mute with simple commands!", inline=False)
    embed.add_field(name="pokemon", value="Catch, battle and train pokemon, have a fun time with the pokemon commands!", inline=False)
    embed.add_field(name="more", value="Some extra super helpful and fun commands you could use", inline=False)


    await ctx.send(embed=embed)

@client.command()
async def fun(ctx):
    embed = discord.Embed(color = ctx.author.color, timestamp = ctx.message.created_at)

    embed.set_author(name="Fun Commands")
              
    embed.add_field(name="play <move>", value="Play rock paper scissors against the bot, choose one of the moves", inline=False)
    embed.add_field(name="say <something>", value="Make the bot say something and then immediately delete you message", inline=False)
    embed.add_field(name="kiu <member>", value="Kiu someone, something random or maybe a fellow member... (kill ofc)", inline=False)
    embed.add_field(name="8ball <question>", value="Ask a question to the mysterious 8ball to get some answers", inline=False)

    await ctx.send(embed=embed)



@client.command()
async def mod(ctx):
    embed = discord.Embed(color = ctx.author.color, timestamp = ctx.message.created_at)

    embed.set_author(name="Mod commands")
              
    embed.add_field(name="kick <member> <reason>", value="Use this command to kick members", inline=False)
    embed.add_field(name="clear <amount>", value="Clear/delete earlier messages, not specifing an amount will delete 5 messages.", inline=False)
    embed.add_field(name="ban <member> <reason>", value="Use this command to ban members", inline=False)
    embed.add_field(name="unban <member>", value="Use this command to unban members", inline=False)

    await ctx.send(embed=embed)


@client.command()
async def play(ctx, *, move):
    cmoves = ['rock', 'paper', 'scissors']
    cmove = random.choice(cmoves)

    
    if move == cmove:
        await ctx.send(f'You used: {move}\nShade used: {cmove}')
        await ctx.send("the match is  a draw")
    elif move == "rock" and cmove == "scissors":
        await ctx.send(f'You used: {move}\nShade used: {cmove}')
        await ctx.send(f'{ctx.author.mention} wins')
    elif move == "rock" and cmove == "paper":
        await ctx.send(f'You used: {move}\nShade used: {cmove}')
        await ctx.send(f'Shade wins')
    elif move == "paper" and cmove == "rock":
        await ctx.send(f'You used: {move}\nShade used: {cmove}')
        await ctx.send(f'{ctx.author.mention} wins')
    elif move == "paper" and cmove == "scissors":
        await ctx.send(f'You used: {move}\nShade used: {cmove}')
        await ctx.send(f'Shade wins')
    elif move == "scissors" and cmove == "paper":
        await ctx.send(f'You used: {move}\nShade used: {cmove}')
        await ctx.send(f'{ctx.author.mention} wins')
    elif move == "scissors" and cmove == "rock":
        await ctx.send(f'You used: {move}\nShade used: {cmove}')
        await ctx.send(f'Shade wins')
    else:
        await ctx.send('Choose from rock, paper or scissors')

    


client.run('NzQwMjIzNTU1MDM1MjAxNTY3.Xyl46A.c9kmwJtwe8VgQUIIslAloJzMR6Q')


charizardimage = 'https://cdn.bulbagarden.net/upload/thumb/7/7e/006Charizard.png/1200px-006Charizard.png'

"""
@client.event
async def on_member_join(member):
    print(f'{member} has joined a server')


@client.event
async def on_member_remove(member):
          print(f'{member} has left a server')


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


    #@client.event
#async def on_command_error(ctx, error):
   # if isisntance(error, commands.MissingRequiredArgument):
       # await ctx.send('Please pass in all required arguments')
