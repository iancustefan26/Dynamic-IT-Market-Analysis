
import mysql.connector
from usable import aboslute_path

db_password = open(aboslute_path + "credentials/db_password.txt", "r").read(64).strip()

connection = mysql.connector.connect(
    host = 'localhost',
    user = 'stefan',
    password =  db_password,
    database = 'jobs'
)

cursor = connection.cursor()

def store_for_one_role(table_name, role_id, skill_id, count, skill_column_name):
    global cursor, connection
    query = f"""INSERT INTO {table_name} (role_id, {skill_column_name}, count)
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY UPDATE count = count + VALUES(count)"""
    data = (role_id, skill_id, count)
    try:
        cursor.execute(query, data)
        connection.commit()
        print(cursor.rowcount, "record inserted.")
    except Exception as e:
        print(f"Error: {e}")


def extract_count_for_role(role_id, skill_name):
    global connection, cursor
    table_name = ""
    column_name = ""
    if skill_name == "databases":
        table_name = "dbases"
    else:
        table_name = skill_name
    if skill_name == "libraries":
        column_name = "library"
    else:
        column_name = skill_name[:-1]
    query = f"""SELECT r.name as role_name, s.name as skill_name, rs.count
                FROM role_{skill_name} rs
                JOIN roles r ON rs.role_id = r.id
                JOIN {table_name} s ON rs.{column_name}_id = s.id
                WHERE r.id = {role_id};"""
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def clear_database():
    global connection, cursor

    try:
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        for (table_name,) in tables:
            cursor.execute(f"TRUNCATE TABLE {table_name}")
        connection.commit()

    except Exception as e:
        print(f"Error: {e}")


def close_database():
    global connection, cursor
    if connection.is_connected():
            cursor.close()
            connection.close()
            print('Database connection closed.')



