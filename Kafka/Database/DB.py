import json
import psycopg2
from psycopg2 import Error


def InsertIntoDB(table_name, data):
    create_query, insert_query = Parse(table_name, data)

    try:

        connection = DBConnection()  # Get DB Connection

        cursor = connection.cursor()  # Get cursor object

        cursor.execute(create_query)  # Execute a command: this creates a new table
        cursor.execute(insert_query)  # Execute a command: this insert values into table
        connection.commit()

        print("Data inserted successfully in PostgreSQL")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def Parse(table_name, data):
    data = json.loads(data)
    columns = [list(x.keys())[0] for x in data]
    column_datatype = list(map((lambda x: x + ' VARCHAR(20)'), columns))

    values = [list(x.values())[0] for x in data]
    values = list(map((lambda x: "'" + x + "'"), values))

    create_query = 'CREATE TABLE ' + table_name + '(' + ', '.join(column_datatype) + ');'

    insert_query = 'INSERT INTO ' + table_name + '(' + ', '.join(columns) + ') VALUES' + '(' + ', '.join(
        values) + ');'

    return create_query, insert_query


def DBConnection():
    connection = psycopg2.connect(user="jai",
                                  password="root",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="jai")

    return connection
