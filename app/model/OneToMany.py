from app import db


# If you use backref you don't need to declare the relationship on the second table.
class Parent(db.Model):
    __tablename__ = "parent"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True)
    children = db.relationship("Child", backref="parent")


class Child(db.Model):
    __tablename__ = "child"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True)
    parent_id = db.Column(db.Integer, db.ForeignKey("parent.id"))


class Ancestor(db.Model):
    __tablename__ = "ancestor"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True)
    descendent = db.relationship("Descendent", back_populates="ancestor")


class Descendent(db.Model):
    __tablename__ = "descendent"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True)
    ancestor_id = db.Column(db.Integer, db.ForeignKey("ancestor.id"))
    ancestor = db.relationship("Ancestor", back_populates="descendent")
