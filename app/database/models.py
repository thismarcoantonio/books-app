import peewee

database = peewee.SqliteDatabase("books.sqlite")


class BaseModel(peewee.Model):
    class Meta:
        database = database


class Author(BaseModel):
    name = peewee.CharField(unique=True)


class Book(BaseModel):
    title = peewee.CharField(unique=True)
    author = peewee.ForeignKeyField(Author)


if __name__ == "__main__":
    try:
        Author.create_table()
    except peewee.OperationalError:
        print("Error creating 'Author' table")

    try:
        Book.create_table()
    except peewee.OperationalError:
        print("Error creating 'Book' table")
