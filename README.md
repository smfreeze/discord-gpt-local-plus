# AI Chatbot made in python with discord.py functionality
Locally run (no chat-gpt) Oogabooga AI Chatbot made with discord.py

This is completely free and doesn't require chat gpt or any API key. You run the large language models yourself using [the oogabooga text generation web ui](https://github.com/oobabooga/text-generation-webui).

Records chat history up to 99 messages for EACH discord channel (each channel will have its own unique history and its own unique responses from the bot as a result)

### Examples:

<img src="https://github.com/smfreeze/discord-local-ai-chatbot/assets/117759431/40fd7f89-6d20-426f-977a-417879b6738e" width=450px height=650px>
<img src="https://github.com/smfreeze/discord-local-ai-chatbot/assets/117759431/019f7531-362a-4249-81a8-d9c36f153ebf">
The latter image is an example of the /clearchathistory command and its 10% chance to express itself after running said command (thought it would be funny). This can be disabled in bot.py if you want.


## Setup
### Step 1:
```
git clone
cd discord-local-chatbot
pip install requirements.txt
```
### Step 2:
Open config.ini file in text editor, add your [bot token](https://www.youtube.com/watch?v=aI4OmIbkJH8) to the bot_token parameter and save (also change other parameters as you see fit).

### Step 3:
Complete oogabooga setup guide below:




























## Usage
```
cd discord-local-ai-chatbot
python bot.py
```

Just run bot.py after successfully setting it up.
