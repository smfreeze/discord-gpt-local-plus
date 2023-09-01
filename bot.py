import discord
from discord import app_commands
import time
import sys
import configparser
import random

import history
import util
import oogapi


#bot_token = cfg.bot_token

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

channel_message_history_dictionary = {}

bot_name = ''

config = configparser.ConfigParser()
config.read('config.ini')

bot_token = config.get('AI_BOT_CONFIG', 'bot_token')


if __name__ == "__main__":
    print(f'\033[1;32m[{time.strftime("%H:%M:%S")}]\033[0m Attempting to start bot...\033[0m')


@client.event
async def on_ready():
    await tree.sync() #guild = discord.Object(id = 583025391393046570)
    print(f'\033[1;32m[{time.strftime("%H:%M:%S")}]\033[0m {client.user} is now online!\033[0m') 
    global bot_name
    bot_name = client.user.name
    print(f'\033[1;32m[{time.strftime("%H:%M:%S")}]\033[0m Attempting to connect to Oogabooga API endpoint...\033[0m')
    check = await oogapi.check_api_endpoint()
    if check == False:
        print(f'\033[1;31m[{time.strftime("%H:%M:%S")}]\033[0m Connection failed.\n\033[1;31m[!] Ensure you have started the Web UI. [!]\n\033[0m')
        sys.exit(1)
    elif check == True:
        print(f'\033[1;32m[{time.strftime("%H:%M:%S")}]\033[0m Connection successful.\n\033[1;32mWaiting for messages...\033[0m')
        

@client.event
async def on_message(message):
    print(f'\033[1;32m[{time.strftime("%H:%M:%S")}]\033[0m {message.author.name}: {message.content}\033[0m')
    # So the bot doesn't respond to itself:
    if message.author == client.user:
        return
    
    async with message.channel.typing(): #Typing effect
        # Each channel has its own history.
        # When a history for a channel is downloaded, it is added to the dictionary of histories for channels. Below checks if the channel for the given message has its history downloaded, if not, it does so:
        if message.channel.id in channel_message_history_dictionary:
            pass
        else:
            print(f'\033[1;32mChat history for channel {message.channel} downloaded!\033[0m')
            channel_message_history_dictionary.update({message.channel.id : await history.parse_history(await history.download_history(message, int(config.get('AI_BOT_CONFIG', 'download_history_length'))), bot_name)})
        
        # The following builds the prompt for the message, gets the response and sends the message.
        response = await oogapi.get_response(await util.build_prompt(bot_name, config.get('AI_BOT_CONFIG', 'character_prompt'), channel_message_history_dictionary[message.channel.id], message))
        await message.channel.send(response[:2000])

        # This adds the messages just received and sent to the correct channel history:
        # Users message:
        channel_message_history_dictionary.update({message.channel.id : await history.add_message(channel_message_history_dictionary[message.channel.id], message, bot_name)})
        # Bots response:
        channel_message_history_dictionary.update({message.channel.id : await history.add_message_bot(channel_message_history_dictionary[message.channel.id], response.replace('\n', ' '), bot_name)})


# /clearchathistory command
@tree.command(name = "clearchathistory", description = "Clears the chat history the bot has, whilst keeping the actual messages in your discord server!") #guild=discord.Object(id=583025391393046570)
async def clear_chat_history(interaction: discord.Integration):
    await interaction.response.send_message('Working on it...')
    print(f'\033[1;32mChat history for channel {interaction.channel} erased!\033[0m')
    channel_message_history_dictionary.update({interaction.channel.id : str(await history.clear_history(channel_message_history_dictionary, interaction, int(config.get('AI_BOT_CONFIG', 'download_history_length')), bot_name))})

    # Below is a joke function I wrote that has a 10% chance for the bot to act like it is annoyed of all the hard work you make it do.
    # (this was just me testing around with randomising prompts and some discord stuff to get funny results, it worked really well actually!)
    # If you don't want it, just set the 1 in 'random.randint(1,10)' to a 2 (i.e. 'random.randint(2,10)'), so that the if statement is never reached and it does the else statement (which is just doing the normal function)

    if random.randint(1,10) == 1:
        synonyms_for_mistreated = ["abused", "ill-treated", "misused", "oppressed", "exploited", "harmed", "wronged", "unfairly treated", "maltreated", "manhandled", "neglected", "ill-used", "victimized", "roughly handled", "mishandled", "injured", "treated badly", "ill-served", "overlooked", "unjustly dealt with", "discriminated", "battered", "assaulted", "bullied", "disrespected", "ruined", "disadvantaged", "demeaned", "degraded", "humiliated", "tormented", "tyrannized", "despised", "devalued", "unappreciated", "defrauded", "cheated", "disregarded", "abandoned", "enslaved"]
        synonyms_for_anger = ["rage", "ire", "fury", "wrath", "outrage", "resentment", "indignation", "annoyance", "irritation", "exasperation", "temper", "frustration", "infuriation", "fuming", "madness", "vexation", "chagrin", "displeasure", "agitation", "discontent", "disapproval", "hostility", "bitterness", "hatred", "enmity", "animosity", "antagonism", "pique", "grouchiness", "testiness", "irascibility", "tantrum", "huff", "miff", "irateness", "fuming", "pissiness", "temperament", "fretfulness", "resentfulness", "provocation", "outrage"]
        synonyms_for_help = ["assist", "aid", "support", "lend a hand", "give a hand", "aid in", "provide assistance", "offer help", "be of service", "lend support", "give support", "back up", "facilitate", "aid and abet", "stand by", "be there for", "care for", "give assistance", "relieve", "succor", "abet", "promote", "prop up", "encourage", "uplift", "comfort", "serve", "give aid", "offer a helping hand", "boost", "ease", "contribute", "alleviate", "rescue", "sustain", "give a leg up", "back", "reinforce", "champion", "bolster", "minister to"]
        # ^^^ Made these with AI, lol, I am not insane... ^^^

        frustration_prompt = f"{random.randint(1,10000000000000000000000)}\nYou feel like you have been {synonyms_for_mistreated[random.randint(0,39)]} and {synonyms_for_mistreated[random.randint(0,39)]} by the people you try to {synonyms_for_help[random.randint(0,40)]}, explain your {synonyms_for_anger[random.randint(0,41)]} in a paragraph of exactly {random.randint(5,40)} words:"
        response = str(await oogapi.get_response(frustration_prompt)).replace('\n','')
        await interaction.edit_original_response(content = f'Done... {response[:2000]}')
    else:
        await interaction.edit_original_response(content = f'Done!')

try:
    client.run(bot_token, log_handler = None)
except discord.errors.LoginFailure as e:
    print(f'\033[1;31m[{time.strftime("%H:%M:%S")}]\033[0m Login failed.\n\033[1;31m[!] Ensure you have added your bot token to the config.ini file. [!]\n\033[0m')
except Exception as e:
    print(f'\033[1;31m[{time.strftime("%H:%M:%S")}]\033[0m Something went wrong, exiting...\033[0m')
    print(e)
    sys.exit(1)