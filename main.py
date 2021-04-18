import discord
from replit import db
from Profile import UserProfile


client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!commands'):
        await message.channel.send('Check your direct messages!')
        await message.author.send('```Welcome to Hydration Bot!\n\nHere are the following commands:\n\n\t!hydration\t-\tThis command gets you initalize hydration bot for use. (for first time users only)\n\n\t!brand\t-\tThis command provides the user with information about water brands they wish to know more about.```')

    if message.content.startswith('!hydration'):
        userProfile = UserProfile(0,0,0)
        await message.author.send('What is your weight(lbs) [NUMBERS ONLY]?')

        def check(m):
            return m.content.isnumeric()

        msg1 = await client.wait_for('message',check=check)
        userProfile.setWeight(msg1.content)
        print(msg1.content)
            
        await message.author.send('How many minutes do you exercise a day [NUMBERS ONLY]?')
        msg2 = await client.wait_for('message',check=check)
        userProfile.setActivityTime(msg2.content)
        print(msg2.content)
        userProfile.setUser(msg1.id)
        print(userProfile.getUser())
        data2send = (userProfile.getWeight(), userProfile.getActivityTime())
        db[userProfile.getUser()] = data2send
        await message.author.send(userProfile.getStats())
        
    if message.content.startswith('!brand'):
        def checkString(m):
            return m.content.lower()
        await message.author.send('```Please type a brand: ```')
        await message.author.send('```Here are the following selection(s):\ndasani\npoland spring\nsmartwater\nfiji\nessentia\nvoss\ncore\ndeer park\nMORE WILL BE ADDED SOON! ```')
        brand = await client.wait_for('message',check=checkString)
        if brand.content.lower() == 'dasani':
            await message.author.send('The pH level of Dasani is 5.6.')
        if brand.content.lower() == 'poland spring':
            await message.author.send('The pH level of Poland Spring is 7.2.')
        if brand.content.lower() == 'smartwater':
            await message.author.send('The pH level of Smartwater is 7.0.')
        if brand.content.lower() == 'fiji':
            await message.author.send('The pH level of Fiji Water is 7.7.')
        if brand.content.lower() == 'essentia':
            await message.author.send('The pH level of Essentia Water is 9.5.')
        if brand.content.lower() == 'voss':
          await message.author.send('The pH level of Voss Water is 7.3.')
        if brand.content.lower() == 'core':
            await message.author.send('The pH level of Core Water is 7.4.')
        if brand.content.lower() == 'deer park':
            await message.author.send('The pH level of Deer Park Water is 7.5.')



    
client.run('ODMzMTgzMzE2MTE4NjAxNzY4.YHuobg.akQTJU4719JPmP6S7JCXah24gGQ')