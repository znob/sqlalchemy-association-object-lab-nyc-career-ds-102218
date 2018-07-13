from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

# Write your classes below






engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
