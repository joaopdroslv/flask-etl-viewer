from repository.products import ProductsRepository
from repository.buyers import BuyersRepository
from repository.sellers import SellersRepository
from repository.sales import SalesRepository

from faker import Faker
import random
import datetime


def generate_product() -> None:
    faker = Faker('en_US')
    name = faker.unique.word()
    price = round(random.uniform(10, 1000), 2)
    products_repo = ProductsRepository()
    products_repo.insert(name, price)


def generate_profile(type: str) -> None:
    faker = Faker('en_US')
    profile = faker.profile()

    if type == 'buyer':
        buyers_repo = BuyersRepository()
        buyers_repo.insert(
            profile['name'], 
            profile['sex'],
            random.randint(21, 75),
            profile['address'],
            profile['mail']
        )
    elif type == 'seller':
        sellers_repo = SellersRepository()
        sellers_repo.insert(
            profile['name'], 
            profile['sex'],
            random.randint(21, 55),
            profile['address'],
            profile['mail']
        )


def generate_sale() -> None:
    faker = Faker('en_US')

    products_repo = ProductsRepository()
    products = products_repo.select()

    buyers_repo = BuyersRepository()
    buyers = buyers_repo.select()

    sellers_repo = SellersRepository()
    sellers = sellers_repo.select()

    payment_methods = [
        'Credit Card (Visa)', 'Credit Card (MasterCard)', 'Credit Card (American Express)', 
        'Debit Card', 'Pix', 'Cash', 'Bank Transfer', 'Cryptocurrency (Bitcoin)', 
        'Cryptocurrency (Ethereum)', 'PayPal', 'Google Pay', 'Apple Pay'
    ]

    product = random.choice(products)
    p_id, p_name, p_price, p_created_at, p_updated_at = product
    p_price = float(p_price)

    buyer = random.choice(buyers)
    b_id, b_name, b_sex, b_age, b_address, \
        b_contact, b_created_at, b_updated_at = buyer

    seller = random.choice(sellers)
    s_id, s_name, s_sex, s_age, s_address, \
        s_contact, s_created_at, s_updated_at = seller

    start_date = datetime.date(2010, 1, 1)
    end_date = datetime.date(2025, 1, 1)
    delta_days = (end_date - start_date).days
    sale_date = start_date + datetime.timedelta(days=random.randint(0, delta_days))

    units_sold = random.randint(1, 10)
    unit_price = round(p_price * (1 + random.uniform(-0.1, 0.1)), 2)
    payment_method = random.choice(payment_methods)
    discount = True if random.choice([1, 3, 5, 7, 10]) % 2 == 0 else False 
    discount_perc = random.randint(5, 10) if discount else 0

    sales_repo = SalesRepository()
    sales_repo.insert(p_id, b_id, s_id, sale_date, units_sold, 
                      unit_price, payment_method, discount, discount_perc)
