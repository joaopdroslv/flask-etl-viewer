from repository.connection import DBConnectionHandler

from sqlalchemy import text
from decimal import Decimal


class SalesRepository:
    def insert(
            self, product_id: int, buyer_id: int, seller_id: int, sale_date, units_sold: int,
            unit_price: float, payment_method: str, discount: bool, discount_perc: int
            ) -> None:
        with DBConnectionHandler() as db:
            query = text("""
                INSERT INTO sales (product_id, buyer_id, seller_id, sale_date, units_sold, unit_price, payment_method, discount, discount_perc) 
                VALUES (:product_id, :buyer_id, :seller_id, :sale_date, :units_sold, :unit_price, :payment_method, :discount, :discount_perc)
            """)
            db.session.execute(
                query, {
                    'product_id': product_id,
                    'buyer_id': buyer_id,
                    'seller_id': seller_id,
                    'sale_date': sale_date,
                    'units_sold': units_sold,
                    'unit_price': Decimal(unit_price),
                    'payment_method': payment_method,
                    'discount': discount,
                    'discount_perc': discount_perc
                }
            )
            db.session.commit()

    def select(self) -> list:
        with DBConnectionHandler() as db:
            sales = db.session.execute(text("""SELECT * FROM sales"""))
            return sales.fetchall()
