""" Classes that manage database connections via SQLAlchemy Query API """

from utilities.db_helpers.db_connection import DBConnectionBase

CON_STR_TEMPLATE = '{dialect}://{user}:{password}@{host}:{port}/{database_name}'


class AccountManagement(DBConnectionBase):
    """
    Using the SQLAlchemy engine creates a connection for the Query API to perform actions on the
    account_management databases
    """
    def __init__(self, env_config):
        self._env = env_config['env']
        self._dialect = env_config['db_server_config']['dialect']
        self._database_name = env_config['databases']['account_management']
        self._user = env_config['db_server_config']['user']
        self._password = env_config['db_server_config']['password']
        self._host = env_config['db_server_config']['host']
        self._port = env_config['db_server_config']['port']
        DBConnectionBase.__init__(self, self.connection_string)

    @property
    def connection_string(self):
        return CON_STR_TEMPLATE.format(dialect=self._dialect,
                                       user=self._user,
                                       password=self._password,
                                       host=self._host,
                                       port=self._port,
                                       database_name=self._database_name)

    @property
    def database_name(self):
        return self._database_name

    def __str__(self):
        return 'RDSPostgresSQL("{}")'.format(self.connection_string)


class AccountOpeningAlloy(DBConnectionBase):
    """
    Using the SQLAlchemy engine creates a connection for the Query API to perform actions on the
    account_opening_alloy databases
    """
    def __init__(self, env_config):
        self._env = env_config['env']
        self._dialect = env_config['db_server_config']['dialect']
        self._database_name = env_config['databases']['account_opening_alloy']
        self._user = env_config['db_server_config']['user']
        self._password = env_config['db_server_config']['password']
        self._host = env_config['db_server_config']['host']
        self._port = env_config['db_server_config']['port']
        DBConnectionBase.__init__(self, self.connection_string)

    @property
    def connection_string(self):
        return CON_STR_TEMPLATE.format(dialect=self._dialect,
                                       user=self._user,
                                       password=self._password,
                                       host=self._host,
                                       port=self._port,
                                       database_name=self._database_name)

    @property
    def database_name(self):
        return self._database_name

    def __str__(self):
        return 'RDSPostgresSQL("{}")'.format(self.connection_string)


class AccountOpeningGalileo(DBConnectionBase):
    """
    Using the SQLAlchemy engine creates a connection for the Query API to perform actions on the
    account_opening_galileo databases
    """
    def __init__(self, env_config):
        self._env = env_config['env']
        self._dialect = env_config['db_server_config']['dialect']
        self._database_name = env_config['databases']['account_opening_galileo']
        self._user = env_config['db_server_config']['user']
        self._password = env_config['db_server_config']['password']
        self._host = env_config['db_server_config']['host']
        self._port = env_config['db_server_config']['port']
        DBConnectionBase.__init__(self, self.connection_string)

    @property
    def connection_string(self):
        return CON_STR_TEMPLATE.format(dialect=self._dialect,
                                       user=self._user,
                                       password=self._password,
                                       host=self._host,
                                       port=self._port,
                                       database_name=self._database_name)

    @property
    def database_name(self):
        return self._database_name

    def __str__(self):
        return 'RDSPostgresSQL("{}")'.format(self.connection_string)


class BankingDatabase(DBConnectionBase):
    """
    Using the SQLAlchemy engine creates a connection for the Query API to perform actions on the
    banking_db databases
    """
    def __init__(self, env_config):
        self._env = env_config['env']
        self._dialect = env_config['db_server_config']['dialect']
        self._database_name = env_config['databases']['banking_db']
        self._user = env_config['db_server_config']['user']
        self._password = env_config['db_server_config']['password']
        self._host = env_config['db_server_config']['host']
        self._port = env_config['db_server_config']['port']
        DBConnectionBase.__init__(self, self.connection_string)

    @property
    def connection_string(self):
        return CON_STR_TEMPLATE.format(dialect=self._dialect,
                                       user=self._user,
                                       password=self._password,
                                       host=self._host,
                                       port=self._port,
                                       database_name=self._database_name)

    @property
    def database_name(self):
        return self._database_name

    def __str__(self):
        return 'RDSPostgresSQL("{}")'.format(self.connection_string)


class WebDatabase(DBConnectionBase):
    """
    Using the SQLAlchemy engine creates a connection for the Query API to perform actions on the
    web_db databases
    """
    def __init__(self, env_config):
        self._env = env_config['env']
        self._dialect = env_config['db_server_config']['dialect']
        self._database_name = env_config['databases']['web_db']
        self._user = env_config['db_server_config']['user']
        self._password = env_config['db_server_config']['password']
        self._host = env_config['db_server_config']['host']
        self._port = env_config['db_server_config']['port']
        DBConnectionBase.__init__(self, self.connection_string)

    @property
    def connection_string(self):
        return CON_STR_TEMPLATE.format(dialect=self._dialect,
                                       user=self._user,
                                       password=self._password,
                                       host=self._host,
                                       port=self._port,
                                       database_name=self._database_name)

    @property
    def database_name(self):
        return self._database_name

    def __str__(self):
        return 'RDSPostgresSQL("{}")'.format(self.connection_string)
