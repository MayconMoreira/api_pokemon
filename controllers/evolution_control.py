from apps import db
from models import Evolution, evolutions_share_schema

class EvolutionControl:
    
    def __init__(self):
        self.db = db
    
    def search_evolutions(self, evolution_chain, id):

        primary = None
        regular = None

        data_evolutions = {'pokemons': []}
        evolutions = evolutions_share_schema.dump(Evolution.query.filter_by(evolution_chain=evolution_chain).order_by(Evolution.primary.desc()))
        

        pokemons = []
        is_pokemon = False
        evolutions_clean_data = []

        for evolution in evolutions:
            if evolution['id'] == id:
                is_pokemon = True
                primary = evolution['primary']
                regular = evolution['regular']
            if is_pokemon:
                pokemons.append(evolution)
        
        for index in range(len(pokemons)):
            
            data_trigger = []
            filter_trigger = []
            evolutions_clean_data.append(
                {key: value for key, value in pokemons[index].items() if value != 'None'})
            if evolutions_clean_data[index]['id'] != id:
                data_trigger.append({key: value for key, value in evolutions_clean_data[index].items(
                ) if key != 'id' and key != 'name' and key != 'url_imagem_evolute' and key !='primary'and key != 'regular'})
                
                for ind in range(len(data_trigger)):
                    for key, value in data_trigger[ind].items():
                        if key == 'item':
                            filter_trigger.append({'name': key, 'value': value, 'image': data_trigger[ind]['image']})
                        elif key != 'image':
                            filter_trigger.append({'name': key.replace('_', ' '), 'value': value})
            
                evolutions_clean_data[index].update({'details': filter_trigger})
                evolutions_clean_data[index].update({'image': evolutions_clean_data[index]['url_imagem_evolute']})
                data_evolutions['pokemons'].append({key: value for key, value in evolutions_clean_data[index].items(
                ) if key == 'id' or key == 'name' or key == 'image' or key == 'details'})

        if len(data_evolutions['pokemons']) == 0 or not regular and not primary:
            return {'pokemons': []}
        return data_evolutions

evolution_control = EvolutionControl()