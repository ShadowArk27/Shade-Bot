
import discord
from discord.ext import commands, tasks
import os
import random
from itertools import cycle
import json
import threading


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
    
    try:
        return prefixes[str(message.guild.id)]
    except:
        return "."


  

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
        final = 'data:image/jpeg;base64,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'
        
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
        final = 'https://sg.portal-pokemon.com/play/resources/pokedex/img/pm/ca3db4aad5c85a525d9be86852b26db1db7a22c0.png'

    elif poke == "mega charizard y":
        final = 'https://sg.portal-pokemon.com/play/resources/pokedex/img/pm/0aa78a0061bda9d88cbb0bbf739cd9cc56522fe9.png'


        

    
client.remove_command('help')
@client.event
async def on_ready():
    
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f'with the Shadows. My prefix is .'))
    
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
@commands.has_permissions(manage_channels=True)
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
async def meme(ctx, template, text1, text2):
    await ctx.send(f'https://api.memegen.link/images/{template}/{text1}/{text2}.png')
    
    
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
async def fun(ctx):
    embed = discord.Embed(color = ctx.author.color, timestamp = ctx.message.created_at)

    embed.set_author(name="Fun Commands")
              
    embed.add_field(name="play <move>", value="Play rock paper scissors against the bot, choose one of the moves", inline=False)
    embed.add_field(name="say <something>", value="Make the bot say something and then immediately delete you message", inline=False)
    embed.add_field(name="kiu <member>", value="Kiu someone, something random or maybe a fellow member... (kill ofc)", inline=False)
    embed.add_field(name="8ball <question>", value="Ask a question to the mysterious 8ball to get some answers", inline=False)

    await ctx.send(embed=embed)


@client.command()     
async def help(ctx, *, para):
    if para == "pokemon":
            embed = discord.Embed(color = ctx.author.color, timestamp = ctx.message.created_at)

            embed.set_author(name="Pokemon Commands")
                      
            embed.add_field(name="start", value="Do this to start your pokemon adventure before you start catching them all. Doing it twice will reset your progress", inline=False)
            embed.add_field(name="spawn", value="Spawn a pokemon that you can catch ", inline=False)
            embed.add_field(name="catch <pokemon>", value="Type the name of the pokemon after catch to catch it", inline=False)
            embed.add_field(name="pokelist", value="View all the pokemon you have caught", inline=False)
            embed.add_field(name="pokenumber", value="View the  number of pokemon you have caught", inline=False)


            await ctx.send(embed=embed)

    elif para == "mod":
        embed = discord.Embed(color = ctx.author.color, timestamp = ctx.message.created_at)

        embed.set_author(name="Mod commands")
                  
        embed.add_field(name="kick <member> <reason>", value="Use this command to kick members", inline=False)
        embed.add_field(name="clear <aiount>", value="Clear/delete earlier messages, not specifing an amount will delete 5 messages.", inline=False)
        embed.add_field(name="ban <member> <reason>", value="Use this command to ban members", inline=False)
        embed.add_field(name="unban <member>", value="Use this command to unban members", inline=False)

        await ctx.send(embed=embed)

#@client.command()
@help.error
async def help_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(color = ctx.author.color, timestamp = ctx.message.created_at)

        embed.set_author(name="Help Categories")

        embed.add_field(name="How to use command", value="Do help and the name of the category you woulf like to view\n\n\n", inline=False)
              
        embed.add_field(name="mod", value="Commands you can use to moderate your server, from kicking and banning to deleting messages.", inline=False)
        embed.add_field(name="fun", value="Try out this commands to have a nice fun time ", inline=False)
        embed.add_field(name="pokemon", value="Start your pokemon adventure, catch em all!!", inline=False)
        embed.add_field(name="more", value="Try out these super cool extra commands :)", inline=False)


        await ctx.send(embed=embed) 
    
def checkKey(dict, key): 
      
    if key in dict.keys(): 
        return True
    else: 
        return False

@client.command()
async def play(ctx, *, move):
    playstate = "eouh"
    cmoves = ['rock', 'paper', 'scissors']
    cmove = random.choice(cmoves)

    
    if move == cmove:
        await ctx.send(f'You used: {move}\nShade used: {cmove}')
        await ctx.send("the match is  a draw")
        playstate = "none"
    elif move == "rock" and cmove == "scissors":
        await ctx.send(f'You used: {move}\nShade used: {cmove}')
        playstate = "win"
    elif move == "rock" and cmove == "paper":
        await ctx.send(f'You used: {move}\nShade used: {cmove}')
        playstate = "lose"
    elif move == "paper" and cmove == "rock":
        await ctx.send(f'You used: {move}\nShade used: {cmove}')
        playstate = "win"
    elif move == "paper" and cmove == "scissors":
        await ctx.send(f'You used: {move}\nShade used: {cmove}')
        playstate = "lose"
    elif move == "scissors" and cmove == "paper":
        await ctx.send(f'You used: {move}\nShade used: {cmove}')
        playstate = "win"
    elif move == "scissors" and cmove == "rock":
        await ctx.send(f'You used: {move}\nShade used: {cmove}')
        playstate = "lose"
    else:
        await ctx.send('Choose from rock, paper or scissors')


    if playstate == "win":
        await ctx.send(f'{ctx.author.mention} wins')
        await ctx.send('You got a point')
        playstate = 'kib'
        person = ctx.author.id
        with open('sps.json', 'r') as f:
            sps = json.load(f)

        try:
            numer = sps[str(person)]
            numer = int(numer)
            numer = (numer + 1)
            numer = str(numer)

            with open('sps.json', 'r') as f:
                    sps = json.load(f)
            sps[str(person)] = numer

            with open ('sps.json', 'w') as f:
                    json.dump(sps, f, indent=4)
            
            playstate = 'ef'

        except:
            with open('sps.json', 'r') as f:
                    sps = json.load(f)
                    
            sps[str(person)] = "1"
            with open ('sps.json', 'w') as f:
                json.dump(sps, f, indent=4)
            playstate = 'ef'



        
    elif playstate == "lose":
        await ctx.send(f'Shade wins')
        playstate = '3e'

        person = ctx.author.id
        with open('sps.json', 'r') as f:
            sps = json.load(f)

        try:
            numer = sps[str(person)]
            numer = int(numer)
            numer = (numer - 1)
            if numer < 0:
                numer = 0
            else:
                await ctx.send ('You lost a point')

            numer = str(numer)

            with open('sps.json', 'r') as f:
                    sps = json.load(f)
            sps[str(person)] = numer

            with open ('sps.json', 'w') as f:
                    json.dump(sps, f, indent=4)
            
            playstate = 'ef'

        except:
            with open('sps.json', 'r') as f:
                    sps = json.load(f)
                    
            sps[str(person)] = "0"
            with open ('sps.json', 'w') as f:
                json.dump(sps, f, indent=4)
            playstate = 'ef'


@client.command()
async def points(ctx):
    person = ctx.author.id

    try:
        with open('sps.json', 'r') as f:
                sps = json.load(f)
        numer = sps[str(person)]
        await ctx.send(f'You have {numer} points!!!')

    except:
        await ctx.send('You have 0 points')
    
    
    
        

@client.command()
async def leaderboard(ctx, *, para):
    if para == "sps":
        with open('sps.json', 'r') as f:
            sps = json.load(f)

        sps_list = sorted(sps.items(), key=lambda x: x[1], reverse=True)

        await ctx.send("Leaderboard:")
        
        for i in sps_list:
            await ctx.send(f'<@{i[0]}> : {i[1]}')
            
    elif para == "coins":
        with open('bal.json', 'r') as f:
            file = json.load(f)
        embed = discord.Embed(color = ctx.author.color, timestamp = ctx.message.created_at)

        embed.set_author(name="Coins Leaderboard")

        point_list = sorted(file.items(), key=lambda x: x[1], reverse=True)
        num = 1
    
        for i in point_list:
        #await ctx.send (f'{i[0]} : {i[1]}')
        
            embed.add_field(name=(f'#{num}'), value=(f'{i[0]} : {i[1]}'), inline=False)
            num += 1
            
        await ctx.send(embed=embed)
        





        """
        with open('bal.json', 'r') as f:
            balance = json.load(f)

        bal_list = sorted(balance.items(), key=lambda x: x[1], reverse=True)

        await ctx.send("Coin Leaderboard :moneybag::")
        
        for i in bal_list:
            await ctx.send(f'{i[0]} : {i[1]}')"""

    elif para == "pokemon":
        with open('test.json', 'r') as f:
            test = json.load(f)

        sps_list = sorted(test.items(), key=lambda x: x[1], reverse=True)

        await ctx.send("Pokemon Leaderboard:")
        
        for i in sps_list:
            await ctx.send(f'<@{i[0]}> : {i[1]}')
        


@client.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def beg(ctx):
    person = ctx.author.id
    person = (f'<@!{person}>')
    
    

    chanceList = ['1', '1', '1', '2']

    chance  = random.choice(chanceList)
    if chance == "2":
        await ctx.send("Bruh stop begging and do something with your life")

    else:
        with open('bal.json', 'r') as f:
            balance = json.load(f)
        try:
            cash = balance[str(person)]
            cash = int(cash)

        except:
            balance[str(person)] = "0"
            with open ('bal.json', 'w') as f:
                json.dump(balance, f, indent=4)
            cash = 0
            
        money = random.randint(1,100)
        cash += money

        balance[str(person)] = cash
        with open ('bal.json', 'w') as f:
            json.dump(balance, f, indent=4)

        
        donaterList = ['Elon Musk', 'Barack Obama', 'Donald Trump', 'Pewdiepie', 'KSI', 'Billy Eilash', 'Jeff Bezos', 'Tanish', 'I', 'A random stranger', 'Ur mom', 'Ronald McDonald', 'God']
        donation = ['felt nice', 'felt generous', 'felt charitable', 'was having a good day', 'felt sorry for you', 'wanted to be called a charitable person']
        donater = random.choice(donaterList)
        donostat = random.choice(donation)
        
        await ctx.send(f'{donater} {donostat} and gave you {money} coins!')
        

        
        
        

    

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    msg = 'Still on cooldown, please try again in {:.2f}s'.format(error.retry_after)
    await ctx.send(msg)
    
        
    
    


@client.command()
async def gamble(ctx, money):
    chance_list = ['1', '1', '2' '2', '3', '3', '1', '2']
    multi_list = ['2', '2', '2', '4']
    
    chance = int(random.choice(chance_list))
    multi = int(random.choice(multi_list))
    person = ctx.author.id
    person = (f'<@!{person}>')
    money = int(money)
    with open('bal.json', 'r') as f:
        balance = json.load(f)

    try:
        cash = balance[str(person)]
        cash = int(cash)
        if cash == 0 or cash < 0:
            await ctx.send('You have no coins to gamble')
        elif money > cash:
            await ctx.send ('You dont have that much to gamble')
        else:
            if chance == 1:
                await ctx.send ('Ouch, you just lost your coins')
                cash = (cash - money)
                if cash < 0:
                    cash = 0
                balance[str(person)] = cash
                with open ('bal.json', 'w') as f:
                    json.dump(balance, f, indent=4)
                

            elif chance == 2:
                await ctx.send('Yay, you earned back the coins you gambled :moneybag:')
                

            elif chance == 3:
                money = (multi * money)
                cash = (cash + money)
                balance[str(person)] = cash
                with open ('bal.json', 'w') as f:
                    json.dump(balance, f, indent=4)
                
                await ctx.send(f'Amazing you just got {money} coins :moneybag:')
                
                
    except:
        await ctx.send('You have no coins to gamble')


@client.command()
async def bal(ctx):
    person = ctx.author.id
    person = (f'<@!{person}>')
    with open('bal.json', 'r') as f:
        balance = json.load(f)

    try:
        cash = balance[str(person)]
        await ctx.send (f'You have {cash} coins :moneybag:')

    except:
        await ctx.send ('You have 0 coins')
        

@client.command()
async def quest(ctx):
    chancelist = ['1', '1', '1', '1', '1', '2', '2', '2', '2', '2', '2', '1', '1'] 
    person = ctx.author.id
    person = (f'<@!{person}>')
    dislist = ['fat', 'slow', 'sloppy', 'dumb']
    dis = random.choice(dislist)
    monsterlist = ['dragon', 'troll', 'goblin', 'witch', 'beast']
    monster = random.choice(monsterlist)
    advlist = ['strong', 'agile', 'powerful', 'quick', 'invincible']
    adv = random.choice(advlist)

    
    with open('bal.json', 'r') as f:
        balance = json.load(f)

    try:
        cash = balance[str(person)]
        cash = int(cash)
    except:
        balance[str(person)] = "0"
        with open ('bal.json', 'w') as f:
            json.dump(balance, f, indent=4)
        cash = 0

    chance = random.choice(chancelist)

    if chance == '1':
        await ctx.send('You went on a dangerous quest...')
        await ctx.send(f'A {monster} attacked you..')
        await ctx.send(f'You were to {dis} and the {monster} killed you, you lost a lot of coins')

        if cash < 0:
            cash = 0
            
        elif cash > 0 and cash < 100:
            cash -= 20

        elif cash > 100 and cash < 500:
            cash -= 50

        elif cash > 500 and cash < 1000:
            cash -= 200

        elif cash > 1000 and cash < 2000:
            cash -= 400

        elif cash > 2000 and cash < 5000:
            cash -= 700

        elif cash > 5000 and cash < 10000:
            cash -= 1000

        else:
            cash -= 5000

        if cash < 0:
            cash = 0


        balance[str(person)] = cash
        with open ('bal.json', 'w') as f:
            json.dump(balance, f, indent=4)

    else:
        win = random.randint(1,300)
        cash = win + cash
        await ctx.send('You went on a dangerous quest...')
        await ctx.send(f'A {monster} attacked you..')
        await ctx.send(f'You were to {adv} and you killed the {monster}, winning {win} coins :moneybag:')

        balance[str(person)] = cash
        with open ('bal.json', 'w') as f:
            json.dump(balance, f, indent=4)
        

@client.command()
async def shop(ctx):
    embed = discord.Embed(color = ctx.author.color, timestamp = ctx.message.created_at)

    embed.set_author(name="Shop")
              
    embed.add_field(name="Commands", value="Do .buy and the name of the item u wanna buy", inline=False)
    embed.add_field(name="Pets", value=" :dog: Puppy : 10,000 coins \n:sheep: Water Sheep : 20,000 coins\n :snake: Python : 50,000 coins\n :dragon: Dragon : 100,000 coins ", inline=False)
    embed.add_field(name="Weapons", value=":knife: Knife \n :dagger: Dagger\n :axe: Axe\n :crossed_swords: Sword\n :chains: Chainsaw\n", inline=False)
    embed.add_field(name="Tools", value=":pick: Pickaxe : 500 coins \n :hammer: Hammer\n :wrench: Wrench\n <:fishrod:774263070335827981> Fishing Rod : 300 coins", inline=False)

        
    await ctx.send(embed=embed)

            
            
            
@client.command()
async def rob(ctx, *, tag):
    weaponlist = ['sword', 'dagger', 'knife', 'chainsaw', 'hammer']
    weapon = random.choice(weaponlist)
    person = ctx.author.id
    person = (f'<@!{person}>')
    with open('bal.json', 'r') as f:
        balance = json.load(f)
    
    try:
        urcash = balance[str(person)]
        urcash = int(urcash)
        if urcash < 200:
            await ctx.send('You need atleast 200 coins to try to rob someone')

        else:
            try:
                theircash = balance[str(tag)]
                #print (thiercash)
                theircash = int(theircash)
                if theircash < 200:
                    await ctx.send('The person you tagged doesnt have enough money to steal from')
                else:
                    chance = random.randint(1,2)
                    if chance == 1:
                        theircash += 200
                        balance[str(tag)] = theircash
                        with open ('bal.json', 'w') as f:
                            json.dump(balance, f, indent=4)
                        urcash -= 200
                        balance[str(person)] = urcash
                        with open ('bal.json', 'w') as f:
                            json.dump(balance, f, indent=4)
                            
                        await ctx.send(f'You sneaked into {tag}\'s house at midnight..')
                        await ctx.send(f'But to you surprise they were there waiting for with a {weapon}')
                        await ctx.send(f'You got killed and lost your 200 coins')
                        

                    else:
                        won = random.randint(1,300)
                        theircash -= won
                        balance[str(tag)] = theircash
                        with open ('bal.json', 'w') as f:
                            json.dump(balance, f, indent=4)
                        won = random.randint(1,300)
                        urcash += won
                        balance[str(person)] = urcash
                        with open ('bal.json', 'w') as f:
                            json.dump(balance, f, indent=4)
                        await ctx.send(f'You sneaked into {tag}\'s house at midnight....')
                        await ctx.send(f'You were like sneaky like a shadow')
                        await ctx.send(f'Noice, you got away with {won} coins')
                    
                    

            except:
                await ctx.send("Either you didn't tag a real person or they dont have enough coins to steal from")
            
    except:
        await ctx.send('You dont have any money to rob someone, maybe go on a quest?')
        balance[str(person)] = 0
        with open ('bal.json', 'w') as f:
            json.dump(balance, f, indent=4)
        
        

def ted(dude):
    time.sleep(20)
    with open('time.json', 'r') as f:
        tim = json.load(f)
        
    tim[str(dude)] = "no"
    with open ('time.json', 'w') as f:
        json.dump(tim, f, indent=4)
    
    
    
@client.command()
async def work(ctx):
    person = ctx.author.id
    person = (f'<@!{person}>')
    with open('time.json', 'r') as f:
        tim = json.load(f)
    
    try:
        stat = tim[str(person)]
        
    except:
        tim[str(person)] = "yes"
        with open ('time.json', 'w') as f:
            json.dump(tim, f, indent=4)
        stat = "yes"

    if stat == "yes":
        await ctx.send('you started working')
        tim[str(person)] = "no"
        with open ('time.json', 'w') as f:
            json.dump(tim, f, indent=4)
            
        t = threading.Thread( tim, (person) )
        t.start
        
        
    else:
        await ctx.send('You cant work yet')
    

@client.command()
async def amongus(ctx):
    person = ctx.author.id
    person = (f'<@!{person}>')

    with open('among.json', 'r') as f:
        among = json.load(f)

        
    chance_list = ('imposter', 'crewmate')
    chance = random.choice(chance_list)
    if chance == 'crewmate':
        await ctx.send('Noice your a crewmate :mag:\nWhere would you like to go?')
        
    else:
        await ctx.send('Congrats your the imposter!! :knife:\nWhere would you like to go?')

    among[str(person)] = chance
    with open ('among.json', 'w') as f:
        json.dump(among, f, indent=4)

        
@client.command()
async def go(ctx, *, place):
    person = ctx.author.id
    person = (f'<@!{person}>')

    with open('among.json', 'r') as f:
        among = json.load(f)

    try:
        stat = among[str(person)]

        if stat == "imposter" or stat == "crewmate":
            
            

            if place == "electrical":
                await ctx.send('You went to electrical')

            elif place == "weapons":
                await ctx.send('You went to weapons')

            else:
                await ctx.send("Thats not a valid place to go")

                
            if stat == 'crewmate':
                await ctx.send('What would you like to do: task/leave')
                
            elif stat == 'imposter':
                await ctx.send('What would you like to do: fake/kill/leave')

        else:
            await ctx.send('You need to start a among us game first')
                    
        

    except:
        await ctx.send('You need to start a among us game first')

@client.command()
async def task(ctx):
    person = ctx.author.id
    person = (f'<@!{person}>')

    with open('among.json', 'r') as f:
        among = json.load(f)

    try:
        stat = among[str(person)]
        if stat == "crewmate":
            chance = ('1', '2')
            chance = random.choice(chance)

            if chance == '1':
                await ctx.send('You completed your task and won the game!')
            else:
                await ctx.send('You started doing your task....But an imposter enetered the room and killed you :knife:!! You lost :(')

            among[str(person)] = 'iug'
            with open ('among.json', 'w') as f:
                json.dump(among, f, indent=4)            
                
            

        elif stat == "imposter":
            await ctx.send('You can\'t do a task your an imposter... but you could fake them')

        else:
            await ctx.send('You need to start a among us game first')
    except:
        await ctx.send('You need to start a among us game first')


@client.command()
async def buy(ctx, *, item):
    person = ctx.author.id
    person = (f'<@!{person}>')

    with open('bal.json', 'r') as f:
        balance = json.load(f)

    try:
        cash = balance[str(person)]
        cash = int(cash)

        try:
            with open('shop.json', 'r') as f:
                shop = json.load(f)

            shop_list = shop[str(person)]

        except:
            shop[str(person)] = []
            with open ('shop.json', 'w') as f:
                json.dump(shop, f, indent=4)
            shop_list = shop[str(person)]

        if item == "pickaxe" or item == "Pickaxe":
            if 'Pickaxe' in shop_list:
                await ctx.send('You already have this item')

            elif cash < 500:
                await ctx.send('You don\'t have enough money :moneybag:')

            else:
                await ctx.send('You bought a Pickaxe! :pick:')

                cash -= 500
                balance[str(person)] = cash
                with open ('bal.json', 'w') as f:
                    json.dump(balance, f, indent=4)

                shop_list.append('Pickaxe')
                shop[str(person)] = shop_list
                with open ('shop.json', 'w') as f:
                    json.dump(shop, f, indent=4)


        if item in ['fish', 'fishingrod', 'fishrod', 'fishing rod', 'rod']:
            


            if 'Fishing Rod' in shop_list:
                await ctx.send('You already have this item')

            elif cash < 300:
                await ctx.send('You don\'t have enough money :moneybag:')

            else:
                await ctx.send('You bought a Fishing Rod! <:fishrod:774263070335827981>')

                cash -= 300
                balance[str(person)] = cash
                with open ('bal.json', 'w') as f:
                    json.dump(balance, f, indent=4)

                shop_list.append('Fishing Rod')
                shop[str(person)] = shop_list
                with open ('shop.json', 'w') as f:
                    json.dump(shop, f, indent=4)
                
                      

    except:
        await ctx.send("You dont have enough money to buy anything :moneybag:")

@client.command(aliases=['inv'])
async def inventory(ctx):
    person = ctx.author.id
    person = (f'<@!{person}>')

    try:
        with open('shop.json', 'r') as f:
            shop = json.load(f)

        shop_list = shop[str(person)]

        await ctx.send(f'INVENTORY:\n{shop_list}')

    except:
        await ctx.send('You have nothing in your inventory')

    
@client.command()
async def test(ctx, para):
    await ctx.send('Halo')

@test.error
async def test_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('YASSSSIT WORKED')
            
    
@client.command()
async def fish(ctx):
    person = ctx.author.id
    person = (f'<@!{person}>')

    try:
        with open('shop.json', 'r') as f:
            shop = json.load(f)

        shop_list = shop[str(person)]

        if "Fishing Rod" in shop_list:

            chances = ['1', '2']
            chance = random.choice(chances)
            if chance == '1':
                await ctx.send("You just caught a fish :tropical_fish:")

            else:
                await ctx.send("Ha you got nothing suckit")
        else:
            await ctx.send('You don\'t have a fishing rod :( \n Buy one with "buy fishing rod" <:fishrod:774263070335827981> ')

            
    except:
        await ctx.send('You don\'t have a fishing rod :( \n Buy one with "buy fishing rod" <:fishrod:774263070335827981> ')

    
        
    
""" 
@client.command()
async def test(ctx, *, thing):
""" 
    
    #await ctx.send('<:fishrod:773556128918798397>')
    #await ctx.author.send('helllooooooooo')
    
    



client.run('NzQwMjIzNTU1MDM1MjAxNTY3.Xyl46A.5VxAFGMym7cEpgwLiojPqE-4nfM')


charizardimage = 'https://cdn.bulbagarden.net/upload/thumb/7/7e/006Charizard.png/1200px-006Charizard.png'

"""

with open('sps.json', 'r') as f:
        sps = json.load(f)
        points = sps[str(key)]
        await ctx.send(f'<@{key}> : {points}')
    for key in sps:
        points = sps[str(key)]
        await ctx.send(f'<@{key}> : {points}')
        

    for key in sps:
        points = sps[str(key)]
        #points = int(points)
        sps_list.append(points)

    sps_list.sort(reverse=True)
            
    for key in sps_list:
        name = sps[str(key)]
        await ctx.send(f'<@{name}> : {key}')

        
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
"""
