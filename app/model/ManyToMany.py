from app import db

# # back_populates
# class Association(db.Model):
#     __tablename__ = 'association'
#     house_id = db.Column(db.Integer, db.ForeignKey('house.id'), primary_key=True)
#     people_id = db.Column(db.Integer, db.ForeignKey('people.id'), primary_key=True)
#     extra_data = db.Column(db.String(50))
#     people = db.relationship("People", back_populates="houses")
#     house = db.relationship("House", back_populates="people")

# class House(db.Model):
#     __tablename__ = 'house'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(60), index=True)
#     people = db.relationship("Association", back_populates="house")

# class People(db.Model):
#     __tablename__ = 'people'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(60), index=True)
#     houses = db.relationship("Association", back_populates="people")


# backref
class Association(db.Model):
    __tablename__ = "association"
    house_id = db.Column(db.Integer, db.ForeignKey("house.id"), primary_key=True)
    people_id = db.Column(db.Integer, db.ForeignKey("people.id"), primary_key=True)
    extra_data = db.Column(db.String(50))
    people = db.relationship("People", backref="house_associations")
    house = db.relationship("House", backref="people_associations")


class House(db.Model):
    __tablename__ = "house"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True)
    people = db.relationship("People", secondary="association")


class People(db.Model):
    __tablename__ = "people"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True)
