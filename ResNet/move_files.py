import os
import shutil
import json
from random import randint

with open('./pokemon_full.json') as f:
    data = json.load(f)

# print(data)
os.mkdir('./train')
os.mkdir('./test')

for pkm in data:
    # print('./pokemons/{id}.png'.format(id = pokemon['id']))
    # print(pkm["type"])
    for pkm_type in pkm['type']:
        original_path = './pokemons/{id}.png'.format(id = pkm['id'])
        train_path = './train/{type}/{id}.png'.format(type = pkm_type, id = pkm['id'])
        test_path = './test/{type}/{id}.png'.format(type = pkm_type, id = pkm['id'])
        rd = randint(0,6)
        try:
            if rd <= 5:
                shutil.copy(original_path, train_path)
            else:
                shutil.copy(original_path, test_path)
        except FileNotFoundError:
            if rd <= 5:
                os.mkdir('./train/{type}'.format(type = pkm_type))
                shutil.copy(original_path, train_path)
            else:
                os.mkdir('./test/{type}'.format(type = pkm_type))
                shutil.copy(original_path, test_path)
