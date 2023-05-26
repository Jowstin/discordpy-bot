import os       #Using Env Variables
import discord  #Discord API thingy
from discord.ext import commands, tasks
import random   #Random
from datetime import datetime
from pytube import YouTube, Playlist


#INFO HUB

def swirly(placeholder):
    random.shuffle(placeholder)
    return placeholder[0]



# Notifies in terminal when bot online.
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}. In: {message.channel}')
        
        author=message.author
        content=message.content
        channel=message.channel


        discord_message={'Message from {message.author}: {message.content}. In: {message.channel}\n'}
        bamp = 'Massage:',str(content),'from',str(author),'in',str(channel),'at',str(datetime.now())

        file = open('repo.txt','a')
        file.writelines(str(bamp))
        file.writelines('\n')
        file.close()


        if message.content.startswith('+Ihatechildren'):
            await message.channel.send('Me too')

        if message.content.startswith('+feetpic'):
            await message.channel.send('https://www.diabetesaustralia.com.au/wp-content/uploads/feet-web.png')

        if message.content.startswith('+goodbot'):
            await message.channel.send(':D')
        
        if message.content.startswith('+musicreccomend'):
            p = Playlist('https://www.youtube.com/watch?v=HUZnmTa1oM4&list=PLtcyL5PJGFnjZsy20m0xrqphGsHetBoph')

            urls = p.video_urls
            print(urls)
            fabled = random.choice(urls)
            await message.channel.send(fabled)





# I honestly have no idea
intents = discord.Intents.default()
intents.message_content = True

# Runs the Bot
client = MyClient(intents=intents)
client.run(os.environ["DISCORD_TOKEN"])
