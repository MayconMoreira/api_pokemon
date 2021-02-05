from apps import db, ma


class Pokemon(db.Model):

    __tablename__ = 'pokemons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(84), nullable=False)
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    primary = db.Column(db.Boolean)
    regular = db.Column(db.Boolean)
    male = db.Column(db.Boolean)
    female = db.Column(db.Boolean)
    genderless = db.Column(db.Boolean)
    type_one = db.Column(db.String(84))
    type_two = db.Column(db.String(84))
    localization = db.Column(db.String(84))
    rate = db.Column(db.Integer)
    front_default = db.Column(db.String(256))
    back_default = db.Column(db.String(256))
    front_female = db.Column(db.String(256))
    back_female = db.Column(db.String(256))
    front_default_shiny = db.Column(db.String(256))
    back_default_shiny = db.Column(db.String(256))
    front_female_shiny = db.Column(db.String(256))
    back_female_shiny = db.Column(db.String(256))
    evolution_chain = db.Column(db.Integer)

    def __init__(self, id, name,  **kwargs):
        self.id = id
        self.name = name
        self.information = kwargs


class PokemonSorted(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'front_default', 'rate')

pokemons_share_sorted = PokemonSorted(many=True)


class PokemonSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'height', 'weight', 'primary', 'regular', 'male', 'female', 'genderless', 'type_one', 'type_two', 'localization', 'rate', 'front_default',
                  'back_default', 'front_female', 'back_female', 'front_default_shiny', 'back_default_shiny', 'front_female_shiny', 'back_female_shiny', 'evolution_chain')

pokemons_share_schema = PokemonSchema(many=True)

class PokemonRandom(ma.Schema):
    class Meta:
        fields = ('id', 'rate')

pokemons_share_random = PokemonRandom(many=True)