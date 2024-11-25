from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


engine = create_engine("sqlite:///pizzas.db", echo=True)
Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass

def create_db():
    Base.metadata.create_all(bind=engine)


def drop_db():
    Base.metadata.drop_all(bind=engine)