from apps import db
from models import backpacks_share_schema, Backpack, pokemons_share_sorted, Pokemon
from controllers.pokemon_control import pokemon_control
import datetime

class BackpackControl:

    def __init__(self):
        self.db = db

    def get_backpack(self, current_user):
        pokemon = backpacks_share_schema.dump(Backpack.query.filter_by(id_user=current_user.id))
        for index in range(len(pokemon)):
            if pokemon[index]['date'] == None:
                pass
            else:
                data = pokemon[index]['date'].split('T')
                pokemon[index]['date'] = '/'.join(data[0].split('-')) + ' ' + data[1]
        captured_amount = self.count_captured(current_user ,True)
        sighted_amount = self.count_captured(current_user, False)
        return pokemon, captured_amount, sighted_amount

    def insert(self, model):
        self.db.session.add(model)
        self.db.session.commit()

    def capture_for_current_backpack(self, current_user, id):
        try:
            Backpack.query.filter_by(id_user=current_user.id, id_pokemon=id, nickname=None).update(
            dict(captured=True, date=datetime.datetime.now() - datetime.timedelta(hours=3)))
            self.db.session.commit()
        except:
            raise BaseException
    
    def auth_nickname(self, current_user, id, nickname):
        if nickname:
            try:
                Backpack.query.filter_by(id_user=current_user.id, id_pokemon=id, nickname=None).update(
                dict(nickname=nickname))
                self.db.session.commit()
                return True
            except:
                return False
        return False
    
    def count_captured(self, current_user, boolean):
        return Backpack.query.filter_by(id_user=current_user.id, captured=boolean).count() 

    def sighted(self, current_user, id):
        pokemon_capture = pokemons_share_sorted.dump(Pokemon.query.filter_by(id=id))[0]
        pokemon_sighted = Backpack(current_user.id, False, id, pokemon_capture['name'], pokemon_capture['front_default'], None, None)
        pokemon_by_id =  Backpack.query.filter_by(id_user=current_user.id, id_pokemon=id).all()
        can_add = True
        for pokemon in pokemon_by_id:
            if not pokemon.nickname and not pokemon.captured:
                can_add = False
            elif pokemon.captured and not pokemon.nickname:
                try:
                    Backpack.query.filter_by(id_user=current_user.id, id_pokemon=id, nickname=None, captured=True).update(
                    dict(nickname=pokemon.name))
                    self.db.session.commit()
                except:
                    pass
        if can_add:
            try:
                self.insert(pokemon_sighted)
            except:
                pass
        return True
        

backpack_control = BackpackControl()