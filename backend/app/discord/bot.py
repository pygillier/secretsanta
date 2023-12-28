import asyncio
import discord
from discord.ext import commands
from .. import settings

# Discord bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=settings.prefix, intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} running with FastAPI")


@bot.command(name="subscribe", description="Subscribe to Secret Santa")
async def subscribe(ctx: commands.Context):
    await ctx.send(f"Got subscription request from {ctx.author.display_name} (ID: {ctx.author.id})")


@bot.command(name="unsubscribe", description="Unsubscribe from Secret Santa")
async def unsubscribe(ctx: commands.Context):
    await ctx.send(f"Got subscription request from {ctx.author.display_name} (ID: {ctx.author.id})")


@bot.command(name="sent", description="Indicates you've send your gift")
async def notify_sent(ctx: commands.Context):
    await ctx.send(f"Hello {ctx.author.mention}, your gift is marked as sent! You giftee has been notified over discord")


@bot.command(name="received", description="Indicated you've received your gift")
async def notify_received(ctx: commands.Context):
    await ctx.send(f"Hello {ctx.author.mention}, your gifter has been notified you received his/her gift.")


async def run_bot():
    try:
        await bot.start(token=settings.discord_token)
    except KeyboardInterrupt:
        await bot.close()

asyncio.create_task(run_bot())
