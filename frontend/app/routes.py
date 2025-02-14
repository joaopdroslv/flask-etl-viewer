from repository.sales import SalesRepository

from flask import Blueprint, render_template, jsonify


bp = Blueprint('webui', __name__, url_prefix='/webui', template_folder='templates')


@bp.route('/ping')
def ping():
    return jsonify({'message': 'pong'})

@bp.route('/sales')
def sales():
    sales_repo = SalesRepository()
    sales = sales_repo.select()
    return render_template('index.html')
