#!/usr/bin/env python3

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Game

fake = Faker()

if __name__ == '__main__':
    engine = create_engine('sqlite:///seed_db.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Game).delete()

    for _ in range(10):
        game = Game(
            title=fake.word(),
            genre=fake.word(),
            platform=fake.word(),
            price=random.randint(10, 100),
        )
        session.add(game)

    session.commit()