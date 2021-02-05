from apps import db, ma


class Evolution(db.Model):
    __tablename__ = 'evolutions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)
    primary = db.Column(db.Boolean)
    regular = db.Column(db.Boolean)
    gender = db.Column(db.String(200), nullable=True)
    held_item = db.Column(db.String(200), nullable=True)
    item = db.Column(db.String(200), nullable=True)
    know_move = db.Column(db.String(200), nullable=True)
    know_move_type = db.Column(db.String(200), nullable=True)
    location = db.Column(db.String(200), nullable=True)
    min_affection = db.Column(db.String(200), nullable=True)
    min_beauty = db.Column(db.String(200), nullable=True)
    min_happiness = db.Column(db.String(200), nullable=True)
    min_level = db.Column(db.String(200), nullable=True)
    needs_overworld_rain = db.Column(db.String(200), nullable=True)
    party_species = db.Column(db.String(200), nullable=True)
    party_type = db.Column(db.String(200), nullable=True)
    relative_physical_stats = db.Column(db.String(200), nullable=True)
    time_of_day = db.Column(db.String(200), nullable=True)
    trader_species = db.Column(db.String(200), nullable=True)
    turn_upside_down = db.Column(db.String(200), nullable=True)
    url_imagem_evolute = db.Column(db.String(500), nullable=True)
    evolution_chain = db.Column(db.Integer, nullable=True)
    image = db.Column(db.String(200))

    def __init__(self, id, **kwargs):
        self.id = id
        self.information = kwargs


class EvolutionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'primary', 'regular','gender', 'held_item', 'item', 'know_move', 'know_move_type', 'location', 'min_affection', 'min_beauty', 'min_happiness','min_level', 'needs_overworld_rain','party_species', 'party_type', 'relative_physical_stats', 'time_of_day', 'trader_species', 'turn_upside_down', 'url_imagem_evolute', 'image')


evolution_share_schema = EvolutionSchema()
evolutions_share_schema = EvolutionSchema(many=True)
