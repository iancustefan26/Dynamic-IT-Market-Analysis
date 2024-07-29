from scraper import get_skills_for_all_roles
from scraper import get_skills_for_role
from json_convertor import extract_countries
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
                VALUES (%s, %s, %s)"""
    data = (role_id, skill_id, count)
    cursor.execute(query, data)
    connection.commit()
    print(cursor.rowcount, "record inserted.")

roles_id = {
    "Software Engineer" : 1,
    "Data Scientist" : 2,
    "Machine Learning Engineer" : 3,
    "Cloud Engineer" : 4,
    "Cybersecurity Specialist" : 5
}

locations = extract_countries(90)

store_for_one_role("role_languages", 1, 1, 3, "language_id")

query = "SELECT * FROM role_languages"
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print(row)