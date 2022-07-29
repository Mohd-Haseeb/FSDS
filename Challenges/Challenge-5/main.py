import mysql.connector
from mysql.connector import Error

def connect_to_mysql(host_name, user_name, password):
    myConnection = None
    try:
        myConnection = mysql.connector.connect(
            host=host_name,
            user = user_name,
            passwd = password,
            use_pure=True,
            auth_plugin='mysql_native_password'
        )

    except Error as e:
        print("CONNECTION FAILED!!")
        print(f"Error : {e}")
    
    return myConnection


def close_connection(connection):
    connection.close()
    print("CONNECTION CLOSED SUCCESSFULLY!!!")


def execute_query_databases(connection, query):
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        print(cursor.fetchall())
        
        # connection.commit()
        print("QUERY EXECUTION SUCCESSFULLY!!")
    except Error as e:
        print("EXECUTION FAILES...")
        print(f"Error : {e}")
    finally:
        cursor.close()

def database_tables(connection ,database_name):
    cursor = connection.cursor()

    myQuery = f"""
            USE {database_name};
            SELECT table_name FROM information_schema.tables;
    """

    cursor.execute(myQuery, multi=True)

    all_tables = cursor.fetchmany()

    print(all_tables)

    for table_name in cursor:
       print(table_name)


def get_table_data(connection, database_name, table_name):
   
    query = f"""
        
        SELECT * FROM {database_name}.{table_name};
    """

    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print(cursor.fetchall())
    except Error as e:
        print(f"Error : {e}")
    finally:
        cursor.close()


def connect_and_read_data(host_name, user_name, password):
    connection = mysql.connector.connect(host=host_name, user=user_name, password=password, use_pure=True, auth_plugin='mysql_native_password')

    cursor = connection.cursor()

    query = """
        SELECT * FROM bank.bank_details;
    """

    cursor.execute(query)
    all_table_data = cursor.fetchall()

    for row in all_table_data:
        print(row)


    cursor.close()
    connection.close()

connect_and_read_data('localhost','root','haseeb123')

# if __name__=='__main__':


#     connection = connect_to_mysql('localhost','root','haseeb123')

#     query = 'SHOW DATABASES'

#     query2 = """
#         USE bank;
#         SHOW TABLES;
#     """

#     # execute_query_databases(connection=connection, query=query)

#     # database_tables(connection=connection, database_name='bank')

#     get_table_data(connection, database_name='bank', table_name='bank_details')



#     close_connection(connection)

