import datetime
from random import randint, sample

from apps import db
from models import (Backpack, Evolution, Location, Pokemon,
                    evolutions_share_schema, locations_share_schema,
                    pokemons_share_schema, pokemons_share_sorted, backpacks_share_schema)

from .evolution_control import evolution_control
from .pokemon_random import random


class PokemonControl:

    def __init__(self):
        self.db = db

    def count(self):
        return self.db.session.query(Pokemon.id).count()

    def insert(self, model):
        self.db.session.add(model)
        self.db.session.commit()

    def search_pokemon(self, id):
        filters_evolutions = ['primary', 'regular']
        filters_pokemon = ['id', 'name', 'height', 'weight',
                           'localization', 'rate', 'male', 'female', 'genderless']
        filters_sprites = ['front_default', 'back_default', 'front_female', 'back_female',
                           'front_default_shiny', 'back_default_shiny', 'front_female_shiny', 'back_female_shiny']
        filters_types = ['type_one', 'type_two']

        data = {'sprites': [], 'types': {}, 'evolutions': {}}

        pokemon = pokemons_share_schema.dump(Pokemon.query.filter_by(id=id))
        pokemon_clean_data = {key: value for key,
                              value in pokemon[0].items() if value != 'None'}

        data_evolutions = evolution_control.search_evolutions(
            pokemon[0]['evolution_chain'], id)

        for key in filters_sprites:
            if key in pokemon_clean_data.keys():
                data['sprites'].append(
                    {'name': key, 'value': pokemon_clean_data[key]})

        data['evolutions'].update(data_evolutions)
        data.update({key: value for key,
                     value in pokemon_clean_data.items() if key in filters_pokemon})
        data['types'].update(
            {key: value for key, value in pokemon_clean_data.items() if key in filters_types})
        data['evolutions'].update(
            {key: value for key, value in pokemon_clean_data.items() if key in filters_evolutions})

        return data

    def sorted_pokemon(self, current_user, local):
        pokemon_random_ids = random.get_five_pokemon(local)
        data = []
        sorted = []

        for id_for_pokemon in pokemon_random_ids:
            data.append(pokemons_share_sorted.dump(
                Pokemon.query.filter_by(id=id_for_pokemon)))

        for pokemon in data:
            sorted.append({key: value for key, value in pokemon[0].items()})
        
        return sorted

    def return_pokemon_for_id(self, id):

        return pokemons_share_sorted.dump(Pokemon.query.filter_by(id=id))

    def attempt_capture(self, id):

        pokemon_capture = Pokemon.query.filter_by(id=id).order_by()
        for pokemon in pokemon_capture:
            rate = [id]*(3*pokemon.rate)

        while len(rate) < 100:
            rate.append(False)

        if sample(rate, 1)[0] == id:
            return True
        return False


pokemon_control = PokemonControl()
