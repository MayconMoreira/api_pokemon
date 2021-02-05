from apps import db, ma


class Location(db.Model):
    __tablename__ = 'location'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(84), nullable=False, primary_key=True)

    def __init__(self, name):
        self.name = name


class LocationSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

locations_share_schema = LocationSchema(many=True)

