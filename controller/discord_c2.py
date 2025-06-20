import discord as dc
import asyncio as asy
import os

tkns = os.getenv("1tkn", "2tkn")
channelid = 123xd456xd789

p = print

int = dc.Intents.default()
int.messages = True
int.message_content = True

bot = dc.Client(intents=intents)

@bot.event
async def on_ready():
    p(f"[+] Discord bot online as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.id != channelid:
        return

    content = message.content.lower()

    if content == "!ping":
        await message.channel.send("Pong!")
    
    elif content == "!bots":
        await message.channel.send("🤖 [Mock] 2 bots online: #001 (Win10), #002 (Win11)")

    elif content.startswith("!cmd "):
        command = content[5:]
        await message.channel.send(f"💻 Executing command: `{command}`\n[Mock] Result: OK")

    elif content == "!screenshot":
        await message.channel.send("[Mock] Screenshot saved and sent.")

    else:
        await message.channel.send("❓ Unknown command. Try `!ping`, `!bots`, `!cmd <command>`, `!screenshot`.")

if __name__ == "__main__":
    bot.run(tkns)
