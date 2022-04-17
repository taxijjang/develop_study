from odmantic import AIOEngine, Model


class BookModel(Model):
    keyword: str
    publisher: str
    price: int
    image: str

    class Config:
        collection = 'books'
