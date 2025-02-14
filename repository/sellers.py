from repository.connection import DBConnectionHandler

from sqlalchemy import text


class SellersRepository:
    def insert(self, name: str, sex: str, age: int, address: str, contact: str) -> None:
        with DBConnectionHandler() as db:
            query = text("""
                INSERT INTO sellers (name, sex, age, address, contact) 
                VALUES (:name, :sex, :age, :address, :contact)
            """)
            db.session.execute(
                query, {'name': name, 'sex': sex, 'age': age, 'address': address, 'contact': contact}
            )
            db.session.commit()

    def select(self) -> list:
        with DBConnectionHandler() as db:
            sellers = db.session.execute(text("""SELECT * FROM sellers"""))
            return sellers.fetchall()
