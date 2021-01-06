from app import db


class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))
    post = db.relationship("Post", backref="comments")


class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True)
