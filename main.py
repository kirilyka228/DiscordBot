import asyncio
from asyncio import TimeoutError
from prisma import Prisma
import json
import discord
from discord.ext import commands
from discord import utils
from asyncio import sleep
from discord.ui import Button,View
import settings

intents = discord.Intents.all()
intents = discord.Intents.default()
intents.members = True
PREFIX = '!'
client = commands.Bot(command_prefix= PREFIX, intents = discord.Intents.all())
prisma = Prisma()

#ewfewfwe
@client.event
async def on_ready():
    print('Я тут!!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='за чатом🔍'))


# @client.command(aliases=["Телеграмм"])
# async def tg(ctx, message ):
#     await ctx.message.delete()
#     def check(m):
#         return m.author.id == ctx.author.id
#     await ctx.send('Напиши в чат!(@твой_тг)')
#
#     try:
#         await client.wait_for("message", check = check, timeout=5)
#     except TimeoutError:
#         return await ctx.send('Время вышло.')
#     if message.startswith("@"):
#         await ctx.send(f'Ваш логин: {message}')
#     else:
#         pass

@client.command()
async def tg(ctx, arg):
    channel = client.get_channel(1036691862603432107)
    author = ctx.message.author
    if arg[3] == '@':
        await ctx.send(f'{author.mention},твой телеграмм записан!'+ arg)
    else:
        await ctx.send('Ты неверно ввел свой логин,смотри структуру🔝',delete_after = 6.0)

    await ctx.message.delete()





# @client.command()
# async def TG(ctx):
#     await ctx.message.delete()
#     channel = client.get_channel(1029818322201620510)
#     embed = discord.Embed(title='Напишите свой ТГ в чат',description='@ваш_тг', color = ctx.author.color)
#     embed.set_thumbnail(url = 'https://emoji.discadia.com/emojis/9fa603df-4864-439b-b78d-544c7f78cdca.gif')
#     mojj = await channel.send(embed=embed)


# @client.event
# async def on_message(message):
#     if '@' in message.content.lower():
#         await message.channel.send('Отлично')
#         await prisma.connect()
#         user = await prisma.test.update(
#             where = {'ID_DC': str(member.id)},
#             data={'tg_channel': 'Строка с аккаунтом введенная пользователем'},
#         )
#         await prisma.disconnect()


@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 1036266024636514314:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        # Python, Swift (Чайка), C++, Dart ( Дротик), JS, Ruby, C#, Java
        if payload.emoji.name == 'python':
            role = discord.utils.get(guild.roles, name='Python')
        elif payload.emoji.name == 'swift22':
            role = discord.utils.get(guild.roles, name='Swift')
        elif payload.emoji.name == 'cplus':
            role = discord.utils.get(guild.roles, name='C++')
        elif payload.emoji.name == 'dart98':
            role = discord.utils.get(guild.roles, name='Dart')
        elif payload.emoji.name == 'js37':
            role = discord.utils.get(guild.roles, name='JS')
        elif payload.emoji.name == 'ruby22':
            role = discord.utils.get(guild.roles, name='Ruby')
        elif payload.emoji.name == 'sharp33':
            role = discord.utils.get(guild.roles, name='C#')
        elif payload.emoji.name == 'javaS':
            role = discord.utils.get(guild.roles, name='Java')
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)
        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)

                await prisma.connect()
                print(type(role.name))
                result = await prisma.test.find_first(
                    where = {
                        'Name' : member.name
                    }
                )
                if result:
                    user = await prisma.test.update(
                        where={
                            'Name': member.name
                        },
                        data = {
                            'user_role': {
                                'push' : [str(role.name)]
                            }
                        }
                    )
                else:
                    user = await prisma.test.create(
                        data = {
                            'Name': member.name,
                            'ID_DC': str(member.id),
                            'user_role': [str(role.name)]
                        },
                    )
                await prisma.disconnect()
                print('done')
            else:
                print('Member is not found.')
        else:
            print('Role not found')

@client.event
async def on_raw_reaction_remove(payload):
        message_id = payload.message_id
        if message_id == 1036266024636514314:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

            # Python, Swift (Чайка), C++, Dart ( Дротик), JS, Ruby, C#, Java
            if payload.emoji.name == 'python':
                role = discord.utils.get(guild.roles, name='Python')
            elif payload.emoji.name == 'swift22':
                role = discord.utils.get(guild.roles, name='Swift')
            elif payload.emoji.name == 'cplus':
                role = discord.utils.get(guild.roles, name='C++')
            elif payload.emoji.name == 'dart98':
                role = discord.utils.get(guild.roles, name='Dart')
            elif payload.emoji.name == 'js37':
                role = discord.utils.get(guild.roles, name='JS')
            elif payload.emoji.name == 'ruby22':
                role = discord.utils.get(guild.roles, name='Ruby')
            elif payload.emoji.name == 'sharp33':
                role = discord.utils.get(guild.roles, name='C#')
            elif payload.emoji.name == 'javaS':
                role = discord.utils.get(guild.roles, name='Java')
            else:
                role = discord.utils.get(guild.roles, name = payload.emoji.name)
            if role is not None:
                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)

                    await prisma.connect()
                    result = await prisma.test.find_first(
                        where={
                            'Name': member.name
                        }
                    )
                    if not result:
                       print('такого нет')
                    else:
                        print(type(role))
                        print(result.user_role)
                        array = result.user_role
                        updt_array = list(filter(lambda x:x != role.name, array))
                        print(updt_array)
                        user = await prisma.test.update(
                            where={
                                'Name': member.name
                            },
                            data = {
                                'user_role':{
                                    'set' : updt_array
                                }
                            }
                        )
                    print('done')
                    await prisma.disconnect()
                else:
                    print('Member is not found.')
            else:
                print('Role not found')

@client.command()
async def role(ctx):
    await ctx.message.delete()
    channel = client.get_channel(1029818322201620510)
    embed = discord.Embed(title='Choose your role in life!',description='1.<:python:1030814666995277846>   Python,'
                                                                        '\n2.<:swift22:1035107575601045535>  Swift,'
                                                                        '\n3.<:cplus:1035107603367333928>  C++,'
                                                                        '\n4.<:dart98:1035107655867437066>  Dart,'
                                                                        '\n5.<:js37:1035107672820826162>  JS,'
                                                                        '\n6.<:ruby22:1035107719952224266>  Ruby,'
                                                                        '\n7.<:sharp33:1035107795952996352>  C#,'
                                                                        '\n8.<:javaS:1030815263458857001>  Java', color = ctx.author.color)
    embed.set_thumbnail(url = 'https://emoji.discadia.com/emojis/77fbde32-ecb2-4d1f-881b-b126047f93b7.gif')
    mojj = await channel.send(embed=embed)

@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def clear(ctx,amount = 100):
    await ctx.message.delete()
    await ctx.channel.purge(limit = amount)

@client.event
async def on_member_join(member):
    channel = client.get_channel(1031559545018908702)
    role = discord.utils.get(member.guild.roles, id = 1031559990235906058)
    await  member.add_roles(role)
    await channel.send(embed = discord.Embed(description = f'🏃🏿💨💨Теперь и``{member.name}``вместе с нами!',color = 0x0000FF ))

@client.command()
async def number_role(ctx):
    await ctx.message.delete()
    #roleID = 1031559990235906058
    role = utils.get(ctx.guild.roles,name = 'Gay' )
    print(f'Список пользователей для роли "{role.name}"\n')
    number = 0
    for member in role.members:
        number += 1
        print(
            f'№: {number}\nName: {member.name}\nID: {member.id}\nDiscriminator: {member.discriminator}\nStatus: {member.status}\n')

@client.command()
async def skill(ctx):
    await ctx.message.delete()
    channel = client.get_channel(1029818322201620510)
    embed = discord.Embed(title='Choose your skill level!',description='1.<:success:1036662551964029019>   Junior'
                                                                        '\n2.<:memesstar:1036663057700638771>  Middle'
                                                                        '\n3.<:old95:1036663278304239647>  Senior', color = ctx.author.color)
    embed.set_thumbnail(url = 'https://emoji.discadia.com/emojis/77fbde32-ecb2-4d1f-881b-b126047f93b7.gif')
    mojj = await channel.send(embed=embed)

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 1036666325730345010:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        if payload.emoji.name == 'success':
            role = discord.utils.get(guild.roles, name='Junior')
        elif payload.emoji.name == 'memesstar':
            role = discord.utils.get(guild.roles, name='Middle')
        elif payload.emoji.name == 'old95':
            role = discord.utils.get(guild.roles, name='Senior')
        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                print('done')
            else:
                print('Member is not found.')
        else:
            print('Role not found')

@client.event
async def on_raw_reaction_remove(payload):
        message_id = payload.message_id
        if message_id == 1036666325730345010:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

            if payload.emoji.name == 'success':
                role = discord.utils.get(guild.roles, name='Junior')
            elif payload.emoji.name == 'memesstar':
                role = discord.utils.get(guild.roles, name='Middle')
            elif payload.emoji.name == 'old95':
                role = discord.utils.get(guild.roles, name='Senior')
            else:
                role = discord.utils.get(guild.roles, name = payload.emoji.name)
            if role is not None:
                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
                    print('done')
                else:
                    print('Member is not found.')
            else:
                print('Role not found')


client.run(settings.token_bot)




# @client.command()
# async def list(ctx):
#     await ctx.message.delete()
#     embed = discord.Embed(title = 'Список', color = ctx.author.color)
#     # emb.set_author(name = client.user.name, icon_url = client.user.avatar.url)
#     # emb.set_footer(text = author.name, icon_url = author.avatar.url)
#     adminID = 1029816335322062891
#     admin = utils.get(ctx.guild.roles, id = adminID)
#     embed.add_field(name="Администраторы", value=[2], inline=True)
#     for member in role.members:
#       embed.add_field(value=f'{member.mention}')
#     moderID = 1029816505052954784
#     moder = utils.get(ctx.guild.roles, id = moderID)
#     embed.add_field(name="Модераторы",value=[1], inline=True)
#     for member in role.members:
#       embed.add_field(value=f'{member.mention}')
#     admrID = 1029816546710802442
#     admr = utils.get(ctx.guild.roles, id=admrID)
#     embed.add_field(name="Администраторы", value=[0], inline=True)
#     for member in role.members:
#         embed.add_field(value=f'{member.mention}')
#         await ctx.send( embed = embed )