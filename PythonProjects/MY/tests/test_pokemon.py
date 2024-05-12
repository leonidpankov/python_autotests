import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'TOKEN'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '4063'

def test_status_code():
    responce = requests.get(url = f'{URL}/trainers')
    assert responce.status_code == 200

def test_part_of_responce():
        responce_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
        assert responce_get.json()["data"][0]["trainer_name"] == 'капот'