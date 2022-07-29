import mysql.connector
from mysql.connector import Error

class Database: 
    __connection = None
    def __init__(self,host_name, user_name, password):
        self.__connection = mysql.connector.connect(host=host_name, user = user_name, password=password, use_pure=True, auth_plugin='mysql_native_password')
        
        all_databases = """
            SHOW DATABASES
        """
    
    def get_table_data(self,table_name, database_name):
        query = f"""
            SELECT * FROM {database_name}.{table_name};
        """
        try:
            curr = self.__connection.cursor()

            curr.execute(query)
            all_rows = curr.fetchall()

            for row in all_rows:
                print(row)

        except Error as e:
            print(f"Error -> {e}")

        curr.close()
    
    def close_connection(self):
        self.__connection.close()
        print('CONNECTION CLOSED SUCCESSFULY!!!')

    def show_databases(self):
        all_databases = """
            SHOW DATABASES
        """

        curr = self.__connection.cursor()

        curr.execute(all_databases)
        databases =  curr.fetchall()

        for db in databases:
            print(db)

        curr.close()

    def create_database(self,database_name):
        query = f"""
            CREATE DATABASE {database_name}
        """
        try:
            cursor = self.__connection.cursor()
            cursor.execute(query)
            self.__connection.commit()

            print('DATABASE IS CREATED SUCCESSFULLY!!!')
        except Error as e:
            print('ERROR IN CREATING DATABASE!!!')
            print(f"Error -> {e}")
        
        finally:
            cursor.close()
            self.show_databases()

    def create_table(self,databae_name,query):
        try:
            cursor = self.__connection.cursor()
            cursor.execute(query.format(database_name=databae_name))
            self.__connection.commit()
            print("TABLE IS CREATED SUCCESSFULLY!!!")
        except Error as e:
            print("ERROR OCCURED WHILE CREATING A TABLE!!!")
            print(f"Error -> {e}")
        finally:
            cursor.close()

db = Database('localhost','root','<your password>')

db.get_table_data(table_name='ui_sales', database_name='dummytest')

# db.show_databases()

# db.create_database("dummytest")

create_table_attribute = """
    CREATE TABLE IF NOT EXISTS {database_name}.attribute(
        Dress_ID varchar(30) not null,Style varchar(30), Price varchar(30), Rating varchar(30), Size varchar(30), Season varchar(30),
         NeckLine varchar(30),
       SleeveLength varchar(30), waiseline varchar(30), Material varchar(30), FabricType varchar(30), Decoration varchar(30),
       PatternType varchar(30), Recommendation int
    )
"""

create_table_sales = """
    CREATE TABLE IF NOT EXISTS {database_name}.dressSales(
       Dress_ID int, `29/8/2013`int, `31/8/2013`  int, `2013-02-09` int,
       `2013-04-09` int, `2013-06-09` int, `2013-08-09` int,
       `2013-10-09` int, `2013-12-09` int, `14/9/2013` int, `16/9/2013` int,
       `18/9/2013` int, `20/9/2013` int, `22/9/2013` int, `24/9/2013` int, `26/9/2013` int,
       `28/9/2013` int, `30/9/2013` int, `2013-02-10` int, `2013-04-10` int,
       `2013-06-10` int, `2010-08-10` int, `2013-10-10` int,
       `2013-12-10` int
    )
"""



# db.create_table('dummytest',create_table_sales)

bulk_load_attribute = """
    LOAD DATA INFILE '/Users/mohdhaseeb/Desktop/FSDS-Bootcamp/FSDS_DATA_SET/atribute.csv'
    FIELDS TERMINATED BY ','
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS;
"""




db.close_connection()