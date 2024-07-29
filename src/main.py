from scraper import get_skills_for_all_roles, get_skills_for_role
from json_convertor import extract_countries
from store_into_database import store_for_one_role, extract_count_for_role, roles_id, skills_id

locations = extract_countries(3)

#results = get_skills_for_role("Software Engineer", locations)

results = [{'C++': 19, 'C': 7, 'Fortran': 0, 'Java': 20, 'Python': 12, 'PHP': 0, 'Ruby': 4, 'Rust': 0, 'C#': 4, 'Go': 4, 'JavaScript': 9, 'R': 4, 'Bash': 0, 'SQL': 13, 'NoSQL': 0}, {'AWS': 6, 'Azure': 3, 'Google': 0, 'Snowflake': 0, 'Databricks': 0, 'Redshift': 0, 'Oracle': 8, 'GCP': 3}, {'Tableau': 0, 'Excel': 3, 'Word': 0, 'SAS': 0, 'PowerPoint': 0, 'SAP': 4, 'Looker': 0, 'SSIS': 0, 'Docker': 0, 'Kubernetes': 4, 'Linux': 8}, {'Server': 4, 'MySQL': 0, 'Postgre': 0, 'Cassandra': 0, 'Mongo': 1, 'Firebase': 0, 'Elasticsearch': 0, 'Dynamo': 0}, {'Express': 0, 'Node': 5, 'Angular': 6, 'Flask': 0, 'Django': 0, 'Phoenix': 0, 'Vue': 0, 'FastAPI': 0, '¡Query': 0, 'Ruby on Rails': 0, '.NET': 0}, {'Spark': 0, 'Hadoop': 0, 'Kafka': 7, 'Airflow': 0, 'PySpark': 0, 'TensorFlow': 0, 'Pandas': 0, 'PyTorch': 0, 'NumPy': 0, 'Spring': 4, 'Matplotlib': 0}]

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
            roles_id["Software Engineer"],
            skills_id[skill],
            dict[skill],
            column_name
        )

for skill in skills:
    extract_count_for_role(1, skill)