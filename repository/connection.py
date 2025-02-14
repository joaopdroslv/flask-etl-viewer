from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    # Creating a context manager to manage our sessions
    def __init__(self):
        self.__connection_string = 'mysql+pymysql://root:root_password@mysql:3306/sales_data_pipeline'
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_maker = sessionmaker(bind=self.__engine)
        self.session = session_maker()
        return self

    def __exit__(self, type, value, traceback):
        self.session.close()
