#Reverses array's content
async def reverse_array(array):
   return array[::-1]

#Switches each pair, e.g. [1,2,3,4,5,6] becomes [2,1,4,3,6,5]
async def pair_switch_array(array):
    for a in range(0, len(array)):
        if a%2 == 0:
            array[a], array[a + 1] = array[a + 1], array[a]
    return array

async def build_prompt(bot_name, character_prompt, message_history, message):
    return f"REMEMBER THIS: Your name is {bot_name}. {character_prompt}. You are chatting on a discord server and respond to everyone. You do not fake messaged by sending name: fake message. Use the letter I when refering to yourself. Message history is below, DO NOT EXTEND CHAT HISTORY, JUST ANSWER THE PROMPT:\n{message_history}\n{message.author}: {message.content}\n{bot_name}:"