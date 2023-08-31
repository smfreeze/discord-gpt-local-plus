import json
import requests
import sys

HOST = '127.0.0.1:5000'
URI = f'http://{HOST}/api/v1/generate'

async def get_response(prompt):

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


    try:
        response = requests.post(URI, json=request)
        if response.status_code == 200:
            try:
                result = response.json()['results'][0]['text']
                return result
            except (KeyError, json.JSONDecodeError) as e:
                print(e)
    except Exception as e:
        print(e)
        sys.exit(1)

async def check_api_endpoint():
    try:
        requests.get(URI)
        return True
    except:
        return False