#Returns array of message history for the channel where a message was sent
async def download_history(message, history_length):
    a = 0
    history = []
    async for message in message.channel.history():
        if a  < history_length + 1:
            if a != 0:
                history.append(message.content.replace('\n', ' '))
                history.append(message.author.name)
            a += 1
    return history

#Parses the array of message history into an AI readable langchain part
async def parse_history(history, bot_name):
    parsed_history = ""
    for a in reversed(range(0, len(history))):
        if a%2 == 0:
            if history[a + 1] == bot_name:
                parsed_history += f'\n{bot_name}: {history[a]}'
            else:
                parsed_history += f'\n{history[a + 1]}: {history[a]}'
    return parsed_history[1:]

async def add_message(parsed_history, message, bot_name):
    each_line_list = parsed_history.split('\n')
    each_line_list.pop(0)
    if message.author == bot_name:
        each_line_list.append(f'{bot_name}: {message.content}')
    else:
        each_line_list.append(f'{str(message.author)}: {message.content}')
    new_parsed_history = ''
    for a in each_line_list:
        new_parsed_history = new_parsed_history + a + '\n'
    return new_parsed_history[:-1]

async def add_message_bot(parsed_history, message, bot_name):
    each_line_list = parsed_history.split('\n')
    each_line_list.pop(0)
    each_line_list.append(f'{bot_name}: {message}')
    new_parsed_history = ''
    for a in each_line_list:
        new_parsed_history = new_parsed_history + a + '\n'
    return new_parsed_history[:-1]

async def clear_history(history_dictionary, interaction, history_length, bot_name):
    erased_history = ''
    try:
        each_line_list = history_dictionary[interaction.channel.id].split('\n')
        for a in each_line_list:
            erased_history += ' \n'
        return erased_history[:-1]
    except:
        each_line_list = str(await parse_history(await download_history(interaction, history_length), bot_name)).split('\n')
        for a in each_line_list:
            erased_history += ' \n'
        return erased_history[:-1]
    