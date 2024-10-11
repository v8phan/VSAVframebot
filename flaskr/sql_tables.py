from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from moveparser import moveparser, listoftuples
import requests



class Base(DeclarativeBase):
    pass

class Character(Base):
    __tablename__ = 'characters'

    charName: Mapped[str] = mapped_column(primary_key=True)
    charImage: Mapped[str]
    
    def __repr__(self):
        return f"({self.charName}, {self.charImage})"

class Move(Base):
    __tablename__ = 'moves'

    moveId: Mapped[str] = mapped_column(primary_key=True)
    chara: Mapped[str] = mapped_column(ForeignKey("characters.charName"))
    input: Mapped[str]
    images: Mapped[str]
    hitboxes: Mapped[str]
    reddmg: Mapped[str]
    whitedmg: Mapped[str]
    guard: Mapped[str] 
    startup: Mapped[str]
    active: Mapped[str]
    recovery: Mapped[str]
    advHit: Mapped[str]
    advBlock: Mapped[str]
    advTech: Mapped[str] 
    invul: Mapped[str]
    cancel: Mapped[str]
    renda: Mapped[str]
    meter: Mapped[str]
    reaction: Mapped[str]
    cursetime: Mapped[str]


#engine

# user = 'postgres'
# password = 'Pviet95.'
# host = 'localhost'
# port = '5432'
# database = 'VSAV'

user = "postgres.zuidpuiggoibnnvrtbfn"
password = "xDohks76sW%Y"
host = "aws-0-us-east-1.pooler.supabase.com"
port = "6543"
database = "postgres"

# for creating connection string
connection_str = f'postgresql://{user}:{password}@{host}:{port}/{database}'
engine = create_engine(connection_str, echo=True)

#creates tables, only needed once
# Base.metadata.create_all(engine)

#test if connect
try:
    with engine.connect() as connection_str:
        print('Successfully connected to the PostgreSQL database')
except Exception as ex:
    print(f'Sorry failed to connect: {ex}')


