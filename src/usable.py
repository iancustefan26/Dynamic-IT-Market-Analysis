import re
import inspect


skills = [
    "languages",
    "databases",
    "frameworks",
    "tools",
    "libraries",
    "cloud_services"
]

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

roles = [
    "Software Engineer",
    "Data Scientist",
    "Machine Learning Engineer",
    "Cloud Engineer",
    "Cybersecurity Specialist"
]

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


aboslute_path = "/Users/stefaniancu/Documents/VS Code/JobScraperEngine/"  #no idea why relative path with .. doesn't work

def check_isolated_word(string, word):
    pattern = rf'(^|[^a-zA-Z]){word}([^a-zA-Z]|$)'
    return re.search(pattern, string) is not None

def check_isolated_letter(text, letter):
    
    allowed_surroundings = r'\s\.,;\/\\|\b'
    pattern = rf'(?<=[{allowed_surroundings}]){re.escape(letter)}(?=[{allowed_surroundings}])'
    matches = re.findall(pattern, text)
    
    return bool(matches)

def get_variable_name(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    for var_name, var_val in callers_local_vars:
        if var_val is var:
            return var_name