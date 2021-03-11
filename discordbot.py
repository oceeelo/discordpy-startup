from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)





@client.event
async def on_message(message):

if message.author.bot:
return

if message.content == 'にゃーん':
await message.channel.send(にゃーーーん')


if message.content == 'しおみ':
filepath = '/discordpy-startup/shiomi/しおみ.png'
await client.send_file(message.channel,filepath)




bot.run(token)
