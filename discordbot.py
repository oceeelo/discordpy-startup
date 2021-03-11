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


@bot.command()
async def オグリキャップ(ctx):
    await ctx.send('https://kamigame.jp/umamusume/page/109898038796877831.html')
    
@bot.command()
async def にゃーん(ctx):
    await ctx.send('にゃーーーん')

# 発言時に実行されるイベントハンドラを定義
@client.event
async def on_message(message):
    if message.content == '/cleanup':
        if message.author.guild_permissions.administrator:
            await message.channel.purge()
            await message.channel.send('塵一つ残らないね！')
        else:
            await message.channel.send('何様のつもり？')


bot.run(token)
