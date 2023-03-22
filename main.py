import discord
import os
from discord.ext import commands
intents=discord.Intents.all()
bot = commands.Bot(command_prefix='prefix', intents=intents) # add a prefix here.

@bot.command()
async def addrole(ctx, hexcode, *rolename):
    color = int(hexcode, 16)
    rolename = ' '.join(rolename)
    role = await ctx.guild.create_role(name=rolename, colour=discord.Colour(color))
    await role.edit(position=0)  # Here you can change the position the role is created in, 0 is the lowest.
    await ctx.author.add_roles(role)
    await ctx.send(f'Created role "{rolename}" with color #{hexcode} and assigned to {ctx.author}')

bot.run(os.environ['TOKEN'])
    
    
