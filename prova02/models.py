import os
import datetime
import peewee
from dotenv import load_dotenv

load_dotenv()

POSTGRES_HOST = os.getenv("POSTGRES_HOST", "")
POSTGRES__DATABASE = os.getenv("POSTGRES__DATABASE", "")
POSTGRES_USER = os.getenv("POSTGRES_USER", "")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "")


db = peewee.PostgresqlDatabase(
    POSTGRES__DATABASE,
    user=POSTGRES_USER,
    host=POSTGRES_HOST,
    password=POSTGRES_PASSWORD
)

class BaseModel(peewee.Model):
    class Meta:
        database = db

class Usuario(BaseModel):
    username = peewee.CharField(unique=True)
    password = peewee.CharField()
    join_date = peewee.DateTimeField(default=datetime.datetime.now)

    def __repr__(self):
        return self.username


class Produto(BaseModel):
    descricao = peewee.CharField()
    quantidade = peewee.IntegerField()
    user = peewee.ForeignKeyField(Usuario)
    create_at = peewee.DateTimeField(default=datetime.datetime.now)

    def __repr__(self):
        return self.descricao


def create_tables():
    with db:
        db.create_tables([Produto, Usuario])