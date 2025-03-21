# ORM mapowanie obiektowo relacyjne
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


# encja - klasa odwzorowyjąca tabele z bazy danych
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"{self.name}, {self.age}"


engine = create_engine('sqlite:///mydatabase.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name='Jan Kowalski', age=30)
session.add(new_user)  # INSERT INTO users (name, age) VALUES (?, ?)
session.commit()
session.close()

users = session.query(User).all()
for user in users:
    print(user)
# SELECT users.id AS users_id, users.name AS users_name, users.age AS users_age
# FROM users
# Jan Kowalski, 30
# Jan Kowalski, 30
# Jan Kowalski, 30
