# AI Chatbot made in python with discord.py functionality
Locally run (no chat-gpt) Oogabooga AI Chatbot made with discord.py

This is completely free and doesn't require chat gpt or any API key. You run the large language models yourself using [the oogabooga text generation web ui](https://github.com/oobabooga/text-generation-webui).

Records chat history up to 99 messages for EACH discord channel (each channel will have its own unique history and its own unique responses from the bot as a result)

Loosely inspired by [DeSinc's sallybot](https://github.com/DeSinc/SallyBot).
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

## Oogabooga setup
(Thanks [DeSinc](https://github.com/DeSinc/SallyBot) for some data regarding this Oogabooga setup guide)
<br><br>
Warning: For the average 7B model, it requires a card with at least 6GB of VRAM, 10GB for 13B.

Download and install [Oobabooga from their repo here](https://github.com/oobabooga/text-generation-webui). Information on how to install in README, but basically just use 1-click installer.

After downloading and unzipping the 1-click installer, run `start_windows.bat`. The installer is interactive and you will need to enter your GPU device when prompted (could use CPU mode, but GPU mode recommended by me)

The install script should then give you a web address to the web ui after installing requirements, go to the model section of said web ui. Install a model (look on HugginFace), copy the model name and paste into model download section (many tutorials of this exist) and then download.

After the installing has finished you need to set up the arguements in the `webui.py` file to allow the script to communicate with Oobabooga. It can be found near the top of the file.

![Showing where to input args](https://github.com/DeSinc/SallyBot/assets/36467674/a7c6e8b0-6644-4c73-878b-9b2cb44c1d3a)

Arguments to be added here include:

`--chat` sets the web interface to chat mode which is better. This arg isn't necessary it just makes the web interface look nicer if you choose to browse to it on localhost:7862 in your web browser.

`--model <folder_name_of_model>` specifies which model Oobabooga should use, replace `<folder_name_of_model>` it is the name of the folder in text-generation-webui/models.

`--api` tells Oobabooga to allow the program to integrate together.

`--loader exllama_hf` uses the much updated ExLLAMA model loader which is literally nearly 2x faster than the previously used loader. Might already be default by the time you see and run this.

`--listen-port 7862` is set to 7862 to not overlap with stable diffusion. `--api` opens a separate port for the program to interface with which runs on port 5000. Port 7862 is still used to view the web interface.

`--xformers` is a very good optimiser that reduces your vram usage for free. This argument is not required but very encouraged. It needs to be installed into Oobabooga to use. Run `cmd_windows.bat` and type `pip install xformers`, when it is done you can type exit.

`--wbits 4` and `--groupsize 128` specify details about the model. If you know what you're doing you can remove whichever ones you don't need. `--groupsize 128` if you are using a non 128 groupsize model, or `--wbits 4` if you are not running a 4-bit quantized model, for instance. Most of the consumer running ones are 4bit quantized to run on normal amounts of vram, so you'll need this arg to run those models.

Example of args:
`'--model TheBloke_Llama-2-7B-Chat-GGML --chat --listen-port 7862 --api'`

If you'd like to modify the parameters for Oobabooga, it's this section here of oogapi.py:
```py
request = {
        'prompt' : prompt,
        'max_new_tokens' : 750,
        
        'do_sample' : False,
        'temperature' : 1,
        'top_p' : 0,
        'typical_p' : 1,
        'repetition_penalty' : 1.18,
        'encoder_repetition_penalty' : 1,
        'top_k' : 40,
        'num_beams' : 1,
        'penalty_alpha' : 0,
        'min_length' : 0,
        'length_penalty' : 1,
        'no_repeat_ngram_size' : 0,

        'seed' : -1,
        'add_bos_token' : True,
        'ban_eos_token' : False,
        'skip_special_tokens' : True
    }
```


## Usage
```
cd discord-local-ai-chatbot
python bot.py
```

Just run bot.py after successfully setting it up.
