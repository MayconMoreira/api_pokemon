from apps import db, ma



class Backpack(db.Model):
    __tablename__ = 'backpack'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer, nullable=True, autoincrement=False)
    captured = db.Column(db.Boolean)
    id_pokemon = db.Column(db.Integer, nullable=True, autoincrement=False)
    name = db.Column(db.String(84), nullable=False)
    nickname = db.Column(db.String(84), nullable=True)
    image = db.Column(db.String(256))
    date = db.Column(db.DateTime, nullable=True)

    def __init__(self, id_user, captured, id_pokemon, name, image, date=None, nickname=None):
        self.id_user = id_user
        self.captured = captured
        self.id_pokemon = id_pokemon
        self.name = name
        self.nickname = nickname
        self.image = image
        self.date = date


class BackpackSchema(ma.Schema):
    class Meta:
        fields = ('id_user', 'captured', 'id_pokemon', 'name', 'nickname', 'image', 'date')


backpack_share_schema = BackpackSchema()
backpacks_share_schema = BackpackSchema(many=True)
