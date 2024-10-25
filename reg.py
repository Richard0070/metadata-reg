import os
import requests

DISCORD_CLIENT_ID = os.getenv('CLIENT_ID')
DISCORD_TOKEN = os.getenv('TOKEN')

def push_metadata():
    url = f"https://discord.com/api/v10/applications/{DISCORD_CLIENT_ID}/role-connections/metadata"
    body = [
        {  
            "key": "is_heisenberg",
            "name": "the one who knocks",
            "description": "Heisenberg",      
            "type": 7
        }
    ]
    
    headers = {
        'Authorization': f'Bot {DISCORD_TOKEN}',
        'Content-Type': 'application/json',
    }
    
    try:
        response = requests.put(url, headers=headers, json=body)
        response.raise_for_status()
        print("Metadata pushed successfully.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

push_metadata()
