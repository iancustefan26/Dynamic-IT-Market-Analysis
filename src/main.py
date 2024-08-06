from scraper import get_skills_for_role
from json_convertor import extract_countries
from db_operations import store_for_one_role, close_database
from scraper import roles
from usable import table_names, skill_column_names, roles_id, skills_id

locations = extract_countries(6)

for role in roles:
    results = get_skills_for_role(role, locations)
    print(results)
    for dict, table_name, column_name in zip(results, table_names, skill_column_names):
        for skill in dict:
            store_for_one_role(
                table_name,
                roles_id[role],
                skills_id[skill],
                dict[skill],
                column_name
            )
            
close_database()