import crud
import utils

# Start connection to rds
connection_rds = crud.create_db_connection_rds()

# Validing connection to rds
if connection_rds.is_connected():

    # Example create
    # Inform params to create
    table = 'crudpython'

    coluns = ['crudid', 'nome', 'sobrenome', 'to_date']

    values = ['1', 'create', 'crudteste', f'{utils.get_datetime()}']

    # Run create
    answer_create = crud.create_db(connection_rds, table, coluns, values)

    # Example read
    # Inform params to read
    read = '''
        SELECT
            *
        FROM
            crudpython
        ;
    '''

    # Run select
    answer_read = crud.read_db(connection_rds, read)

    print(answer_read)

    # Pause to validating alter in db
    input("Press Enter after validating in db to continue...")

    # Example update
    # Inform params to update
    table = 'crudpython'

    set = {
        'nome': 'NomeUpdate',
        'sobrenome': 'SobrenomeUpdate',
    }

    where = {
        'crudid': '1'
    }

    # Run update
    answer_update = crud.update_db(connection_rds, table, set, where)

    # Pause to validating alter in db
    input("Press Enter after validating in db to continue...")

    # Example update
    # Inform params to update
    table = 'crudpython'

    where = {
        'crudid': '1'
    }

    # Run delete
    answer_delete = crud.delete_db(connection_rds, table, where)

    # Close connection to rds
    connection_rds.close()
