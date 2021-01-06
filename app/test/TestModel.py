from app import db
from app.model import (
    Parent,
    Child,
    Ancestor,
    Descendent,
    Comment,
    Post,
    Book,
    Pen,
    House,
    People,
    Association,
)

# Test 1: one to many - backref
def test_1_1():
    parent = Parent(id=1, name="Mccree")
    parent2 = Parent(id=2, name="Junkrat")
    parent3 = Parent(id=3, name="Pharah")
    db.session.add(parent)
    db.session.add(parent2)
    db.session.add(parent3)
    db.session.commit()
    pass


def test_1_2():
    child = Child(id=1, name="Reinhardt", parent_id=1)
    child2 = Child(id=2, name="Mercy", parent_id=1)
    child3 = Child(id=3, name="Ana", parent_id=2)
    db.session.add(child)
    db.session.add(child2)
    db.session.add(child3)
    db.session.commit()
    pass


def test_1_3():
    parent = Parent.query.filter_by(id=1).first()
    print("parent", parent.__dict__)
    for children in parent.children:
        print(children.parent.__dict__)


# Test 2: one to many - back_populates
def test_2_1():
    ancestor = Ancestor(id=1, name="Mccree")
    ancestor2 = Ancestor(id=2, name="Junkrat")
    ancestor3 = Ancestor(id=3, name="Pharah")
    db.session.add(ancestor)
    db.session.add(ancestor2)
    db.session.add(ancestor3)
    db.session.commit()


def test_2_2():
    descendent = Descendent(id=1, name="Reinhardt", ancestor_id=1)
    descendent2 = Descendent(id=2, name="Mercy", ancestor_id=1)
    descendent3 = Descendent(id=3, name="Ana", ancestor_id=2)
    db.session.add(descendent)
    db.session.add(descendent2)
    db.session.add(descendent3)
    db.session.commit()


def test_2_3():
    ancestor = Ancestor.query.filter_by(id=1).first()
    print("ancestor", ancestor.__dict__)
    for descendent in ancestor.descendent:
        print(descendent.ancestor.__dict__)


# Test 3: many to one
def test_3_1():
    post = Post(id=1, name="science")
    post2 = Post(id=2, name="history")
    post3 = Post(id=3, name="physical")
    db.session.add(post)
    db.session.add(post2)
    db.session.add(post3)
    db.session.commit()


def test_3_2():
    comment = Comment(id=1, name="nice", post_id=1)
    comment2 = Comment(id=2, name="good", post_id=1)
    comment3 = Comment(id=3, name="great", post_id=2)
    db.session.add(comment)
    db.session.add(comment2)
    db.session.add(comment3)
    db.session.commit()


def test_3_3():
    post = Post.query.filter_by(id=1).first()
    print("post", post.comments)

    comment = Comment.query.filter_by(id=1).first()
    print("comment", comment.__dict__)
    print("post", comment.post.comments)


# Test 4: one to one
def test_4_1():
    book = Book(id=1, name="science")
    book2 = Book(id=2, name="history")
    book3 = Book(id=3, name="physical")
    db.session.add(book)
    db.session.add(book2)
    db.session.add(book3)
    db.session.commit()


def test_4_2():
    pen = Pen(id=1, name="color", book_id=1)
    # Error: 1->1
    # pen2 = Pen(id=2, name="pencil", book_id=1)
    db.session.add(pen)
    # db.session.add(pen2)
    db.session.commit()


# Test 5: many to many
def test_5_1():
    house = House(id=1, name="villa")
    house2 = House(id=2, name="mansion")
    house3 = House(id=3, name="office")
    db.session.add(house)
    db.session.add(house2)
    db.session.add(house3)
    db.session.commit()


def test_5_2():
    people = People(id=1, name="Mccree")
    people2 = People(id=2, name="Junkrat")
    people3 = People(id=3, name="Pharah")
    db.session.add(people)
    db.session.add(people2)
    db.session.add(people3)
    db.session.commit()


def test_5_3():
    myhouse = House.query.filter_by(id=1).first()
    print("house", myhouse.__dict__)
    mypeople = People.query.filter_by(id=1).first()
    print("house", mypeople.__dict__)
    myhouse.people.append(mypeople)
    db.session.commit()
