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
    cursor.execute(query, data)
    connection.commit()
    print(cursor.rowcount, "record inserted.")

def extract_count_for_role(role_id, skill_name):
    global connection, cursor
    table_name = ""
    if skill_name == "databases":
        table_name = "dbases"
    else:
        table_name = skill_name
    query = f"""SELECT r.name as role_name, s.name as skill_name, rs.count
                FROM role_{skill_name} rs
                JOIN roles r ON rs.role_id = r.id
                JOIN {table_name} s ON rs.{skill_name[:-1]}_id = s.id
                WHERE r.id = {role_id};"""
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)
    return result


store_for_one_role("role_databases", 1, 3, 2, "database_id")
x = extract_count_for_role(1, "databases")