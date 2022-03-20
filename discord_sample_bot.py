import discord
import random

TOKEN = 'OTA4MDcwMTQ5NjIwMzY3Mzkx.YYwYOg.sfH-ZwrJl7J3R6nsPgwR_igc57c'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')
    
    # make sure bot does not respond to its own messages (infinite loop)
    if message.author == client.user:
        return

    if message.channel.name == 'csp-bot-channel': # only respond in this authorized channel
        if user_message.lower() == '+hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == '+bye':
            await message.channel.send(f'See you later {username}!')
            return
        elif user_message.lower() == '+random':
            response = f'This is your random number (up to 100): {random.randrange(100)}'
            await message.channel.send(response)
            return

    if user_message.lower() == '+commands':
        await message.channel.send('I accept the commands: +hello, +bye, and +random as long as I am in my designated channel: csp-bot-channel. I accept +command from any channel.')
        return

client.run(TOKEN)