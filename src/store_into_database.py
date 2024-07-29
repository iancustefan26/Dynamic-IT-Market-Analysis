from scraper import get_skills_for_all_roles
from scraper import get_skills_for_role
from json_convertor import extract_countries
import mysql.connector
from usable import aboslute_path

roles_id = {
    "Software Engineer" : 1,
    "Data Scientist" : 2,
    "Machine Learning Engineer" : 3,
    "Cloud Engineer" : 4,
    "Cybersecurity Specialist" : 5
}

skills_id = {
    "Tableau" : 1,
    'Excel' : 2,
    'Word' : 3,
    'SAS' : 4,
    'PowerPoint' : 5,
    'SAP' : 6,
    'Looker' : 7,
    'SSIS' : 8,
    'Docker' : 9,
    'Kubernetes' : 10,
    'Linux' : 11,
    'Server' : 1,
    'MySQL' : 2,
    'Postgre' : 3,
    'Cassandra' : 4,
    'Mongo' : 5,
    'Firebase' : 6,
    'Elasticsearch' : 7,
    'Dynamo' : 8,
    'AWS' : 1,
    'Azure' : 2,
    'Google' : 3,
    'Snowflake' : 4,
    'Databricks' : 5,
    'Redshift' : 6,
    'Oracle' : 7,
    'Redshift' : 8,
    'GCP' : 9,
    'Spark' : 1,
    'Hadoop' : 2,
    'Kafka' : 3,
    'Airflow' : 4,
    'PySpark' : 5,
    'TensorFlow' : 6,
    'Pandas' : 7,
    'PyTorch' : 8,
    'NumPy' : 9,
    'Spring' : 10,
    'Matplotlib' : 11,
    'Express' : 1,
    'Node' : 2,
    'Angular' : 3,
    'Flask' : 4,
    'Django' : 5,
    'Phoenix' : 6,
    'Vue' : 7,
    'FastAPI' : 8,
    '¡Query' : 9,
    'Ruby on Rails' : 10,
    '.NET' : 11,
    'C++' : 1,
    'C' : 2,
    'Fortran' : 3,
    'Java' : 4,
    'Python' : 5,
    'PHP' : 6,
    'Ruby' : 7,
    'Rust' : 8,
    'C#' : 9,
    'Go' : 10,
    'JavaScript' : 11,
    'R' : 12,
    'Bash' : 13,
    'SQL' : 14,
    'NoSQL' : 15
}


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
                VALUES (%s, %s, %s)"""
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
    for row in result:
        print(row)
    return result

def clear_database():
    global connection, cursor

    try:
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        for (table_name,) in tables:
            cursor.execute(f"TRUNCATE TABLE {table_name}")
            #print(f"Table {table_name} truncated.")

        connection.commit()

    except Exception as e:
        print(f"Error: {e}")


def close_database():
    global connection, cursor
    if connection.is_connected():
            cursor.close()
            connection.close()
            print('Database connection closed.')



