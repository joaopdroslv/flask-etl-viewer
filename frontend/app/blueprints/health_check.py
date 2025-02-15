from repository.connection import DBConnectionHandler

from flask import Blueprint, render_template, jsonify
from sqlalchemy import text


bp = Blueprint('health-check', __name__, url_prefix='/health-check')


@bp.route('/ping', methods=['GET'])
def ping():
    try:
        with DBConnectionHandler() as db:
            db.session.execute(text("""SELECT 1"""))
        return jsonify({'message': 'pong', 'database': 'ok'}), 200
    except Exception as e:
        return jsonify({'message': 'error', 'database': 'error', 'detail': str(e)}), 500
