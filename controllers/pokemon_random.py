from models import locations_share_schema, pokemons_share_random, Location, Pokemon
from random import randint

class Random:

    def __init__(self):
        self.field = self.random(1)
        self.pond = self.random(2)
        self.forest = self.random(3)
        self.mountain = self.random(4)
        self.sea = self.random(5)
        self.secret = self.random(6)

    
    def random(self, id):
        local = locations_share_schema.dump(Location.query.filter_by(id=id))
        pokemon_random = pokemons_share_random.dump(Pokemon.query.filter_by(
            localization=local[0]['name']))
        rate = []

        for pokemon in pokemon_random:
            for index in range(pokemon['rate']):
                rate.append(pokemon['id'])
            
        return rate

    def get_local(self, id):
        local = {
            1 : self.field,
            2 : self.pond,
            3 : self.forest,
            4 : self.mountain,
            5 : self.sea,
            6 : self.secret
        }

        return local[id]

    def get_five_pokemon(self, id):
        rate = self.get_local(id)
 
        pokemon_ids_found = []

        while True:
            id_pokemon = rate[randint(0, len(rate))]
            if id_pokemon not in pokemon_ids_found:
                pokemon_ids_found.append(id_pokemon)
                if len(pokemon_ids_found) == 5:
                    break

        return pokemon_ids_found

random = Random()