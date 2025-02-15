from repository.sales import SalesRepository
from repository.products import ProductsRepository
from repository.buyers import BuyersRepository
from repository.sellers import SellersRepository

from flask import Blueprint, render_template


bp = Blueprint('webui', __name__, url_prefix='/webui', template_folder='templates', static_folder='static')


@bp.route('/', methods=['GET'])
def homepage():
    return render_template('homepage.html')

@bp.route('/sales', methods=['GET'])
def sales():
    sales_repo = SalesRepository()
    sales = sales_repo.select()
    return render_template('sales.html', sales=sales)

@bp.route('/products', methods=['GET'])
def products():
    products_repo = ProductsRepository()
    products = products_repo.select()
    return render_template('products.html', products=products)

@bp.route('/buyers', methods=['GET'])
def buyers():
    buyers_repo = BuyersRepository()
    buyers = buyers_repo.select()
    return render_template('buyers.html', buyers=buyers)

@bp.route('/sellers', methods=['GET'])
def sellers():
    sellers_repo = SellersRepository()
    sellers = sellers_repo.select()
    return render_template('sellers.html', sellers=sellers)
