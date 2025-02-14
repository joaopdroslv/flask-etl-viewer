from repository.connection import DBConnectionHandler

from sqlalchemy import text


class ProductsRepository:
    def insert(self, name: str, price: float) -> None:
        with DBConnectionHandler() as db:
            query = text("""INSERT INTO products (name, price) VALUES (:name, :price)""")
            db.session.execute(
                query, {'name': name, 'price': price}
            )
            db.session.commit()

    def select(self) -> list:
        with DBConnectionHandler() as db:
            products = db.session.execute(text("""SELECT * FROM products"""))
            return products.fetchall()
