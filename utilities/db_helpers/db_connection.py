""" SQLAlchemy Engine Creation Class"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from abc import ABCMeta, abstractmethod


class DBConnectionBase(object):
    """
    Base class for making SQLAlchemy connections
    ============================================
    Usage:
        class = MyProjectDB(DBConnectionBase):
            def __init__(self, env_config):
                self._env = env_config['env']
                self._dialect = env_config['db_server_config']['dialect']
                self._database_name = self.get_database_name()
                self._user = env_config['db_server_config']['user']
                self._password = env_config['db_server_config']['password']
                self._host = env_config['db_server_config']['host']
                self._port = env_config['db_server_config']['port']
                DBConnectionBase.__init__(self, self.connection_string)

            @property
            def connection_string(self):
                con_str_template = '{dialect}://{user}:{password}@{host}:{port}/{database_name}'
                return con_str_template.format(dialect=self._dialect,
                                               user=self._user,
                                               password=self._password,
                                               host=self._host,
                                               port=self._port,
                                               database_name=self._database_name
                                               )

        The example MyProjectDB class can be imported, then used as follows:
            with MyProjectDB(env_config) as db:
                obj = db.session.Query(ObjTable).first()
    """
    __metaclass__ = ABCMeta

    def __init__(self, connection_string):
        self.conn_string = connection_string
        self._session = None

    def __enter__(self):
        engine = create_engine(self.conn_string)
        session_maker = sessionmaker()
        session = session_maker(bind=engine)
        self.session = session
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    @property
    def session(self):
        return self._session

    @session.setter
    def session(self, sesh):
        self._session = sesh

    @abstractmethod
    def database_name(self):
        """ :return: database name """
        pass
