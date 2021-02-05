from apps import db
from models import Location, locations_share_schema

class LocationControl:

    def __init__(self):
        self.db = db

    def count(self):
        return self.db.session.query(Location.id).count()

    def get_all_locations(self):
        return locations_share_schema.dump(Location.query.all())

location_control = LocationControl()