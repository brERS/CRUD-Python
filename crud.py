import subprocess

import mysql.connector
from mysql.connector import Error

import log


# Function to read file my.cnf and get password
def get_file_password():

    # Create subprocess to read file and get password
    answer = subprocess.run(
        ['grep', '-Ri', 'password=', '/etc/mysql/my.cnf'], stdout=subprocess.PIPE)
    # Store output
    answer = answer.stdout
    # Set decode charSet
    answer = answer.decode('UTF-8')
    # Separating content from the variable
    answer = answer.split("=")
    # Removing unnecessary quotation marks
    answer = answer[1].replace("'", '')
    # Removing unnecessary line break
    answer = answer.replace("\n", '')

    return answer


# Function from connect to a db
def create_db_connection_rds():

    try:
        
        params = {
            'host':'127.0.0.1',
            'user':'crudteste',
            'port':'3306',
            'database':'teste_crud',
            'password':'passcrudteste',
            'auth_plugin':'mysql_native_password' 
            
            # caso tenha configurado o user e pass no arquivo my.cnf do mysql pode usar a opção abaixo
            # 'password': get_file_password(),
        }

        answer = mysql.connector.connect(**params)
        
    except Error as err:
        answer = err

        # Save the log to debug later
        log.save_log(str(answer), 'connect_db_error')
    finally:
        return answer


# Function to run a create
def create_db(connection, table, coluns, values):
    connection.autocommit = False
    cursor = connection.cursor()
    params_coluns = ''
    params_values = ''

    for x in coluns:
        params_coluns += x + ','

    for x in values:
        params_values += "'" + x + "',"

    # Formatting update variable
    create = f'INSERT INTO {table} ({params_coluns[:-1]}) VALUES ({params_values[:-1]});'  # noqa: E501

    try:
        # Executing update
        cursor.execute(create)
        connection.commit()

        # Checking update
        effect_row = cursor.rowcount

        if effect_row == 0:
            answer = 'Create failure'

            # Save the log to debug later
            log.save_log(str(answer), 'create_db')
        else:
            answer = 'Create success'

            # Save the log to debug later
            log.save_log(str(answer), 'create_db')

    except Error as err:
        answer = err

        # Save the log to debug later
        log.save_log(str(answer), 'create_db')

        # Reverting changes because of exception
        connection.rollback()

    finally:
        cursor.close()

        return answer


# Function to run a read
def read_db(connection, query):
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        answer = cursor.fetchall()
    except Error as err:
        answer = err

        # Save the log to debug later
        log.save_log(str(answer), 'read_db')

    finally:
        cursor.close()

        return answer


# Function to run a update
def update_db(connection, table, set, where):

    # Validating not to execute without the parameter where
    if not where:
        answer = 'Oh no, running update without where?!'

        # Save the log to debug later
        log.save_log(str(answer), 'update_db')

        return answer

    connection.autocommit = False
    cursor = connection.cursor()

    # Declaring variables
    params_set = ''
    params_where = ''

    # For to organize params
    for i in set:
        params_set += str("`" + str(i) + "`='" + str(set[i]) + "', ")
    for i in where:
        params_where += str("`" + str(i) + "`='" + str(where[i]) + "', ")

    # Formatting update variable
    update = f'UPDATE {table} SET {params_set[:-2]} WHERE {params_where[:-2]};'

    try:
        # Executing update
        cursor.execute(update)
        connection.commit()

        # Checking update
        effect_row = cursor.rowcount

        if effect_row == 0:
            answer = 'Update failure'

            # Save the log to debug later
            log.save_log(str(answer), 'update_db')
        else:
            answer = 'Update success'

            # Save the log to debug later
            log.save_log(str(answer), 'update_db')

    except Error as err:
        answer = err

        # Save the log to debug later
        log.save_log(str(answer), 'update_db')

        # Reverting changes because of exception
        connection.rollback()

    finally:
        cursor.close()

        return answer


# Function to run a update
def delete_db(connection, table, where):

    # Validating not to execute without the parameter where
    if not where:
        answer = 'Oh no, running delete without where?!'

        # Save the log to debug later
        log.save_log(str(answer), 'delete_db')

        return answer

    connection.autocommit = False
    cursor = connection.cursor()

    # Declaring variables
    params_where = ''

    for i in where:
        params_where += str("`" + str(i) + "`='" + str(where[i]) + "', ")

    # Formatting update variable
    delete = f'DELETE FROM {table} WHERE {params_where[:-2]};'

    try:
        # Executing update
        cursor.execute(delete)
        connection.commit()

        # Checking update
        effect_row = cursor.rowcount

        if effect_row == 0:
            answer = 'Delete failure'

            # Save the log to debug later
            log.save_log(str(answer), 'delete_db')
        else:
            answer = 'Delete success'

            # Save the log to debug later
            log.save_log(str(answer), 'delete_db')

    except Error as err:
        answer = err

        # Save the log to debug later
        log.save_log(str(answer), 'delete_db')

        # Reverting changes because of exception
        connection.rollback()

    finally:
        cursor.close()

        return answer
