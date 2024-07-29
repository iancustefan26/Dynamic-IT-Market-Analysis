from scraper import get_skills_for_all_roles, get_skills_for_role
from json_convertor import extract_countries
from store_into_database import store_for_one_role, extract_count_for_role, roles_id, skills_id

locations = extract_countries(7)

results = get_skills_for_role("Data Scientist", locations)


table_names = [
    'role_languages',
    'role_cloud_services',
    'role_tools',
    'role_databases',
    'role_frameworks',
    'role_libraries'
]

skill_column_names = [
    "language_id",
    "cloud_service_id",
    "tool_id",
    "database_id",
    "framework_id",
    "library_id"
]

skills = [
    "languages",
    "databases",
    "frameworks",
    "tools",
    "libraries",
    "cloud_services"
]

for dict, table_name, column_name in zip(results, table_names, skill_column_names):
    for skill in dict:
        #print(1, skills_id[skill], dict[skill])
        store_for_one_role(
            table_name,
            roles_id["Data Scientist"],
            skills_id[skill],
            dict[skill],
            column_name
        )

print(f"Searchings have been done for locations : {locations}")

for skill in skills:
    extract_count_for_role(2, skill)