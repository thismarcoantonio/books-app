import click
import peewee
from flask import g
from .models import database, Author, Book


def get_db():
    if "db" not in g:
        g.db = database

    return g.db


def close_db(self):
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    database.connect()


@click.command("init-db")
def init_db_command():
    db = get_db()
    db.create_tables([Author, Book])
    click.echo("Initialized the database.")
