from . import db


class Property(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    no_of_bedrooms = db.Column(db.Integer())
    no_of_bathrooms = db.Column(db.Integer())
    location = db.Column(db.String(80))
    typep = db.Column(db.Enum(["house","apartment"]))
    description = db.Column(db.String(255))
    photo location = db.Column(db.String(80))
    