import pytest

from database_models import web_db_models

from sqlalchemy import Table, MetaData
from sqlalchemy import create_engine, inspect
from sqlalchemy.engine import reflection


@pytest.mark.db_connections
class TestORMSchemaValidations:
    """ Each test in this class validates their respective database schema """

    def test_compare_orm_web_db_schema_to_remote_web_db_schema(self, web_db_connection, env_config):
        """ Validates web_db schema by comparing local ORM Tables to Remote DB Tables """
        connection_string = web_db_connection.connection_string
        db_connection = create_engine(connection_string)
        metadata = MetaData(db_connection)
        inspection = reflection.Inspector.from_engine(db_connection)
        # web_db_models.tables is a list in the __init__.py containing all ORM table objects
        for orm_table in web_db_models.tables:
            orm_mapper = inspect(orm_table)
            # get each column/type from each ORM table
            orm_table_columns = [(c.key, str(c.type)) for c in orm_mapper.columns]
            # Generate remote table object for inspection to operate on
            remote_table = Table(orm_table.__tablename__, metadata, autoload=True)
            # get each column/type from each remote table where remote table is orm table
            remote_table_columns = [(rc['name'], str(rc['type']))
                                    for rc in inspection.get_columns(orm_table.__tablename__)]
            # sort lists for easier list comparison
            orm_table_columns.sort()
            remote_table_columns.sort()
            # todo GROW-1623: Implement Python Logging https://aspirationpartners.atlassian.net/browse/GROW-1623
            # Replace the following print statement with logging code
            print(f'Comparing column metadata of ORM Table "{orm_table.__tablename__}" '
                  f'to the column metadata of the Remote Table "{remote_table.name}"!')
            column_comparison_error = 'FAILED: The ORM table "{orm}" ' \
                                      'does not have equivalent column/type of remote table {remote}'.\
                format(orm=orm_table.__tablename__, remote=remote_table.name)
            assert orm_table_columns == remote_table_columns, column_comparison_error
