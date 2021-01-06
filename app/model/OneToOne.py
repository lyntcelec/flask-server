from app import db


class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True)
    pen = db.relationship("Pen", uselist=False, back_populates="book")


class Pen(db.Model):
    __tablename__ = "pen"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"))
    book = db.relationship("Book", back_populates="pen")
