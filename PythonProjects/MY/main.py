import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '62df9a52a059754a849c5f434e39a500'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
POKEMON_ID = '27046'
body_registration = {
    "trainer_token": TOKEN,
    "email": "lpankov836@gmail.com",
    "password": "Iloveqa1"
} 
body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Бульбач",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
body_pokeball = {
    "pokemon_id": "27046"
}

body_name = {
    "pokemon_id": POKEMON_ID ,
    "name": "BULBA",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

'''responce = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json =  ) 
print(responce.text)'''


'''responce_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(responce_confirmation.text)'''

'''responce_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(responce_create.text)'''

'''responce_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball' , headers = HEADER , json = body_pokeball)
print(responce_pokeball.text)'''

responce_name = requests.put(url = f'{URL}/pokemons' , headers = HEADER , json = body_name)
print(responce_name.text)
